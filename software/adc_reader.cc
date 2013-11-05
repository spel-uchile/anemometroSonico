/*
 * Copyright (C) 2013  UNIVERSIDAD DE CHILE.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Authors: Luis Alberto Herrera <herrera.luis.alberto@gmail.com>
 */

#include "adc_reader.h"

extern "C" {
#include <mpsse.h>
}


ADCReader::ADCReader()
  : adc_(NULL) {
  adc_ = MPSSE(SPI0, kSpiClock, MSB);
}

ADCReader::~ADCReader() {
  Close(adc_);
}

void ADCReader::GetFrame(int16_t *buffer, unsigned int buffer_size) {
  if (adc_ != NULL) {
    if (adc_->open) {
      Start(adc_);
      FastRead(adc_, (char*) buffer, buffer_size);
      Stop(adc_);

      char *left_pointer = (char*) buffer;
      char *right_pointer = left_pointer + 1;
      for (int i=0; i<buffer_size; i++) {
        char left = *left_pointer; // first 8 bits from adc
        char right = *right_pointer; // last 8 bits from adc
        //signed extension
        if (left & (1<<3)) {
          left |= 0xf0;
        }
        //swap bytes
        *left_pointer = right;
        *right_pointer = left;

        left_pointer += sizeof(int16_t);
        right_pointer += sizeof(int16_t);
      }
    }
  }
}
