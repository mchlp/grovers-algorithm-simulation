"""
grovers.py

Given an input list size N and index of the winning item w, simulate
Grover's algorithm to find the winning item and plot the probability amplitudes
periodically
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import math

N = input("Enter number of items N: ")
N = int(N)
index_of_w = input("Enter index of winning item w: ")
index_of_w = int(index_of_w) - 1

# Oracle function matrix
u_f = np.identity(N)
u_f[index_of_w, index_of_w] = -1

# Diffuser
bra_s = np.matrix([[1/math.sqrt(N)] * N])
ket_s = bra_s.T
u_s = 2 * np.matmul(ket_s, bra_s) - np.identity(N)

r = int(round(math.sqrt(N)))

result = ket_s

probability_amplitudes = [i[0] for i in result.tolist()]

fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111)
ax.set_ylabel('Probability amplitude')
ax.set_yticks(np.arange(0, 1, 0.1))
ax.set_ylim(0, 1)

bars = plt.bar([i for i in range(1, N+1)], probability_amplitudes)
results = [probability_amplitudes]
for i in range(r):
    result = np.matmul(np.matmul(u_s, u_f), result)
    old_max_probability_amplitude = max(results[-1])
    probability_amplitudes = [i[0] for i in result.tolist()]
    # Only add new probability amplitudes if new maximum is greater than old maximum
    if (max(probability_amplitudes) > old_max_probability_amplitude):
        results.append(probability_amplitudes)

"""
Get ith probability_amplitudes data
"""
def get_result(i):
    return results[i]

"""
Plot bar graph of quantum state vector
"""
def plot_quantum_state(i):
    probability_amplitudes = get_result(i)
    for j, b in enumerate(bars):
        b.set_height(probability_amplitudes[j])

ax.set_title(f"Probability amplitudes (N={N}, r={len(results)})")
anim = animation.FuncAnimation(
    fig,
    plot_quantum_state,
    repeat=True,
    blit=False,
    frames=len(results),
    interval=2000
)
plt.show()
