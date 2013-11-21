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
import logging

# Directions of sonic measurement
DIRECTIONS = ('NORTH', 'SOUTH')
# Maximum length of the train of excitation pulses
EXCITATION_LENGTH = 250
# Maximum length of echo
ECHO_LENGTH = 1400
# Maximum length of excitation pulses plus echo
SIGNAL_LENGTH = 2200
# Number of excitation pulses in the excitation train
NUMBER_OF_PULSES = 3
# Signal period in samples
EXCITATION_PERIOD = 36
# Maximum amplitude of excitation pulses
PULSE_AMPLITUDE = 1976

def frame_sanity_check(frame):
  """ Prevents non-desired behavior where the collected frame does not include
      all of the excitation pulses sent to the transducer.
      The existence of the excitation pulses is determined by thresholding the
      derivative of the frame, and counting the amount of pulses.
  """  
  # A threshold of PULSE_AMPLITUDE is used since the ADC saturates at 2048, and
  # the excitation pulses reach the PULSE_AMPLITUDE level. Therefore, the 
  # derivative must be higher than PULSE_AMPLITUDE.
  if np.max(np.diff(frame)) > PULSE_AMPLITUDE:
    # If the condition is met, we check that there are NUMBER_OF_PULSES pulses
    # in the excitation stage of the frame.
    for i in range(NUMBER_OF_PULSES):
      idx = edge_detection(frame)
      # We check that the signal has a certain period that is related to 
      # the variable EXCITATION_PERIOD.     
      if frame[idx + np.floor(EXCITATION_PERIOD*1/4)] < 0:
        return False
      if frame[idx + np.floor(EXCITATION_PERIOD*3/4)] > 0:
        return False
      # Cut the frame and check for the rest of the pulses. We advance until 3/4
      # of the current pulse to make sure that we start looking for the next
      # rising edge before it occurs.
      frame = frame[idx + EXCITATION_PERIOD*3/4:-1]
    # If there are NUMBER_OF_PULSES pulses, we return true.
    return True
  else:
    return False

def edge_detection(frame):
  """ Detect the first excitation pulse (edge) of the frame by using zero-
      crossings.
  """
  assert len(frame) > 0
  return np.where(np.diff(np.sign(frame)))[0][0]

def split_frame(frame):
  """ Splits the complete measurement frame into several echoes that are
      returned in a list of dictionaries. Each list item represents a 
      measurement, and each dictionary entry contains a key in 
      DIRECTIONS = ('NORTH','SOUTH') and a value consisting of a numpy array
      that includes the echo for that measurement.
  """
  echo = dict() # Create an echo dictionary
  echoes = [] # Create an echoes list.

  for direction in DIRECTIONS:
    # Perform sanity check for only 1 signal in frame.
    if frame_sanity_check(frame[0:SIGNAL_LENGTH]):
      # Detect the edge of the excitation pulse
      edge = edge_detection(frame)
      
      # We save the first excitation + echo from the frame and then delete it 
      # from the frame
      signal = frame[edge:edge + SIGNAL_LENGTH]
      frame = frame[edge + SIGNAL_LENGTH:-1]
      
      # Save the measurement for each direction in a dictionary
      echo[direction] = signal[EXCITATION_LENGTH:(EXCITATION_LENGTH +
                                                  ECHO_LENGTH)]
      echoes.append(echo)

    else:
      message = 'Lost ' + direction + ' measurement...'
      logging.info(message)
      return None

  return echoes  