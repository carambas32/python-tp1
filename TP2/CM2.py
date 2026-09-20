# print(3)
# print(2.56)
# print("abc")
# print(True)
# a = 26
# b = False
# print("a =", a, ", b =", b)

# print("\" \\ \"")

# print("a = ", a, ", b = ", b, sep = "")
      
# s = input("Saisissez une entrée : ")
# print("Vous avez saisi \"", s, "\".", sep = "")

# try:
#     a = int(input("Saisissez un entier : "))
#     print("La valeur de a est :", a)
# except ValueError:
#     print("Mauvaise saisie")
    
    
    
# try:
#     # Bloc de code
#     a = int(input("Saisissez un entier : "))
#     print(a) # Erreur : b n’existe pas
# except NameError:
#     print("Mauvaise variable")
# except ValueError:
#     print("Mauvaise valeur")
# except:
#     print("Une autre erreur est survenue")
# else:
#     print("Aucune erreur n'a eu lieu")
# finally:
#     print("Fin du programme")    


# def print_inverse(x):
#     if x == 0:
#         raise ValueError("print_inverse: argument cannot be zero")
    
#     print(1 / x)
#     # ...
    
# try:
#     for i in range(3):
#         print_inverse(i)
# # Le type Exception englobe toutes les exceptions
# except Exception as e:
#     print(e)
    
    
# Fonctions lambda
# f = lambda x : x * x
# print("f(2) =", f(2), "; f(3)", f(3))

# students = [("Alice", 25), ("Eve", 22), ("Bob", 28)]
# sorted_default = sorted(students)
# print("Tri par défaut :", sorted_default)

# sorted_students = sorted(students, key = lambda x : x[1])
# print("Tri par âge : ", sorted_students)



# L = [ 3, 4, 5, 6 ]
# L_squared = list(map(lambda x : x * x, L))
# print(L_squared)
# # L_squared == [9, 16, 25, 36]

# L_cubed = list(map(lambda x : x ** 3, L))
# print(L_cubed)
# # L_cubed == [ 27, 64, 125, 216 ]

# # Alternative :
# L_squared2 = [ x * x for x in L ]
# print(L_squared2)


# words = [ "abc", "def", "ghi" ]
# words_uppercase = list(map(lambda s : s.upper(), words))
# print(words_uppercase)
# # words_uppercase == ['ABC', 'DEF', 'GHI']

# etudiants = [ ("Aurore", 25), ( "Bastien", 17), ("David", 21), ("Emilie", 16) ]
# # Noms en majuscule des étudiants majeurs
# etudiants_majeurs = list(filter(lambda x : x[1] >= 18, etudiants))
# print(etudiants_majeurs)
# noms_etudiants_majeurs = list(map(lambda x : x[0].upper(), etudiants_majeurs))
# print(noms_etudiants_majeurs)
# # [ 'AURORE', 'DAVID' ]


# def f(x : int):
#     return x + 1

# a = f(3)
# b = f("abc")
# c = f("toto")
# print(a, b)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello! I am ", self.name, "!", sep = "")

p = Person("Bob", 31)
p.hello()
print(p.name, "is", p.age, "years old.")