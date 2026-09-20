def sum_inverse(l):
    total = 0
    
    for v in l:
        if v == 0:
            raise ValueError("sum_inverse : impossible de calculer l'inverse de 0")
        
        try:
            total += 1/v
        except:
            raise TypeError(f"sum_inverse : la valeur {v} n'est pas un entier")
    
    return total


listes = [
    list(range(10)),
    list(range(1, 11)),
    [ 'abc', 'def' ]
]

for l in listes:
    try:
        print(l, "->", sep=' ', end=' ')
        print(sum_inverse(l))
    except Exception as e:
        print(e)
    
