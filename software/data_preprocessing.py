#
# Copyright (C) 2013  UNIVERSIDAD DE CHILE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors: Karel Mundnich <kmundnic@ing.uchile.cl>

import numpy as np

DIRECTIONS = ('NORTH', 'SOUTH')
EXCITATION_LENGTH = 250
ECHO_LENGTH = 1400
SIGNAL_LENGTH = 2200

def frame_sanity_check(frame):
  """ Prevents non-desired behavior where the collected frame does not include
      the excitation pulses sent to the transducer.
      The existence of the excitation pulses is determined by thresholding the
      derivative of the frame.
  """
  # A threshold of 2000 is used since the ADC saturates at 2048, and the 
  # excitation pulses reach the 2000 level. Therefore, the derivative must be
  # higher than 2000.
  if np.max(np.diff(frame)) > 2000:
    return True
  else:
    return False

def flank_detection(frame):
  """ Detect the first excitation pulse (flank) of the frame by using zero-
      crossings.
  """
  assert len(frame) > 0
  return np.where(np.diff(np.sign(frame)))[0][0]


def split_frame(frame, number_of_measurements):
  """ Splits the complete measurement frame into several echoes that are
      returned in a list of dictionaries. Each list item represents a 
      measurement, and each dictionary entry contains a key in 
      DIRECTIONS = ('NORTH','SOUTH') and a value consisting of a numpy array
      that includes the echo for that measurement.
  """
  echo = dict() # Create an echo dictionary
  echoes = [] # Create an echoes list.

  for i in range(number_of_measurements):
    try:
      for direction in DIRECTIONS:
        # Perform sanity check for only 1 signal in frame
        assert frame_sanity_check(frame[0:SIGNAL_LENGTH])
  
        # Detect the flank of the excitation pulse
        flank = flank_detection(frame)
        
        # We save the first excitation + echo from the frame and then delete it 
        # from the frame
        signal = frame[flank:flank + SIGNAL_LENGTH]
        frame = frame[flank + SIGNAL_LENGTH:-1]
        
        # Save the measurement for each direction in a dictionary
        echo[direction] = signal[EXCITATION_LENGTH:EXCITATION_LENGTH + \
                                                   ECHO_LENGTH]
    except:
      # If sanity check is False, the frame is cut to check for the next
      # excitation pulse. Because of the Enable in (nombrar archivo), the signal
      # always returns to -1501. We use this information to find the following
      # excitation + echo. If no pre-excitation stage is found, None is
      # returned.
      try:
        idx = np.where(frame = -1501)[0][0]
        frame = frame[idx:-1]
      except:
        return None
      
    echoes.append(echo)
    
  return echoes