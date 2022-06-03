import numpy as np
import matplotlib.pyplot as pyplot

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 8, 10, 12, 14, 20, 22]

pyplot.plot(a, b, 'r-o')
pyplot.axis((0, 10, 0, 30))

#pyplot.grid(True)
#pyplot.grid(True, axis = 'x')
pyplot.grid(True, axis = 'y')

pyplot.show()

