import adc_reader
import numpy as np

from pylab import *

data = np.zeros(10000)

reader = adc_reader.ADCReader()
reader.GetFrame(data)

plot(data)
show()

print data

