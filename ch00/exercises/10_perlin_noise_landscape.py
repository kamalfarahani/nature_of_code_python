import time

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from noise import snoise3


def main():
    def update(frame: int) -> None:
        ax.cla()
        nonlocal z
        for i in range(len(x)):
            for j in range(len(y)):
                z[i, j] = snoise3(x[i, j], y[i, j], frame * 0.01)

        surf = ax.plot_surface(x, y, z, cmap="viridis")

    # Define the grid of x and y values
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    x, y = np.meshgrid(x, y)

    z = np.zeros_like(x)
    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = snoise3(x[i, j], y[i, j], 0)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surf = ax.plot_surface(x, y, z, cmap="viridis")
    ax.view_init(elev=30, azim=30)

    ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=1)
    plt.show()


if __name__ == "__main__":
    main()
