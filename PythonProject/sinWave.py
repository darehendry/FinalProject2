import matplotlib.pyplot as plt
import numpy as np

# Generate 100 linearly spaced numbers between -π and π
x = np.linspace(-np.pi, np.pi, 100)
# Compute the sine of each x value
y = np.sin(x)

plt.plot(x, y)

plt.legend()
plt.xlabel('x values')
plt.ylabel('sin(x)')
plt.show()