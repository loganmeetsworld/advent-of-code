import itertools

from aoc_utils import aoc_utils
from tests import cases


def valid_check(n, seen):
    sums = [sum(i) for i in itertools.combinations(seen, 2)]
    return n in sums


def answer(problem_input, level, test=False):
    preamble = 5 if test else 25
    numbers = [int(i) for i in problem_input.splitlines()]
    seen = numbers[:preamble]
    for n in numbers[preamble:]:
        if not valid_check(n, seen[-preamble:]):
            return n
        seen.append(n)


aoc_utils.run(answer, cases)
