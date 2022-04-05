import numpy as np
import math

N = 64
index_of_w = N-3

u_f = np.identity(N)
u_f[index_of_w, index_of_w] = -1

bra_s = np.matrix([[1/math.sqrt(N)] * N])
ket_s = bra_s.T

u_s = 2 * np.matmul(ket_s, bra_s) - np.identity(N)
r = int(round(math.sqrt(N))) - 2

print(np.matmul(np.linalg.matrix_power(np.matmul(u_s, u_f), r), ket_s))
