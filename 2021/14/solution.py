from collections import Counter

from aoc_utils import aoc_utils
from tests import cases



def transform(polymer, rules):
    return polymer


def answer(problem_input, level, test=False):
    steps = 10
    polymer, rules = problem_input.split("\n\n")
    for _ in range(steps):
        polymer = transform(polymer, [r.split(' -> ') for r in rules.splitlines()])

    counter = Counter(polymer).most_common()
    return counter[0][1] - counter[-1][1]


aoc_utils.run(answer, cases)
