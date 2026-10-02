import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def coucou():
    x = np.array([1, -1, -1, 1])
    y = np.array([1, 1, -1, -1])
    pts = np.array([x, y])
    step_duration = 0.01
    total_time = 10
    nb_steps = total_time / step_duration
    theta = 2.0 * np.pi / nb_steps
    cos_theta, sin_theta = np.cos(theta), np.sin(theta)
    mat = np.array([cos_theta, -sin_theta, sin_theta, cos_theta]).reshape(2, 2)
    fig = plt.figure(figsize=(5, 5))  # initialise la figure
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    sc = plt.scatter([], [])
    plt.grid(True, which="both")

    def animate(_):
        nonlocal pts
        pts = mat @ pts
        sc.set_offsets(pts.T)
        plt.pause(0.01)
        return (sc,)


    ani = animation.FuncAnimation(
        fig, animate, frames=100, interval=1, blit=True, repeat=True
    )
    plt.show()

coucou()


# mat est une matrice effectuant une rotation d'un angle theta (2pi/nb_steps)
# pts : coordonnées de 4 points
# l'animation va faire tourner les points en applicant la matrice nb_steps fois et donc au final un tour complet (2pi)  