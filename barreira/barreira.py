import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.5)
y = np.sin(x)

a = np.arange(0, 3 * np.pi, 0.001)
b = np.cos(a)

plt.subplot(2, 1, 1)
# Plot the points using matplotlib
plt.plot(x, y)
plt.subplot(2, 1, 2)
plt.plot(a, b)
plt.show()  # You must call plt.show() to make graphics appear.
