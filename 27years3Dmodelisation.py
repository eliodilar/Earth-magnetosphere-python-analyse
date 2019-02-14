# -*-coding:Latin-1 -*

import os 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x1 = np.array([
0.8571,
1.7142,
2.5713,
3.4284,
4.2855,
5.1426,
5.9997,
6.8568,
7.7139,
8.571,
9.4281,
10.2852,
11.1423,
11.9994,
12.8565,
13.7136,
14.5707,
15.4278,
16.2849,
17.142,
17.9991,
18.8562,
19.7133,
20.5704,
21.4275,
22.2846,
23.1417,
23.9988
])

X = np.array([20878.30, 20900.70, 20909.30, 20932.10, 20934.00, 20988.70, 20957.30, 20955.70, 20964.40,
 20974.00, 21000.20, 21018.80, 21026.30, 20970.30, 21047.00, 21078.20, 21089.20, 21114.30, 21118.50, 21138.10,
 21146.00, 21161.30, 21175.00, 21191.70, 21196.30, 21222.99, 21237.66, 21235.24])

Y = np.array([-174.50, -1026.00, -981.50, -936.10, -891.30, -879.40, -796.20, -746.50, -686.70,
 -643.50, -602.30, -557.10, -508.70, -458.00, -414.80, -379.10, -329.00, -286.70, -226.90,-175.20,
 -118.70, -63.90,  35.90, 43.90, 100.50, 155.89, 215.35, 295.81])

Z = np.array([42341.00, 42326.20, 42343.30, 42356.60, 42375.10, 42384.80, 42419.70, 42466.60, 42479.80,
 42517.70, 42539.70, 42573.90, 42614.20, 42654.30, 42669.50, 42682.30, 42701.40, 42720.60, 42743.20,
 42764.00, 42786.80, 42808.00, 42826.30, 42849.00, 42886.20, 42904.47, 42939.93, 42981.81])

X.shape
Y.shape
Z.shape



n_radii = 8
n_angles = 36

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)

# Repeat all angles for each radius.
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z to make the pringle surface.
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(X, Y, Z, linewidth=0.1, antialiased=True)

plt.legend(loc='upper left')
plt.show()


plt.show()
os.system("pause")