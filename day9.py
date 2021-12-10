from shared import get_lines_from_file


def find_lowest_points(heightmap):
    result = []
    locations = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if is_low_point(x, y, heightmap):
                result.append(heightmap[y][x])
                locations.append((x, y))
    return result, locations


def is_low_point(x, y, heightmap):
    return (
        (is_out_of_bounds(x - 1, y, heightmap) or heightmap[y][x - 1] > heightmap[y][x])
        and (
            is_out_of_bounds(x + 1, y, heightmap)
            or heightmap[y][x + 1] > heightmap[y][x]
        )
        and (
            is_out_of_bounds(x, y - 1, heightmap)
            or heightmap[y - 1][x] > heightmap[y][x]
        )
        and (
            is_out_of_bounds(x, y + 1, heightmap)
            or heightmap[y + 1][x] > heightmap[y][x]
        )
    )


def is_out_of_bounds(x, y, heightmap):
    return y < 0 or y >= len(heightmap) or x < 0 or x >= len(heightmap[y])


def find_risk(lowest_points):
    result = 0
    for height in lowest_points:
        risk = height + 1
        result += risk
    return result


def build_heightmap(lines):
    result = []
    for line in lines:
        result_row = []
        for digit in line:
            result_row.append(int(digit))
        result.append(result_row)
    return result


def find_three_largest_basins_product(heightmap):
    basins = find_basins_size(heightmap)
    sorted_basins = sorted(basins, reverse=True)
    assert len(sorted_basins) >= 3
    return sorted_basins[0] * sorted_basins[1] * sorted_basins[2]


def find_basins_size(heightmap):
    lowest_points_locations = find_lowest_points(heightmap)[1]
    basins_size = []
    for location in lowest_points_locations:
        basins_size.append(get_basin_size(location, heightmap))
    return basins_size


def get_basin_size(location, heightmap):
    size = 1
    visited = {location: True}
    neighbors = get_valid_neighbors(location, heightmap, visited)
    size += len(neighbors)
    while neighbors:
        new_neighbors = []
        for neighbor in neighbors:
            new_local_neighbors = get_valid_neighbors(neighbor, heightmap, visited)
            size += len(new_local_neighbors)
            new_neighbors.extend(new_local_neighbors)
        neighbors = new_neighbors
    return size


def get_valid_neighbors(location, heightmap, visited):
    x, y = location[0], location[1]
    neighbors = []

    if (
        not is_out_of_bounds(x - 1, y, heightmap)
        and heightmap[y][x - 1] != 9
        and (x - 1, y) not in visited
    ):
        visited[(x - 1, y)] = True
        neighbors.append((x - 1, y))

    if (
        not is_out_of_bounds(x + 1, y, heightmap)
        and heightmap[y][x + 1] != 9
        and (x + 1, y) not in visited
    ):
        visited[(x + 1, y)] = True
        neighbors.append((x + 1, y))

    if (
        not is_out_of_bounds(x, y - 1, heightmap)
        and heightmap[y - 1][x] != 9
        and (x, y - 1) not in visited
    ):
        visited[(x, y - 1)] = True
        neighbors.append((x, y - 1))

    if (
        not is_out_of_bounds(x, y + 1, heightmap)
        and heightmap[y + 1][x] != 9
        and (x, y + 1) not in visited
    ):
        visited[(x, y + 1)] = True
        neighbors.append((x, y + 1))

    return neighbors


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day9.txt")

    heightmap = build_heightmap(lines)
    print(find_risk(find_lowest_points(heightmap)[0]))
    print(find_three_largest_basins_product(heightmap))
