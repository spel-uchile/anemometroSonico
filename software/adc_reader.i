%{
#define SWIG_FILE_WITH_INIT
%}
%include "numpy.i"

%init %{
import_array();
%}

%module adc_reader
%{
#include "adc_reader.h"
%}

%apply (double* INPLACE_ARRAY1, int DIM1) {(double *buffer, int buffer_size)};

class ADCReader {
 public:
  ADCReader();
  ~ADCReader();
  void GetFrame(double *buffer, int buffer_size);
};
