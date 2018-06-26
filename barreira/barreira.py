from sympy import *

import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = Symbol('x')

y = x**2 + x*2

y_derivated = y.diff(x)
y_derivated

a = np.arange(0, 3, 0.001)
b = y_derivated

# Plot the points using matplotlib
plt.subplot(2, 1, 1)
plt.plot(a, b)
plt.show()  # You must call plt.show() to make graphics appear.
