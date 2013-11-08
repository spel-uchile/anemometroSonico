cmake_minimum_required (VERSION 2.6)
project (UchUltrasonicAnemometer)

set(CMAKE_CXX_FLAGS "-std=c++0x")
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
find_package(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})

#python targets
file(COPY plot_from_adc.py DESTINATION .)
file(COPY data_recorder.py DESTINATION .)

# Swig targets
SET_SOURCE_FILES_PROPERTIES(adc_reader.i PROPERTIES CPLUSPLUS ON)
SWIG_ADD_MODULE(adc_reader python adc_reader.i adc_reader.cc)
SWIG_LINK_LIBRARIES(adc_reader ${PYTHON_LIBRARIES} mpsse)

# Test targets
add_subdirectory(gtest)
enable_testing()
include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})
add_executable(adc_reader_test adc_reader_test.cc adc_reader.cc)
target_link_libraries(adc_reader_test gtest gtest_main mpsse)
add_test(adc_reader_test adc_reader_test)
