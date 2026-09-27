import os, shutil, datetime, stat

dir_path = os.path.dirname(os.path.realpath(__file__))
projectDir = dir_path + '/project'
backupDir = dir_path + '/backup/project'

if (not os.path.exists(projectDir)):
    os.mkdir(projectDir)

if (not os.path.exists(f"{projectDir}/include")):
    os.mkdir(f"{projectDir}/include")

with open(f"{projectDir}/include/utils.h", "w") as f:
    f.write("// header file")

if (not os.path.exists(f"{projectDir}/src")):
    os.mkdir(f"{projectDir}/src")

with open(f"{projectDir}/src/main.c", "w") as f:
    f.write("// c file")

with open(f"{projectDir}/src/utils.c", "w") as f:
    f.write("// another c file")

shutil.copytree(projectDir, backupDir, dirs_exist_ok=True)

output_file_name = dir_path + '/backup_' + str(datetime.date.today()) + '.zip'
print(output_file_name)
shutil.make_archive(output_file_name, "zip", backupDir)

shutil.rmtree(backupDir)

def displayRights():
    print(
        f"Permissions du fichier d'archive {output_file_name} : ",
        oct(stat.S_IMODE(os.stat(output_file_name).st_mode)),
    )
    
def changeRight():
    os.chmod(output_file_name, 0o775)
    
displayRights()
changeRight()
displayRights()
