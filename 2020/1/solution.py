from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    year = 2020
    numbers = [int(i) for i in problem_input.splitlines()]
    for num in numbers:
        if (year - num) in numbers:
            return num * (year - num)


aoc_utils.run(answer, cases)
