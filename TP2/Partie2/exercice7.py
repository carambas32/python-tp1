from functools import reduce
from bdd import students

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
    
exercice7()