import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


grid_size = 100
initial_state = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])

def update(grid):
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            neighbors = np.sum(grid[max(0, i-1):min(grid_size, i+2), max(0, j-1):min(grid_size, j+2)]) - grid[i, j]
            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1
    return new_grid

def animate(frame):
    im.set_array(animate.grid)
    animate.grid = update(animate.grid)

fig, ax = plt.subplots()
animate.grid = initial_state

im = ax.imshow(animate.grid, cmap='binary')

ani = animation.FuncAnimation(fig, animate, frames=100, interval=200, blit=False)

plt.show()