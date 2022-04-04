import numpy as np
import matplotlib.pyplot as mpl
from math import log10
from random import randint

N = 100


def norma(u, v):
	suma = 0
	for k in range(N):
		suma += pow(u[k] - v[k], 2)
	return pow(suma, 1/2)


def wektor():
	p = []
	for g in range(N):
		p.append(randint(0, 100))
	return p


a = [[0, 0, 3, 1, 0.2], [0, 1, 3, 1, 0.2]]
b = np.array([], dtype=np.float64)
for i in range(1, N-1):
	a.append([0.2, 1, 3, 1, 0.2])
	b = np.append(b, i)
a.append([0.2, 1, 3, 1, 0])
b = np.append(b, 99)
b = np.append(b, 100)
A = np.array(a, dtype=np.float64)

# metoda Jacobiego ---------------------------------------
o = wektor()
x = np.array(o, dtype=np.float64)
y = np.array(x, dtype=np.float64)
wynik = np.array([], dtype=np.float64)
iteracje = []
it = 0
#
while norma(y, x) > pow(10, -12) or len(iteracje) == 0:
	it += 1
	y = np.array(x, dtype=np.float64)
	for i in range(N-2):
		val = b[i]
		for j in range(-2, 3):
			if j != 0:
				val -= A[i][j+2] * y[i+j]
		x[i] = val / A[i][2]
	x[N-2] = (b[N-2] - A[N-2][0]*y[N-4] - A[N-2][1]*y[N-3] - A[N-2][3]*y[N-1]) / A[N-2][2]
	x[N-1] = (b[N-1] - A[N-1][0]*y[N-3] - A[N-1][1]*y[N-2]) / A[N-1][2]
	iteracje.append(it)
	wynik = np.append(wynik, log10(norma(x, y)))
mpl.plot(iteracje, wynik, label='Jacobi')
print(x)
# -------------------------------------------------------------


# metoda Gaussa-Seidela ------------------------------------
x = np.array(o, dtype=np.float64)
y = np.array(x, dtype=np.float64)
wynik = np.array([], dtype=np.float64)
iteracje = []
it = 0

while norma(y, x) > pow(10, -12) or len(iteracje) == 0:
	it += 1
	y = np.array(x, dtype=np.float64)
	for i in range(N-2):
		val = b[i]
		for j in range(-2, 3):
			if j > 0:
				val -= A[i][j+2] * y[i+j]
			if j < 0:
				val -= A[i][j + 2] * x[i + j]
		x[i] = val / A[i][2]
	x[N-2] = (b[N-2] - A[N-2][0]*y[N-4] - A[N-2][1]*y[N-3] - A[N-2][3]*y[N-1]) / A[N-2][2]
	x[N-1] = (b[N-1] - A[N-1][0]*y[N-3] - A[N-1][1]*y[N-2]) / A[N-1][2]
	iteracje.append(it)
	wynik = np.append(wynik, log10(norma(x, y)))
mpl.plot(iteracje, wynik, label='Gauss-Seidel')
print(x)
# -------------------------------------------------------------

mpl.xlabel('numer iteracji')
mpl.ylabel('log10(||x(n) - x(n-1)||)')
mpl.legend()
mpl.show()
