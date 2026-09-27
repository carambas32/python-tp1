import click
import os


@click.group()
def cli():
    """Python File Manager"""
    pass


@click.command()
@click.argument("file")
def cat(file):
    """affiche le contenu de file dans la console"""
    if not os.path.exists(file):
        print(f"Le fichier {file} n'existe pas")
        exit(1)

    if not os.path.isfile(file):
        print(f"{file} n'est pas un fichier")
        exit(1)

    with open(file, 'r') as f:
        print(''.join(f.readlines()))


@click.command()
@click.argument("dir")
@click.option("--ext", default='', help="Filtre sur le type d'exention")
def listfiles(dir, ext):
    """liste les noms des fichiers présents dans le dossier dir"""
    if not os.path.exists(dir):
        print(f"Le dossier {dir} n'existe pas")
        exit(1)

    if not os.path.isdir(dir):
        print(f"{dir} n'est pas un dossier")
        exit(1)

    filelist = os.listdir(dir)
    
    if ext != '':
        filelist = list(filter(lambda f: f.endswith(f".{ext}"), filelist))
        
    print("\n".join(filelist))


def search_aux(filename, path):
    filelist = os.listdir(path)
    
    for file in filelist:
        fullname = f"{path}/{file}"
        
        if os.path.isdir(fullname):
            search_aux(filename, fullname)
            
        if file.endswith(filename):
            print(os.path.join(path, filename))

@click.command()
@click.argument("filename")
def search(filename):
    path = os.path.dirname(filename)
    name = os.path.basename(filename)
    search_aux(name, path)


cli.add_command(cat)
cli.add_command(listfiles)
cli.add_command(search)

if __name__ == "__main__":
    cli()


# (.venv) PS C:\Prog\python\TP_EFREI\TP3\Partie2> python .\file_manager.py listfiles ../Partie1 --ext=zip
# backup_2026-09-26.zip
# backup_2026-09-26.zip.zip

# (.venv) PS C:\Prog\python\TP_EFREI\TP3\Partie2> python.exe .\file_manager.py search ../../data.csv
# ../../TP3/Partie1\data.csv