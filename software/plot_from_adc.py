# Example of how to use adc_reader. It will plot one frame.

import adc_reader
import numpy as np

from pylab import *

data = np.zeros(10000)

reader = adc_reader.ADCReader()
reader.GetFrame(data)

plot(data)
show()

