from day5 import FloorMap, get_coordinates_from_line


def test_parse_line():
    line = "1,1 -> 1,3"
    x1, y1, x2, y2 = get_coordinates_from_line(line)
    assert x1 == 1
    assert x2 == 1
    assert y1 == 1
    assert y2 == 3

    line = "9,7 -> 7,7"
    x1, y1, x2, y2 = get_coordinates_from_line(line)
    assert x1 == 9
    assert x2 == 7
    assert y1 == 7
    assert y2 == 7


def test_floor_map():
    floor_map = FloorMap(10, 10)
    floor_map.add_line(1, 1, 1, 3)
    assert floor_map.get_location(1, 1) == 1
    assert floor_map.get_location(1, 2) == 1
    assert floor_map.get_location(1, 3) == 1
    floor_map = FloorMap(10, 10)
    floor_map.add_line(9, 7, 7, 7)
    assert floor_map.get_location(9, 7) == 1
    assert floor_map.get_location(8, 7) == 1
    assert floor_map.get_location(7, 7) == 1
    floor_map = FloorMap(10, 10)
    floor_map.add_line(3, 3, 5, 5)
    assert floor_map.get_location(3, 3) == 1
    assert floor_map.get_location(4, 4) == 1
    assert floor_map.get_location(5, 5) == 1
    floor_map = FloorMap(10, 10)
    floor_map.add_line(9, 7, 7, 9)
    assert floor_map.get_location(9, 7) == 1
    assert floor_map.get_location(8, 8) == 1
    assert floor_map.get_location(7, 9) == 1


def test_printing_floor_map():
    floor_map = FloorMap(10, 10)
    floor_map.add_line(1, 1, 1, 3)
    floor_map.add_line(9, 7, 7, 7)
    assert (
        str(floor_map)
        == """..........
.1........
.1........
.1........
..........
..........
..........
.......111
..........
.........."""
    )

    lines = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]

    floor_map = FloorMap(10, 10)
    for line in lines:
        x1, y1, x2, y2 = get_coordinates_from_line(line)
        floor_map.add_line(x1, y1, x2, y2)

    assert (
        str(floor_map)
        == """1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111...."""
    )
    assert floor_map.get_number_of_overlaps() == 12
