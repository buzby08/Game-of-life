There is an initial grid for the game, which is a 50x35 grid. 

Each cell on the grid can be in one of two states: **dead** or **alive**. Living cells are colored blue.

### Initialization:
Before initiating the game, you need to carefully select the cells to bring to life. Observe as your civilization thrives or perishes.

### Gameplay:
The fate of a cell is determined by its 8 immediate neighbors, including those at diagonal positions. 

- If a cell is alive and has 2 or 3 living neighbors, it remains alive.
- If a cell is alive and has more than 3 living neighbors, it dies due to overcrowding.
- If a cell is alive and has fewer than 2 neighbors, it dies due to loneliness.
- If a cell is dead and has exactly 3 neighbors, it becomes alive again.