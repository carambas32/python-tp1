from bdd import students
from functools import reduce

# Calculate mean grade
gradesSum = reduce(lambda a, x : a + x['grade'], students, 0)
mean = gradesSum / len(students)
print(f"Moyenne des notes : {mean}")

# Filter, get names and sort
aboveMeanStudents = list(filter(lambda x : x['grade'] > mean, students))
aboveMeanStudentsNames = list(map(lambda x : x['name'], aboveMeanStudents))
print(sorted(aboveMeanStudentsNames))
