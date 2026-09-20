from bdd import students

# Put students in departments dictionnary with dept name as key
departments = {}
for student in students:
    deptName = student['department']
    if deptName not in departments.keys():
        departments[deptName] = []
        
    departments[deptName].append(student)


# For each department sort students
for (name, dptStudents) in departments.items():
    departments[name] = sorted(dptStudents, key = lambda x : x['grade'], reverse = True)
    
    # then keep only student names
    departments[name] = list(map(lambda x : x['name'], departments[name]))
    
print('Classement :')
for dptName in departments:
    print(dptName, ' : ', departments[dptName])