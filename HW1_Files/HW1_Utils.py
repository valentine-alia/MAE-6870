import numpy as np
import matplotlib.pyplot as plt
def plot_occupancy(grid, title="Occupancy Grid (0 = free, 1 = occupied)"):
    fig, ax = plt.subplots(figsize=(6, 6))
    im = ax.imshow(grid, origin='lower', interpolation='none', cmap='binary', vmin=0, vmax=1)
    ax.set_title(title)
    ax.set_xlabel('Column index')
    ax.set_ylabel('Row index')
    ax.set_xticks(np.arange(0, grid.shape[1], 1))
    ax.set_yticks(np.arange(0, grid.shape[0], 1))
    # Draw gridlines at cell boundaries
    ax.set_xticks(np.arange(-0.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, grid.shape[0], 1), minor=True)
    ax.grid(which='minor', linestyle='-', linewidth=0.5)
    ax.tick_params(axis='both', which='both', length=0)
    plt.show()