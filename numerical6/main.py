import numpy as np
import matplotlib.pyplot as mpl
from math import cos, pi

n = [5, 10, 20, 50, 100]  # ilosc wezlow interpolacji

#
# flaga_funkcji == 1  ->  funkcja y(x)
# flaga_funkcji != 1  ->  funkcja y'(x)
# flaga_wezla == 1  ->  rozklad z przykladu a
# flaga_wezla != 1  ->  rozklad z przykladu b
#

flaga_funkcji = 2
flaga_wezla = 2


def wielomian(a, b, c, _n):
	q = np.poly1d([0])
	for i in range(_n):
		licznik = np.poly1d([1])
		mianownik = 1.
		for j in range(_n):
			if i != j:
				licznik = np.polymul(licznik, c[j])
				mianownik *= (a[i] - a[j])
		q = np.polyadd(q, np.polymul(np.poly1d([b[i] / mianownik]), licznik))
	return q


def wypelnij(_n):
	a = np.array([], dtype=np.float64)
	b = np.array([], dtype=np.float64)
	c = []
	for i in range(_n):
		a = np.append(a, wezel(i, _n))
		b = np.append(b, funkcja(a[i]))
		c.append(np.poly1d([1, -a[i]], variable='x'))
	return a, b, c


def funkcja(a):
	if flaga_funkcji == 1:
		return 1 / (1 + 25 * a * a)
	return 1 / (1 + a * a)


def wezel(m, _n):
	if flaga_wezla == 1:
		return - 1 + 2 * m / _n
	return cos(pi * (2 * m + 1) / (2 * (_n + 1)))


# x - zbior wezlow interpolacji
# y - zbior wartosci funkcji w kolejnych wezlach interpolacji
# p - zbior pierwiastkow wielomianu (x-x_i)

x, y, p = wypelnij(n[0])
W0 = wielomian(x, y, p, n[0])
x, y, p = wypelnij(n[1])
W1 = wielomian(x, y, p, n[1])
x, y, p = wypelnij(n[2])
W2 = wielomian(x, y, p, n[2])
x, y, p = wypelnij(n[3])
W3 = wielomian(x, y, p, n[3])
x, y, p = wypelnij(n[4])
W4 = wielomian(x, y, p, n[4])

x = np.array([], dtype=np.float64)
for k in np.arange(-1, 1, 0.01):
	x = np.append(x, k)

mpl.ylim([0, 2])
mpl.plot(x, funkcja(x), label='y(x)')
mpl.plot(x, W0(x), label='W0(x)')
mpl.plot(x, W1(x), label='W1(x)')
mpl.plot(x, W2(x), label='W2(x)')
mpl.plot(x, W3(x), label='W3(x)')
mpl.plot(x, W4(x), label='W4(x)')
mpl.legend()
mpl.show()
