import pandas as pd
import math

students = pd.DataFrame(
    {
        "id_etudiant": [4271, 1083, 8902, 5146, 7639, 3258, 9471, 6014, 2897, 4835],
        "nom": [
            "Dupont",
            "Benali",
            "Nguyen",
            "Moreau",
            "Silva",
            "Bernard",
            "Hassani",
            "Leroy",
            "Okafor",
            "Fontaine",
        ],
        "prénom": [
            "Alice",
            "Karim",
            "Linh",
            "Julien",
            "Beatriz",
            "Marine",
            "Yanis",
            "Thomas",
            "Ada",
            "Nicolas",
        ],
        "date_naissance": [
            "2004-03-12",
            "2003-11-05",
            "2004-06-23",
            "2003-01-30",
            "2005-09-17",
            "2004-04-08",
            "2003-12-25",
            "2005-02-14",
            "2004-08-02",
            "2003-07-19",
        ],
        "option": ["CS", "DEV", "CS", "DEV", "CS", "CS", "DEV", "DEV", "CS", "CS"],
        "classe": ["B1", "B2", "B3", "B2", "B1", "B3", "B2", "B1", "B3", "B2"],
        "moyenne": [15.5, 12.0, 17.25, 9.5, 18.0, 14.0, 11.5, 13.75, 16.0, 10.25],
    }
)

# 1 noms de colonnes
print(list(students.columns.values))

# 2
print(students.loc[students["id_etudiant"] == 6014])

# 3
# print(students)
students.set_index("id_etudiant", inplace=True)
# print(students)

print(students.loc[6014, ["nom", "prénom"]])  # Index = id_etudiant

# 4 tri par date de naissance croissant
students.sort_values(by="date_naissance", inplace=True)
print(students)

# 5
options = students["option"]
print('\n', options) # options est un dataframe
print('liste des options', list(options.unique())) # type list

# 6
etudiants_cs = students.loc[students["option"] == "CS"]
print(etudiants_cs)
print(round(etudiants_cs["moyenne"].mean(), 2)) # Moyanne de la colonne moyenne des étudiants avec l'option CS

# 7
print(students.groupby(by="option")["moyenne"].mean())