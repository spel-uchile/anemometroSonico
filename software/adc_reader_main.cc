/*
 * Program to read the data from ADC converter.
 *
 * Input format from ADC122S706 is 16 bits: 4 zero bits + 12 data bits (2's
 * complement). Output to stdout format is signed 16 integer little endian.
 */

#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include "adc_reader.h"

#define SAMPLES	100000

int main(void)
{
  int16_t *data = (int16_t*) malloc(2*SAMPLES);

  ADCReader reader;
  reader.GetFrame(data, SAMPLES);
  fwrite(data, 1, 2*SAMPLES, stdout);
  free(data);

  return 0;
}

