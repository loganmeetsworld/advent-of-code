from collections import defaultdict

from aoc_utils import aoc_utils
from tests import cases


def search(graph, node):
    # do something
    return 0

def answer(problem_input, level, test=False):
    graph = defaultdict(list)
    for line in problem_input.splitlines():
        origin, dest = line.split('-')
        if dest != 'start' and origin != 'end':
            graph[origin].append(dest)
        if origin != 'start' and dest != 'end':
            graph[dest].append(origin)
    print(graph)
    return search(graph, 'start')

aoc_utils.run(answer, cases)
