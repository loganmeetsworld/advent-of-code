from numpy import prod

from aoc_utils import aoc_utils
from tests import cases


def traverse(rows, slopes):
    tree_counts = []
    for slope in slopes:
        tree_pos, row_pos, tree_count = 0, 0, 0
        while row_pos < len(rows):
            row = rows[row_pos]
            if rows[row_pos][tree_pos % len(row)] == '#':
                tree_count += 1
            tree_pos += slope[0]
            row_pos += slope[1]
        tree_counts.append(tree_count)
    return prod(tree_counts)


def answer(problem_input, level, test=False):
    rows = problem_input.splitlines()
    slopes = [[3, 1]]
    if level == 2:
        slopes += [[1, 1], [5, 1], [7, 1], [1, 2]]
    return traverse(rows, slopes)


aoc_utils.run(answer, cases)
