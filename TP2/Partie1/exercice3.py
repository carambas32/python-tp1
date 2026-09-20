def min_list(l):
    if len(l) == 0:
        raise ValueError("Impossible de calculer le min d'une liste vide")
    
    return min(l)

try:
    l = [ 1, 2, 3 ]
    print("min of", l, "is", min_list(l))

    l = []
    print("min of", l, "is", min_list(l))
except ValueError as e:
    print(e)