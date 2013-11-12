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
from scipy.io import netcdf
import data_preprocessing as dpp

path = '/Users/karel/Dropbox/Anemometro/AnemometroSonico/samples/20131108'
file_noecho = '/noecho/_0090.nc'
file_v_zero = '/v_zero/_0090.nc'

# Load data
f = netcdf.netcdf_file(path + file_noecho, 'r')
measurement_noecho = f.variables['frame']
f.close()

f = netcdf.netcdf_file(path + file_v_zero, 'r')
measurement_v_zero = f.variables['frame']
f.close()

# Plot raw data
plt.figure()
plt.plot(measurement_noecho.data)
plt.plot(measurement_v_zero.data)
plt.grid(True)
plt.title("Raw data")
plt.legend(('No echo', 'v = 0'))

# Retrieve echoes 
echoes_noecho = dpp.split_frame(measurement_noecho.data, 1)
echoes_v_zero = dpp.split_frame(measurement_v_zero.data, 1)

plt.figure()
plt.subplot(211)
plt.plot(echoes_v_zero[0]['NORTH'])
plt.plot(echoes_v_zero[0]['SOUTH'])
plt.grid(True)
plt.title('Echoes for v = 0')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.legend(('NORTH','SOUTH'))
ymin, ymax = plt.ylim()

plt.subplot(212)
plt.plot(echoes_noecho[0]['NORTH'])
plt.plot(echoes_noecho[0]['SOUTH'])
plt.grid(True)
plt.title('No echo (calibration info)')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.legend(('NORTH','SOUTH'))
plt.ylim(ymin, ymax)


