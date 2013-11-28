cmake_minimum_required (VERSION 2.6)
project (UchUltrasonicAnemometer)

# Copy python files to build directory so they can find the compiled swig
# wrappers
function(add_python_source)
  foreach(file ${ARGN})
    add_custom_command(
      OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${file}
      COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_CURRENT_SOURCE_DIR}/${file} ${CMAKE_CURRENT_BINARY_DIR}/${file}
      MAIN_DEPENDENCY ${CMAKE_CURRENT_SOURCE_DIR}/${file})

    STRING(REGEX REPLACE "/" "_" target_name ${CMAKE_CURRENT_BINARY_DIR}/${file})
    add_custom_target(${target_name} ALL DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/${file})

  endforeach()
endfunction()

set(CMAKE_CXX_FLAGS "-std=c++0x")
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})
find_package(PythonLibs)
include_directories(${PYTHON_INCLUDE_PATH})

#python targets
add_python_source(plot_from_adc.py data_recorder.py)

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
