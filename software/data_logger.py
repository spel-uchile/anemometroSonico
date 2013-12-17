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
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# Authors: Luis Alberto Herrera <herrera.luis.alberto@gmail.com>

import argparse
import numpy as np
import serial
import re
import os

import adc_reader


parser = argparse.ArgumentParser()
parser.add_argument("--output_folder",
                    help="Folder where the records will be stored. Must exist.")
parser.add_argument("--serial_port",
                    help="Device where the GPS is connected.")
parser.add_argument("--repetitions", type=int,
                    help="Number of frames to record.")
args = parser.parse_args()

def main():
  serial_port = serial.Serial(args.serial_port, 19200, timeout=1)
  reader = adc_reader.ADCReader()
  data = np.zeros((args.repetitions, adc_reader.kFrameSize))
  while True:
    serial_port.flushInput()
    gps_line = serial_port.readline()
    gpgga_regex = r"^\$GPRMC,(\d\d)(\d\d)(\d\d).(\d\d\d),V,.*,.,.*,.,.*,.*,(\d\d)(\d\d)(\d\d),.*"
    reg_match = re.match(gpgga_regex, gps_line)
    if reg_match:
      # output path  is output_folder + date + hour.
      # The hour is needed to keep the number of files in a single folder under 
      # control.
      output_dir = "%s/%s%s%s/%s"%(
        args.output_folder, reg_match.group(7), reg_match.group(6), 
        reg_match.group(5), reg_match.group(1))
      if not os.path.exists(output_dir):
        os.makedirs(output_dir)
      # filename is data + time.
      output_file_name = "%s/%s%s%s_%s%s%s_%s"%(
        output_dir, reg_match.group(7), reg_match.group(6), reg_match.group(5), 
        reg_match.group(1), reg_match.group(2),
        reg_match.group(3), reg_match.group(4))
      print "Recording to " + output_file_name
      reader.GetNFrames(data)
      np.save(output_file_name, data)

if __name__ == "__main__":
  main()

