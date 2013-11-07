//
// Copyright (C) 2013  UNIVERSIDAD DE CHILE.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// Authors: Luis Alberto Herrera <herrera.luis.alberto@gmail.com>

// Program to read the data from ADC converter.

#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include "adc_reader.h"

#define SAMPLES 100000

int main(void) {
  int16_t *data = reinterpret_cast<int16_t*>(malloc(2*SAMPLES));

  ADCReader reader;
  reader.GetFrame(data, SAMPLES);
  fwrite(data, 1, 2*SAMPLES, stdout);
  free(data);

  return 0;
}

