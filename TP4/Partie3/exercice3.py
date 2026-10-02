import numpy as np
import matplotlib.pyplot as plt

# 1
values = [1, 2, 3, 4, 5]
distrib = [0.2, 0.1, 0.2, 0.4, 0.1]
x0 = np.random.choice(values, 1000, p=distrib)

# 2
print(x0)
print(np.histogram(x0, bins=[1, 2, 3, 4, 5, 6]))
# plt.figure(figsize=(6, 10))
plt.hist(x0, bins=[1, 2, 3, 4, 5, 6])
plt.show()
