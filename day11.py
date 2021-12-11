import copy

from shared import get_lines_from_file

MAX_ENERGY_LEVEL = 9


def simulate_step(grid):
    flashed = {}
    flashes = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            flashes += visit_octopus(row, col, grid, flashed)
    return flashes


def visit_octopus(row, col, grid, flashed):
    if is_out_of_bounds(row, col, grid):
        return 0

    if grid[row][col] == MAX_ENERGY_LEVEL:
        return flash_octopus(row, col, grid, flashed)
    else:
        if not (row, col) in flashed:
            grid[row][col] += 1
        return 0


def is_out_of_bounds(row, col, grid):
    return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row])


def flash_octopus(row, col, grid, flashed):
    flashes = 0

    grid[row][col] = 0
    flashed[(row, col)] = True
    flashes += 1

    flashes += visit_octopus(row - 1, col, grid, flashed)
    flashes += visit_octopus(row + 1, col, grid, flashed)
    flashes += visit_octopus(row, col - 1, grid, flashed)
    flashes += visit_octopus(row, col + 1, grid, flashed)
    flashes += visit_octopus(row - 1, col - 1, grid, flashed)
    flashes += visit_octopus(row - 1, col + 1, grid, flashed)
    flashes += visit_octopus(row + 1, col - 1, grid, flashed)
    flashes += visit_octopus(row + 1, col + 1, grid, flashed)

    return flashes


def create_grid_from_lines(lines):
    grid = []
    for line in lines:
        numeric_line = []
        for char in line:
            numeric_line.append(int(char))
        grid.append(numeric_line)
    return grid


def calculate_flashes_in_100_steps(grid):
    flashes = 0
    for _ in range(100):
        flashes += simulate_step(grid)
    return flashes


def find_synchronization_step(grid):
    step = 0
    while True:
        flashes = simulate_step(grid)
        step += 1

        assert len(grid) > 0
        # assumes grid is a square
        if flashes == len(grid) * len(grid[0]):
            return step


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day11.txt")
    original_grid = create_grid_from_lines(lines)

    grid = copy.deepcopy(original_grid)
    print(calculate_flashes_in_100_steps(grid))

    grid = copy.deepcopy(original_grid)
    print(find_synchronization_step(grid))
