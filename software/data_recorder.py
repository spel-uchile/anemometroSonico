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
from scipy.io import netcdf

import adc_reader


parser = argparse.ArgumentParser()
parser.add_argument("--repetitions", type=int,
                    help="Number of frames to record.")
parser.add_argument("--prefix",
                    help="Prefix of the files (including output directory.")
args = parser.parse_args()

reader = adc_reader.ADCReader()

data = np.zeros((args.repetitions, adc_reader.kFrameSize))

print "Recording to " + args.prefix
reader.GetNFrames(data)
np.save(args.prefix, data)
