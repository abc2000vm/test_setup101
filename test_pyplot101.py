# test pyplot #101
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 121)
y1, y2 = np.sin(x), np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.title("Pyplot Test 101")
plt.grid("on")

plt.show()
# let's try it now