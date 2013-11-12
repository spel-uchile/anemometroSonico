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

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import netcdf
import data_preprocessing as dpp

file_noecho = '/Users/karel/Dropbox/Anemometro/AnemometroSonico/samples/20131108/noecho/_0090.nc'
file_v_zero = '/Users/karel/Dropbox/Anemometro/AnemometroSonico/samples/20131108/v_zero/_0090.nc'

# Load data
f = netcdf.netcdf_file(file_noecho, 'r')
measurement_noecho = f.variables['frame']
f.close()

f = netcdf.netcdf_file(file_v_zero, 'r')
measurement_v_zero = f.variables['frame']
f.close()

# Plot raw data
plt.figure()
plt.plot(measurement_noecho.data)
plt.plot(measurement_v_zero.data)
plt.grid(True)

print "Sanity check noecho:", dpp.frame_sanity_check(measurement_noecho.data)
print "Sanity check v_zero:", dpp.frame_sanity_check(measurement_v_zero.data)

# Check signal rise
flank_noecho = dpp.flank_detection(measurement_noecho.data)
flank_v_zero = dpp.flank_detection(measurement_v_zero.data)
print "Zero crossings noecho:", flank_noecho
print "Zero crossings v_zero:", flank_v_zero

# Plot aligned data
plt.figure(2)
plt.plot(measurement_noecho.data[flank_noecho:flank_noecho + 6000])
plt.plot(measurement_v_zero.data[flank_v_zero:flank_v_zero + 6000])
plt.grid(True)

# Plot 'clean' frame (v_zero - noecho)
#bla = measurement_v_zero.data[flank_v_zero:flank_v_zero + 6000] - measurement_noecho.data[flank_noecho:flank_noecho + 6000]
#plt.plot(bla, 'r')

# Retrieve echoes
#NORTH = measurement_v_zero.data[flank_noecho + excitation_length:flank_noecho + excitation_length + echo_length]
#plt.figure()
#plt.plot(NORTH,'r')
#
#signal = measurement_v_zero[flank_v_zero:flank_v_zero + signal_length]
#plt.plot(signal)
  
echoes_noecho = dpp.split_frame(measurement_noecho.data, 1)
echoes_v_zero = dpp.split_frame(measurement_v_zero.data, 1)

plt.figure(4)
plt.plot(echoes_noecho[0]['NORTH'])
plt.plot(echoes_noecho[0]['SOUTH'])
plt.grid(True)


plt.figure(5)
plt.plot(echoes_v_zero[0]['NORTH'])
plt.plot(echoes_v_zero[0]['SOUTH'])
plt.grid(True)

plt.figure(6)
plt.plot(echoes_v_zero[0]['NORTH'] - echoes_noecho[0]['NORTH'])
plt.plot(echoes_v_zero[0]['SOUTH'] - echoes_noecho[0]['SOUTH'])
plt.grid(True)

