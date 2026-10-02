import numpy as np

t = np.array([1, 2, 3, 4, 5])
for i in range(len(t)):
    print(t[i])

for x in t:
    print(x)

print(t[2:4])
# array([3, 4])
print(t[[True, True, False, False, True]])
# array([1, 2, 5])
print(t[t > 2])
# array([2, 4])


#Pandas