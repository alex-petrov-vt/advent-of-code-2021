from shared import get_lines_from_file


class FloorMap:
    def __init__(self, width, height):
        self.locations = [[0 for i in range(width)] for j in range(height)]

    def _initialize_locations(self, width, height):
        result = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(0)
            result.append(row)
        return result

    def __str__(self):
        result = []
        for row in self.locations:
            row_string = []
            for location in row:
                if location == 0:
                    row_string.append(".")
                else:
                    row_string.append(str(location))

            result.append("".join(row_string))
            row_string = []
        return "\n".join(result)

    def get_location(self, x, y):
        return self.locations[y][x]

    def set_location(self, x, y, val):
        self.locations[y][x] = val

    def get_number_of_overlaps(self):
        result = 0
        for row in self.locations:
            for location in row:
                if location > 1:
                    result += 1
        return result

    def add_line(self, x1, y1, x2, y2):
        if x1 == x2:
            self._add_vertical_line(x1, y1, y2)
        elif y1 == y2:
            self._add_horizontal_line(y1, x1, x2)
        elif is_45_degree_diagonal_line(x1, y1, x2, y2):
            self._add_diagonal_line(x1, y1, x2, y2)

    def _add_vertical_line(self, x, y1, y2):
        if y1 <= y2:
            for y in range(y1, y2 + 1):
                self.set_location(x, y, self.get_location(x, y) + 1)
        else:
            for y in range(y2, y1 + 1):
                self.set_location(x, y, self.get_location(x, y) + 1)

    def _add_horizontal_line(self, y, x1, x2):
        if x1 <= x2:
            for x in range(x1, x2 + 1):
                self.set_location(x, y, self.get_location(x, y) + 1)
        else:
            for x in range(x2, x1 + 1):
                self.set_location(x, y, self.get_location(x, y) + 1)

    def _add_diagonal_line(self, x1, y1, x2, y2):
        while x1 != x2 and y1 != y2:
            self.set_location(x1, y1, self.get_location(x1, y1) + 1)
            if x2 > x1:
                x1 += 1
            else:
                x1 -= 1

            if y2 > y1:
                y1 += 1
            else:
                y1 -= 1
        # Want to also add last point where x1 = x2 and y1 = y2
        self.set_location(x1, y1, self.get_location(x1, y1) + 1)


def get_coordinates_from_line(line):
    start, end = line.strip().split("->")
    x1, y1 = start.split(",")
    x2, y2 = end.split(",")
    return int(x1), int(y1), int(x2), int(y2)


def is_45_degree_diagonal_line(x1, y1, x2, y2):
    return abs(x2 - x1) == abs(y2 - y1)


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day5.txt")

    floor_map = FloorMap(1000, 1000)
    for line in lines:
        x1, y1, x2, y2 = get_coordinates_from_line(line)
        floor_map.add_line(x1, y1, x2, y2)

    print(floor_map.get_number_of_overlaps())
