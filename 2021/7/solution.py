import statistics

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    horizontal_distances = [int(i) for i in problem_input.split(',')]
    median = statistics.median(horizontal_distances)
    return int(sum([abs(median - i) for i in horizontal_distances]))


aoc_utils.run(answer, cases)
