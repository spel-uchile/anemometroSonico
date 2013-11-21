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

import utilities
import numpy as np
import unittest

class TestUtilities(unittest.TestCase):
  
  def setUp(self):
    # Data paths
    self.file_noecho = './test_data/frame_no_echo.nc'
    
  def test_load_data_from_file(self):
    self.assertEqual(type(utilities.load_data_from_file(self.file_noecho)),
                     np.ndarray)
    self.assertNotEqual(type(self.echoes_noecho), dict)
    self.assertRaises(IOError, utilities.load_data_from_file, 
                      'non_existent_file.nc')
                     
if __name__ == '__main__':
  unittest.main()