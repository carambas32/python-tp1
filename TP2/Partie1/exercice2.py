def inputInt(label : str):
    result = None
    while (result == None):
        try:
            result = int(input(label))
        except ValueError:
            print('Erreur : saisissez un entier')
            
    return result
    
n = inputInt("Saisir le nombre de valeurs attendues : ")

l = []
for i in range(n):
    l.append(int(inputInt("Saisir la valeur n°{} : ".format(i + 1))))
    
print("Valeurs saisies : ", l)
print("Maximum des valeurs saisie : ", max(l))