from bdd import students

def extract(students : list, dept: str):
    result = list(filter(lambda x : x['department'] == dept, students))
    
    if len(result) == 0:
        raise Exception(f'Department "{dept}" not found in database')
    
    return result

print(extract(students, "Math"))