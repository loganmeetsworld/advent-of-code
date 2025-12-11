from aoc_utils import aoc_utils
from tests import cases

# Classic recursive depth first search
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    if start not in graph:
        return []

    all_paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                all_paths.append(new_path)

    return all_paths


def answer(problem_input, level, test=False):
    device_map = {}
    start_node = "you"
    end_node = "out"
    for line in problem_input.splitlines():
        device, output = line.split(": ")
        output = output.split()
        device_map[device] = output
    
    paths = find_all_paths(device_map, start_node, end_node)
    return len(paths)


aoc_utils.run(answer, cases)
