import numpy as np
import matplotlib.pyplot as pyplot

a = np.arange(1, 5) # [1, 2, 3, 4]
b = np.arange(3, 7) # [3, 4, 5, 6]

pyplot.plot(a, b, 'r')

# b = [9, 16, 25, 36] -s = square 직선
pyplot.plot(a, b**2,'b-s', label = "$b^2$")

# color가 cyan
pyplot.plot(a, a**3, 'c:^', label = "letgo")

pyplot.legend()

pyplot.show()

