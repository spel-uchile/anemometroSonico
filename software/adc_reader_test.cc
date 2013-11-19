#include "adc_reader.h"
#include "gtest/gtest.h"

TEST(ADCReaderTest, DataConversion) {
  ADCReader reader;
  int16_t zero = 0;

  int16_t two_thousand;
  ((char*)(&two_thousand))[0] = 0x07;
  ((char*)(&two_thousand))[1] = 0xD0;

  int16_t minus_two_thousand;
  ((char*)(&minus_two_thousand))[0] = 0x08;
  ((char*)(&minus_two_thousand))[1] = 0x30;

  EXPECT_EQ(0, reader.ConvertFromADCFormat(zero));
  EXPECT_EQ(2000, reader.ConvertFromADCFormat(two_thousand));
  EXPECT_EQ(-2000, reader.ConvertFromADCFormat(minus_two_thousand));
}
