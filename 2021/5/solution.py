import re

from collections import Counter


from aoc_utils import aoc_utils
from tests import cases

def points_between(x1, y1, x2, y2):
    coordinates = []

    if x1 - x2 == 0:
        for y in range(min([y2, y1]), max([y2, y1]) + 1):
            coordinates.append(str([x1, y]))
    if y1 - y2 == 0:
        for x in range(min([x2, x1]), max([x2, x1]) + 1):
            coordinates.append(str([x, y1]))

    return coordinates


def answer(problem_input, level, test=False):
    coordinates = []
    for line in problem_input.splitlines():
        coordinates += points_between(*[int(i) for i in re.findall(r'(\d+)', line)])

    return len([k for k,v in Counter(coordinates).items() if v > 1])


aoc_utils.run(answer, cases)
