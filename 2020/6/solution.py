from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    counts = [len(set(group.replace('\n', ''))) for group in problem_input.split('\n\n')]
    return sum(counts)


aoc_utils.run(answer, cases)
