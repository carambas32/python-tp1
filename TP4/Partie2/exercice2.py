import numpy as np
import pandas as pd
import time

np.random.seed(0)

# 1
myarray = []

for i in range (1_000_000):
    myarray.append(np.random.randint(1, 100))


# 2
mydf = pd.DataFrame({"Values": myarray})

# 3
timeDebut = time.time()
somme = 0

for val in mydf["Values"]:
    somme += val

time_loop = time.time() - timeDebut
print("Somme = ", somme, " calculé en ", round(time_loop * 1000, 2), "ms")

# 4
timeDebut = time.time()

somme = mydf["Values"].sum()

time_method = time.time() - timeDebut
print("Somme = ", somme, " calculé en ", round(time_method * 1000, 2), "ms")

# 5
print("Rapport de durée entre les deux méthodes = ", time_loop / time_method)
