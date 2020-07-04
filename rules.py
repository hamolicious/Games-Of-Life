from random import randint

def generate_grid(fill=50):
    resolution = 50
    grid = []
    for y in range(resolution):
        temp = []
        for x in range(resolution):

            if x in [0, resolution-1] or y in [0, resolution-1]:
                state = False
            else:
                if randint(0, 100) <= fill:
                    state = True
                else:
                    state = False

            temp.append(state)

        grid.append(temp)
    return grid

def ConwaysGameOfLifeRule(current, num_neighbours):
    """
    Any live cell with fewer than two live neighbours dies
    Any live cell with two or three live neighbours lives
    Any live cell with more than three live neighbours dies
    Any dead cell with exactly three live neighbours becomes a live cell
    """
    if current == True:
        if num_neighbours < 2:
            return False
        if num_neighbours == 2 or num_neighbours == 3:
            return True
        if num_neighbours > 3:
            return False

    else:
        if num_neighbours == 3:
            return True

def run_single_step(grid, rule=ConwaysGameOfLifeRule):
    temp = generate_grid(0)
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            state = grid[y][x]
            n = [
                bool(grid[y-1][x  ]),
                bool(grid[y+1][x  ]),
                bool(grid[y  ][x-1]),
                bool(grid[y  ][x+1]),
                bool(grid[y-1][x-1]),
                bool(grid[y+1][x+1]),
                bool(grid[y-1][x+1]),
                bool(grid[y+1][x-1])
            ]

            temp[y][x] = rule(state, n.count(True))

    return temp





