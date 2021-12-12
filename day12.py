import copy

from shared import get_lines_from_file

def build_graph(lines):
    result = {}
    for line in lines:
        start, end = line.strip().split("-")

        if end != "start":
            if start in result:
                result[start].append(end)
            else:
                result[start] = [end]

        if end != "end" and start != "start":
            if end in result:
                result[end].append(start)
            else:
                result[end] = [start]
        elif end == "end":
            result[end] = []

    return result

def count_paths(graph):
    assert "start" in graph and "end" in graph
    visited = {}
    return count_paths_helper("start", graph, visited)

def count_paths_helper(node, graph, visited):
    if node == "end":
        return 1

    if node.islower():
        if node not in visited:
            visited[node] = True
        else:
            return 0

    result = 0
    for neighbor in graph[node]:
        new_visited = copy.deepcopy(visited)
        result += count_paths_helper(neighbor, graph, new_visited)
    return result

def count_paths_can_visit_twice(graph):
    assert "start" in graph and "end" in graph
    visited = {}
    return count_paths_helper_can_visit_twice("start", graph, visited, False)

def count_paths_helper_can_visit_twice(node, graph, visited, second_visit_used):
    if node == "end":
        return 1

    if node.islower():
        if node not in visited:
            visited[node] = True
        else:
            if not second_visit_used:
                second_visit_used = True
            else:
                return 0

    result = 0
    for neighbor in graph[node]:
        new_visited = copy.deepcopy(visited)
        result += count_paths_helper_can_visit_twice(neighbor, graph, new_visited, second_visit_used)
    return result


if __name__ == "__main__":
    lines = get_lines_from_file("./input/day12.txt")

    graph = build_graph(lines)
    print(count_paths(graph))
    print(count_paths_can_visit_twice(graph))
