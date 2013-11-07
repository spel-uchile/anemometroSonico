cmake_minimum_required (VERSION 2.6)
project (UchUltrasonicAnemometer)

set(CMAKE_CXX_FLAGS "-std=c++0x")

add_executable(adc_reader adc_reader_main.cc adc_reader.cc )
target_link_libraries (adc_reader mpsse)
