import itertools
import numpy

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    numbers = [int(i) for i in problem_input.splitlines()]
    for combo in itertools.combinations(numbers, level + 1):
        if sum(combo) == 2020:
            return numpy.prod(combo)


aoc_utils.run(answer, cases)
