import numpy as np
import matplotlib.pyplot as plt

items = ["Pommes", "Poires", "Bananes", "Citron"]
ventes = [25.5, 32.8, 21.4, 10.3]
plt.barh(items, ventes)
plt.ylabel("Items")
plt.xlabel("Ventes (en euros)")
index_max = ventes.index(max(ventes))
article_le_plus_vendu = items[index_max]
plt.title(
    f"Les {article_le_plus_vendu} " f"sont les fruits les plus vendus", fontsize=12
)
avg_sale = np.mean(ventes)
plt.axvline(float(avg_sale), color="r", label="moyenne")
plt.legend()
plt.show()


x = np.arange(0, 8)
y = np.array([2, 4, 5, 6, 7.5, 3, 1, 0.5])
plt.plot(x, y)
plt.show()

n = 1000
r = np.sqrt(np.random.random_sample((n,)))
theta = 2.0 * np.pi * np.random.random_sample((n,))
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(5, 5))
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.scatter(x, y)
circle = plt.Circle((0, 0), 1, color="r", fill=False)
plt.gca().add_patch(circle)
plt.show()
