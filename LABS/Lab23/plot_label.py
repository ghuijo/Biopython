import matplotlib
import numpy as np
import matplotlib.pyplot as pyplot
import matplotlib.font_manager as fm

a = ["12.16", "12.17", "12.18", "12.19", "12.21", "12.22", "12.23"]
b = [1, 8, 10, 12, 14, 20, 40]

font_prop = fm.FontProperties(fname = "C:/Windows/Fonts/gulim.ttc").get_name()
matplotlib.rc('font', family = font_prop)

pyplot.plot(a, b, 'r')
pyplot.axis((0, 10, 0, 70))

pyplot.title("비트코인 시가총액 그래프")
pyplot.ylabel("가격(단위: 천억원)")
pyplot.xlabel("날짜")
pyplot.text(2, 42, "상한가: 코로나 백신접종으로 인한 집단면역 성공")

pyplot.show()

