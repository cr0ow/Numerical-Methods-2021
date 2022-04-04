import numpy as np

N = 50

z1 = np.array([5/9], dtype=np.float64)
z2 = np.array([1/9], dtype=np.float64)

for i in range(N-2, -1, -1):
	z1 = np.append(z1, (5 - 7 * z1[N-i-2]) / 9)
	z2 = np.append(z2, (1 - 7 * z2[N-i-2]) / 9)

z1 = z1[::-1]
z2 = z2[::-1]

licznik = np.array([], dtype=np.float64)
mianownik = 1
items = np.array([], dtype=np.float64)

for j in range(N):
	item = 0
	for i in range(N):
		item += z2[j]*z1[i]
	items = np.append(items, item)
	mianownik += z2[j]

for i in range(N):
	licznik = np.append(licznik, items[i])

x = np.array([], dtype=np.float64)
y = np.array([], dtype=np.float64)

for i in range(N):
	x = np.append(x, licznik[i] / mianownik)
	y = np.append(y, z1[i] - x[i])


print("y =", y)
