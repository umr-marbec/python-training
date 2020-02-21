import pylab as plt
import numpy as np
plt.rcParams['font.size'] = 15

nx, ny = 3, 4

x = np.arange(nx) + 0.5
y = np.arange(ny) + 0.5

plt.figure()
ax = plt.gca()
ax.set_aspect('equal')
ax.set_facecolor('lightgray')
ax.set_xticks(np.arange(nx + 1))
ax.set_yticks(np.arange(ny + 1))
plt.grid(linestyle='--')
plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax.get_yticklabels(), visible=False)
plt.xlim(0, nx)
plt.ylim(0, ny)

cpt = 0
for i in range(0, nx):
    for j in range(ny):
        plt.text(x[i], y[j], cpt, ha='center', va='center')
        cpt += 1

plt.savefig('corder.svg', bbox_inches='tight')
