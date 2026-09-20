from functools import reduce
from bdd import students

def exercice7():
    youngest = reduce(
        lambda s1, s2: s1 if s1['age'] < s2['age'] else s2,
        students,
        students[0],
    )
    print("Youngest student : ", youngest["name"], ", age ", youngest["age"])
    
exercice7()