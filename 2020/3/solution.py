from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    tree_pos, tree_count = 0, 0
    for row in problem_input.splitlines():
        if row[tree_pos % len(row)] == '#':
            tree_count += 1
        tree_pos += 3
    return tree_count


aoc_utils.run(answer, cases)
