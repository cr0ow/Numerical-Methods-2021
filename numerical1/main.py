import math as m
import numpy as np
import matplotlib.pyplot as mpl

#tablice do trzymania wynikow obliczen
y1 = []
x1 = []
y2 = []
x2 = []

#obliczenia dla podpunktu A
for h in np.arange(1*pow(10, -10), 1*pow(10, -6), 9*pow(10, -11)):
    logE1 = m.log(abs((m.cos(0.3 + h) - m.cos(0.3)) / h + m.sin(0.3)), m.e)
    y1.append(logE1)
    logH1 = m.log(h, m.e)
    x1.append(logH1)

#obliczenia dla podpunktu B
for h in np.arange(1*pow(10, -9), 1*pow(10, -3), 9*pow(10, -10)):
    logE2 = m.log(abs((m.cos(0.3 + h) - m.cos(0.3 - h)) / (2 * h) + m.sin(0.3)), m.e)
    y2.append(logE2)
    logH2 = m.log(h, m.e)
    x2.append(logH2)

#rysowanie wykresu
mpl.plot(x1, y1, label="wykres A")
mpl.plot(x2, y2, label="wykres B")
mpl.xlabel("log h ")
mpl.ylabel("log E(h)")
mpl.legend()
mpl.show()
