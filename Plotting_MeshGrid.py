import numpy as np

import matplotlib.pyplot as plt

points = np.arange(-5,0,0.01)

dx,dy = np.meshgrid(points,points)

# print(dx)
# print()
# print(dy)
z = (np.sin(dx) + np.sin(dy))
#print(z)
print(plt.imshow(z))

plt.imshow(z)
plt.colorbar()

plt.title('Plot for sin(x) + sin(y)')
