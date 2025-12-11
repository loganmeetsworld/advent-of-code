from aoc_utils import aoc_utils
from tests import cases

def count_paths(graph, start, end, required_nodes=None, visited=None, found_required=None):
    if required_nodes is None:
        required_nodes = set()
    if visited is None:
        visited = set()
    if found_required is None:
        found_required = set()
    
    if start in visited:
        return 0
    
    new_visited = visited | {start}
    new_found = found_required | ({start} if start in required_nodes else set())
    
    if start == end:
        return 1 if required_nodes.issubset(new_found) else 0
    
    if start not in graph:
        return 0
    
    result = 0
    for node in graph[start]:
        if node not in new_visited:
            result += count_paths(
                graph, node, end, required_nodes, new_visited, new_found
            )
    
    return result


def answer(problem_input, level, test=False):
    device_map = {}
    if level == 1:
        start_node = "you"
    else:
        start_node = "svr"
    end_node = "out"
    for line in problem_input.splitlines():
        device, output = line.split(": ")
        output = output.split()
        device_map[device] = output

    if level == 1:
        return count_paths(device_map, start_node, end_node)
    else:
        return count_paths(device_map, start_node, end_node, {"dac", "fft"})


aoc_utils.run(answer, cases)
