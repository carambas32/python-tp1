import pandas as pd
import matplotlib.pyplot as plt

# 1
data = pd.read_csv("TP4/Partie3/data.csv")
print(data.head(5))

# 2
_, (pl0, pl1) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

pl0.scatter(data["Longueur Sépale"], data["Largeur Sépale"], color='b')
pl0.set_xlabel("Longueur Sépale")
pl0.set_ylabel("Largeur Sépale")

pl1.scatter(data["Longueur Pétale"], data["Largeur Pétale"], color='r')
pl1.set_xlabel("Longueur Pétale")
pl1.set_ylabel("Largeur Pétale")

plt.show()

# 3
_, (pl0, pl1) = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

especes = list(data["Espèce"].unique())
masks = list(map(lambda e: list(data["Espèce"] == e), especes))

pl0.set_xlabel("Longueur Sépale")
pl0.set_ylabel("Largeur Sépale")

pl1.set_xlabel("Longueur Pétale")
pl1.set_ylabel("Largeur Pétale")

for i in range(len(especes)):
    pl0.scatter(
        data.loc[masks[i]]["Longueur Sépale"],
        data.loc[masks[i]]["Largeur Sépale"],
        label=especes[i]
    )
    pl1.scatter(
        data.loc[masks[i]]["Longueur Pétale"],
        data.loc[masks[i]]["Largeur Pétale"],
        label=especes[i]
    )

pl0.legend(loc="lower right")
pl1.legend(loc="lower right")

plt.show()
