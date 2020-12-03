from numpy import prod

from aoc_utils import aoc_utils
from tests import cases


def traverse(rows, x, y):
    tree_pos, tree_count = 0, 0
    for row in rows:
        if row[tree_pos % len(row)] == '#':
            tree_count += 1
        tree_pos += y
    print(tree_count)
    return tree_count


def answer(problem_input, level, test=False):
    rows = problem_input.splitlines()
    if level == 1:
        return traverse(rows, 1, 3)
    elif level == 2:
        return prod([traverse(rows, 1, 1), traverse(rows, 1, 3), traverse(rows, 1, 5), traverse(rows, 1, 7), traverse(rows, 2, 1)])


aoc_utils.run(answer, cases)
