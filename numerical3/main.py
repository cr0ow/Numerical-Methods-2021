import numpy as np


def det(m):
	_det = 1
	for j in range(len(m)):
		_det *= m[j][1]
	return _det


N = 100
a = [[0, 1.2, 0.1, 0.4]]
x = [1]

for i in range(2, N-1):
	a.append([0.2, 1.2, 0.1/i, 0.4/(i*i)])
	x.append(i)
a.append([0.2, 1.2, 0.1/(N-1), 0])
a.append([0.2, 1.2, 0, 0])
x.append(99)
x.append(100)

A = np.array(a, dtype=np.float64)
np.set_printoptions(suppress=True)

for i in range(1, N-1):
	A[i][0] = A[i][0] / A[i-1][1]  # L
	A[i][1] = A[i][1] - A[i][0]*A[i-1][2]  # U
	A[i][2] = A[i][2] - A[i][0]*A[i-1][3]  # U
A[99][0] = A[99][0] / A[98][1]
A[99][1] = A[99][1] - A[99][0]*A[98][2]

print('det(A) = ', det(A))

b = np.array([], dtype=np.float64)
b = np.append(b, x[0])
for i in range(1, 100):
	b = np.append(b, x[i] - A[i][0] * b[i-1])

y = np.array([], dtype=np.float64)
y = np.append(y, b[99] / A[99][1])
y = np.append(y, (b[98] - A[98][2] * y[0]) / A[98][1])
for i in range(97, -1, -1):
	y = np.append(y, (b[i] - A[i][3] * y[N-i-3] - A[i][2] * y[N-i-2]) / A[i][1])

y = y[::-1]
print('y = ', y)
