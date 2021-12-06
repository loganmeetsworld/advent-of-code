import re

from collections import Counter


from aoc_utils import aoc_utils
from tests import cases


def find_all_coordinates(x1, y1, x2, y2, part_one=False):
    points = []

    dx = x1 - x2
    dy = y1 - y2 

    # Like 2,2 -> 2,1
    if dx == 0:
        for y in range(min([y2, y1]), max([y2, y1]) + 1):
            points.append(str([x1, y]))

    # Like 0,9 -> 5,9
    if dy == 0:
        for x in range(min([x2, x1]), max([x2, x1]) + 1):
            points.append(str([x, y1]))

    if part_one:
        return points
    
    # Like 1,1 -> 3,3
    if dx < 0 and dy < 0:
        for i in range(abs(dx) + 1):
            points.append(str([x1 + i, y1 + i]))

    # Like 3,3 -> 1,1
    if dx > 0 and dy > 0:
        for i in range(abs(dx) + 1):
            points.append(str([x1 - i, y1 - i]))

    # Like 9,7 -> 7,9
    if dx > 0 and dy < 0:
        for i in range(abs(dx) + 1):
            points.append(str([x1 - i, y1 + i]))

    # Like 7,9 > 9,7
    if dx < 0 and dy > 0:
        for i in range(abs(dx) + 1):
            points.append(str([x1 + i, y1 - i]))

    return points


def horrizontal_points(x1, y1, x2, y2):
    points = []

    if x1 - x2 == 0:
        for y in range(min([y2, y1]), max([y2, y1]) + 1):
            points.append(str([x1, y]))
    if y1 - y2 == 0:
        for x in range(min([x2, x1]), max([x2, x1]) + 1):
            points.append(str([x, y1]))

    return points


def answer(problem_input, level, test=False):
    coordinates = []
    for line in problem_input.splitlines():
        coords = [int(i) for i in re.findall(r'(\d+)', line)]
        if level == 1:
            coordinates += find_all_coordinates(*coords, part_one=True)
        else:
            coordinates += find_all_coordinates(*coords)

    return len([k for k,v in Counter(coordinates).items() if v > 1])


aoc_utils.run(answer, cases)
