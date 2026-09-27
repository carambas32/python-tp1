import os
import math
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
csvFilename = f"{dir_path}/data.csv"

def write_csv():
    with open(csvFilename, "w") as f:
        f.write("Sample number,x,cos(x),sin(x)\n")

        for x in range(0, int((2 * math.pi) * 100) + 1):
            y = x / 100
            f.write(f"{x},{y},{math.cos(y)},{math.sin(y)}\n")

def parse_csv():
    x = []
    cos = []
    sin = []

    with open(csvFilename, 'r') as f:
        # On saute la première ligne qui correspond au nom des colonnes
        line = f.readline()
        eof = False

        while not eof:
            line = f.readline()
            try:
                [number, cosx, sinx] = line.split(',')[1:4]
                x.append(float(number))
                cos.append(float(cosx))
                sin.append(float(sinx))
            except:
                eof = True

    return(x, cos, sin)

def displayGraph(x, y1, y2):
    plt.plot(x, y1, 'r', x, y2, 'b')
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.axis((0, 2 * math.pi + 0.2, -1.2, 1.2))
    plt.show()

write_csv()
(x, cos, sin) = parse_csv()
displayGraph(x, cos, sin)
