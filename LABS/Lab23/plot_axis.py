import numpy as np
import matplotlib.pyplot as pyplot

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 8, 10, 12, 14, 20, 22]

pyplot.plot(a, b)

pyplot.axis((0, 10, 0, 30)) # 튜플
pyplot.axis([0, 10, 0, 30]) # 리스트

pyplot.show()

