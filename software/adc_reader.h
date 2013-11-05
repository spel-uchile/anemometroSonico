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

#ifndef ADC_READER_H_
#define ADC_READER_H_

#include <cstdint>

struct mpsse_context;

/** This class provides access to the hardware of the anemometer.
 *
 *  This connection is implemented using an analog-digital converter (ADC)
 *  connected to the USB though an SPI-USB bridge.
 */
class ADCReader {
public:
  /** Opens a communication channel with the underlying ADC. */
  ADCReader();
  /** Closes the communication channel with the underlying ADC. */
  ~ADCReader();

  /** Reads one frame of data from the anemometer. This frame consists of two
   *  measurements per direction. Each direction includes the excitation signal
   * on one transducer and the echo of the paired transducer.
   */
  void GetFrame(int16_t *buffer, unsigned int buffer_size);
private:
  //! Communication interface with the ADC
  struct mpsse_context *adc_;
  //! Speed of the communication with the ADC. The actual sampling rate can be
  //! calculated as kSpiClock/16.
  static const int kSpiClock = 15000000;
};

#endif  // ADC_READER_H_
