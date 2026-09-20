from bdd import students

names = list(map(lambda x : x['name'], students))
print(sorted(names))