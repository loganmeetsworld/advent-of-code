from numpy import prod

from aoc_utils import aoc_utils
from tests import cases


def traverse(rows, slopes):
    terrain_translation, tree_counts = {'.': 0, '#': 1}, []
    for slope in slopes:
        tree_pos, row_pos, tree_count = 0, 0, 0
        while row_pos < len(rows):
            row = rows[row_pos]
            tree_count += terrain_translation[row[tree_pos % len(row)]]
            tree_pos += slope[0]
            row_pos += slope[1]
        tree_counts.append(tree_count)
    return prod(tree_counts)


def answer(problem_input, level, test=False):
    slopes = [[3, 1]]
    if level == 2:
        slopes += [[1, 1], [5, 1], [7, 1], [1, 2]]
    return traverse(problem_input.splitlines(), slopes)


aoc_utils.run(answer, cases)
