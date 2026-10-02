import numpy as np
import sys
import math

# 1
x = np.array([1, 0, 0, 0, 0])
print(x)
# [1 0 0 0 0]

print(x.tolist())
[1, 0, 0, 0, 0]

# 2 np.zeros, np.ones, np.full
tableau_zeros = np.zeros(5)
tableau_ones = np.ones(5)
tableau_fours = np.full(5, 4.0)

print(tableau_zeros)
print(tableau_ones)
print(tableau_fours)
# [0. 0. 0. 0. 0.]
# [1. 1. 1. 1. 1.]
# [4. 4. 4. 4. 4.]


# 3 np.any et np.all
print(
    np.any(x),  # True
    np.any(tableau_zeros),
    np.any(tableau_ones),
    np.any(tableau_ones),
)
print(
    np.all(x),  # False
    np.all(tableau_zeros),
    np.all(tableau_ones),
    np.all(tableau_ones),
)

# True False True True
# False False True True
# any fait un ou logique sur l'ensemble des éléments de la liste
# all fait un et logique sur l'ensemble des éléments de la liste

# 4
x = np.array([1.0, 0.0, np.nan, np.nan, 2.0, 4.0, np.inf])
finished_mask = np.isfinite(x)
print(finished_mask)  # [ True  True False False  True  True False]

def containsInfinite(x):
    return np.any(np.isinf(x))

print(
    containsInfinite(x),
    containsInfinite([0, 1]),
    containsInfinite([np.inf, 1]),
    containsInfinite([np.inf, np.nan]),
    containsInfinite([np.inf, np.inf]),
)

# 5
print("Eléments finis de x", x[finished_mask])
numbers_mask = list(map(lambda val: not np.isnan(val), x))
print("Eléments non nan de x", x[numbers_mask])

# 6
x = np.array([1, 3, 6, 2, 8, 9, 4, 5, 7])
print("nombre d'élements de x : ", len(x))
print("taille de chaque élément de x : ", list(map(lambda elt: sys.getsizeof(elt), x)))
print("taille de x : ", sys.getsizeof(x)) # 184 < 288 (9 * 32)

# 7
print(x.shape)  # (9,)

# 8
nb_columns = int(math.sqrt(len(x)))
print('Reshaping x in square matrix\n', x.reshape(nb_columns, nb_columns))
