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

from scipy.io import netcdf
import numpy as np

def load_data_from_file(file_path):
  """ Loads data from and NetCDF file and returns a numpy.ndarray with the full
      data frame.
  """
  # Open data
  f = netcdf.netcdf_file(file_path, 'r')
  # Load data into a variable  
  aux = f.variables['frame']
  # Copy data into a new numpy array for security
  measurement = np.array(aux.data)
  f.close()
  return measurement