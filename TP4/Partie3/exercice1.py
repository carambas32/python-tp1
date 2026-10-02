import numpy as np
import matplotlib.pyplot as plt

# 1
x = np.linspace(-10, 10, 20)
print(x)

# 2
y = x**3
y2 = abs(x**3) + 100

# 3
plt.plot(x, y, x, y2)
plt.show()

# 4
plt.figure(figsize=(10,5))
plt.grid(True, which="both")
plt.plot(x, y, color='black', marker='D', label='x^3')
plt.plot(x, y2, "r--", label="|x|^3 + 100")
plt.legend()
plt.show()
