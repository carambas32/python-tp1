import numpy as np
import math

# 1
theta = math.pi / 4
mat = np.array(
    [[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]]
)

print(mat)

# 2
v = np.array([2, 0])
v2 = mat @ v
print('v2 = mat @ v = ', np.round(v2, 5))

# 3
v3 = mat @ v2  # Arrondi pour un meilleur affichage
print("v3 = mat @ v2 = ", np.round(v3, 5)) # [0, -2] la matrice effectue une rotation d'un angle de -pi/4

# 4
mat2 = mat @ mat
print('mat2 = mat @ mat = ', np.round(mat2, 5))
# [[ 0.  1.]
#  [-1. -0.]]

mH = mat * mat
print("mH = mat * mat = ", np.round(mH, 5))
#  [[0.5 0.5]
#  [0.5 0.5]]

# 5
print(np.round(v @ v2, 5)) # 2,8...
print(np.round(v @ v3, 5)) # 0 car les deux vecteurs sont orthogonaux et c'est normal vu que v3 = rotation de 2 * pi/4 soit pi/2
