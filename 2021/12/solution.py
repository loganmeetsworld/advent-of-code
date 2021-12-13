from collections import (Counter, defaultdict, deque)

from aoc_utils import aoc_utils
from tests import cases


def search(graph):
    paths = deque([['start']])
    valid_paths = []

    while paths:
        current_path = paths.pop()
        current_node = current_path[-1]

        if current_node == 'end':
            valid_paths.append(current_path)
            continue

        for node in graph[current_node]:
            if node.isupper() or node not in current_path:
                paths.append(current_path + [node])

    return valid_paths

def answer(problem_input, level, test=False):
    graph = defaultdict(set)
    for line in problem_input.splitlines():
        (origin, dest) = tuple(line.split('-'))
        graph[origin].add(dest)
        graph[dest].add(origin)

    return search(graph)

aoc_utils.run(answer, cases)
