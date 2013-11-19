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

import data_preprocessing as dpp
import numpy as np
import unittest

class TestDataPreprocessing(unittest.TestCase):
  
  def setUp(self):
    self.file_noecho = './test_data/frame_no_echo.nc'
    self.file_v_zero = './test_data/frame_v_zero.nc'
    self.file_faulty = './test_data/frame_with_faulty_excitation.nc'
    self.file_noexci = './test_data/frame_with_no_excitation.nc'
    
  def test_load_data_from_file(self):
    self.assertEqual(type(dpp.load_data_from_file(self.file_noecho)),
                     np.ndarray)
    self.assertEqual(type(dpp.load_data_from_file(self.file_v_zero)),
                     np.ndarray)
    self.assertEqual(type(dpp.load_data_from_file(self.file_faulty)),
                     np.ndarray)
    self.assertEqual(type(dpp.load_data_from_file(self.file_noexci)),
                     np.ndarray)
    
  def test_frame_sanity_check(self):
    measurement_noecho = dpp.load_data_from_file(self.file_noecho)
    self.assertTrue(dpp.frame_sanity_check(measurement_noecho))
    
    measurement_v_zero = dpp.load_data_from_file(self.file_v_zero)
    self.assertTrue(dpp.frame_sanity_check(measurement_v_zero))
    
    measurement_faulty = dpp.load_data_from_file(self.file_faulty)
    self.assertFalse(dpp.frame_sanity_check(measurement_faulty))
    
    measurement_noexci = dpp.load_data_from_file(self.file_noexci)
    self.assertFalse(dpp.frame_sanity_check(measurement_noexci))
    
  def test_edge_detection(self):
    measurement_noecho = dpp.load_data_from_file(self.file_noecho)
    self.assertEqual(dpp.edge_detection(measurement_noecho), 783)
    
    measurement_v_zero = dpp.load_data_from_file(self.file_v_zero)
    self.assertEqual(dpp.edge_detection(measurement_v_zero), 810)

  def test_split_frame(self):
    echoes_v_zero = dpp.split_frame(dpp.load_data_from_file(self.file_v_zero))
    self.assertTrue(np.max(echoes_v_zero[0]['NORTH']) in np.arange(400, 600))
    
    echoes_faulty = dpp.split_frame(dpp.load_data_from_file(self.file_faulty))
    self.assertEqual(echoes_faulty, None)
    
  
if __name__ == '__main__':
  unittest.main()