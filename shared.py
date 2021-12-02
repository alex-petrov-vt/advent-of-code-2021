def get_lines_from_file(filename):
    result = []
    f = open(filename, "r")
    for line in f.readlines():
        result.append(line.strip())
    return result


def convert_lines_to_ints(lines):
    result = []
    for line in lines:
        result.append(int(line.strip()))
    return result
