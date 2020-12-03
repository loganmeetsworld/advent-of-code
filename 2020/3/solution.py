from numpy import prod

from aoc_utils import aoc_utils
from tests import cases


def traverse(problem_input, slopes):
    rows = problem_input.splitlines()
    tree_counts = []
    for slope in slopes:
        tree_pos, tree_count, row_pos = 0, 0, 0
        while row_pos < len(rows):
            row = rows[row_pos]
            if row[tree_pos % len(row)] == '#':
                tree_count += 1
            tree_pos += slope[1]
            row_pos += slope[0]
        tree_counts.append(tree_count)
    return prod(tree_counts)


def answer(problem_input, level, test=False):
    if level == 1:
        return traverse(problem_input, [[1, 3]])
    elif level == 2:
        return traverse(problem_input, [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]])


aoc_utils.run(answer, cases)
