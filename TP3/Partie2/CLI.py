import click

@click.group()
def cli():
    """Simple CLI avec plusieurs commandes."""
    pass

@click.command()
@click.argument("name")
@click.option("--count", default=1, help = "Nombre de répétitions")
def hello(name, count):
    """Dit bonjour à quelqu'un"""
    for i in range(count):
        print("Bonjour " + name + " !")

@click.command()
@click.argument("name")
def goodbye(name):
    """Dit au revoir à quelqu'un"""
    print("Au revoir " + name + " !")

cli.add_command(hello)
cli.add_command(goodbye)

if __name__ == "__main__":
    cli()
    
    
    
# (.venv) PS C:\Prog\python\TP_EFREI\TP3\Partie2> python .\CLI.py
# Usage: CLI.py [OPTIONS] COMMAND [ARGS]...

#   Simple CLI avec plusieurs commandes.

# Options:
#   --help  Show this message and exit.

# Commands:
#   goodbye  Dit au revoir à quelqu'un
#   hello    Dit bonjour à quelqu'un

# (.venv) PS C:\Prog\python\TP_EFREI\TP3\Partie2> python .\CLI.py hello Bob
# Bonjour Bob !


