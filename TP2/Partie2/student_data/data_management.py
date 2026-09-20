from functools import reduce
from .database import students


def exercice1():
    # On cherche l'âge du plus jeune étudiant
    ageMini = reduce(
        lambda a, student: min(a, student["age"]), students, students[0]["age"]
    )

    # On filtre le dictionnaire pour ne garder que les étudiants ayant cet age minilam
    youngest = list(filter(lambda student: student["age"] == ageMini, students))[0]
    print("Youngest student : ", youngest["name"], ", age ", youngest["age"])


def exercice2():
    names = list(map(lambda x: x["name"], students))
    print(sorted(names))


def exercice3():
    def extract(students: list, dept: str):
        result = list(filter(lambda x: x["department"] == dept, students))

        if len(result) == 0:
            raise Exception(f'Department "{dept}" not found in database')

        return result

    print(extract(students, "Math"))


def exercice4():
    # Calculate mean grade
    gradesSum = reduce(lambda a, x: a + x["grade"], students, 0)
    mean = gradesSum / len(students)
    print(f"Moyenne des notes : {mean}")

    # Filter, get names and sort
    aboveMeanStudents = list(filter(lambda x: x["grade"] > mean, students))
    aboveMeanStudentsNames = list(map(lambda x: x["name"], aboveMeanStudents))
    print(sorted(aboveMeanStudentsNames))


def exercice5():
    # Put students in departments dictionnary with dept name as key
    departments = {}
    for student in students:
        deptName = student["department"]
        if deptName not in departments.keys():
            departments[deptName] = []

        departments[deptName].append(student)

    # For each department sort students
    for name, dptStudents in departments.items():
        departments[name] = sorted(dptStudents, key=lambda x: x["grade"], reverse=True)

        # then keep only student names
        departments[name] = list(map(lambda x: x["name"], departments[name]))

    print("Classement :")
    for dptName in departments:
        print(dptName, " : ", departments[dptName])


def exercice7():
    def compareStudentsAge(s1, s2):
        if s1["age"] < s2["age"]:
            return s1
        return s2

    youngest = reduce(
        compareStudentsAge,
        students,
        students[0],
    )
    print("Youngest student : ", youngest["name"], ", age ", youngest["age"])
