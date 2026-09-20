from functools import reduce
from bdd import students

# On cherche l'âge du plus jeune étudiant
ageMini = reduce(lambda a, student : min(a, student['age']), students, students[0]['age'])

# On filtre le dictionnaire pour ne garder que les étudiants ayant cet age minilam
youngest = list(filter(lambda student : student['age'] == ageMini, students))[0]
print('Youngest student : ', youngest['name'], ', age ', youngest['age'])