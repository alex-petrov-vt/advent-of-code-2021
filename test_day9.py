from day9 import (
    build_heightmap,
    find_lowest_points,
    find_risk,
    find_basins_size,
    find_three_largest_basins_product,
)


def test_build_heightmap():
    input = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]

    heightmap = build_heightmap(input)
    assert heightmap == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_find_lowest_points():
    input = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]

    lowest_points = find_lowest_points(input)[0]
    assert lowest_points == [1, 0, 5, 5]


def test_find_risk():
    input = [1, 0, 5, 5]
    risk = find_risk(input)
    assert risk == 15


def test_find_basins_size():
    input = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    assert find_basins_size(input) == [3, 9, 14, 9]
    assert find_three_largest_basins_product(input) == 1134
