from collections import Counter


from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    directions = [l.split(' -> ') for l in problem_input.splitlines()]
    coordinates = []
    for direction in directions:
        point_one = [int(n) for n in direction[0].split(',')]
        point_two = [int(n) for n in direction[1].split(',')]
        if point_one[0] == point_two[0]:
            for y in range(min([point_two[1], point_one[1]]), max([point_two[1], point_one[1]]) + 1):
                coordinates.append([point_one[0], y])
        if point_one[1] == point_two[1]:
            for x in range(min([point_two[0], point_one[0]]), max([point_two[0], point_one[0]]) + 1):
                coordinates.append([x, point_one[1]])
    coord_counter = dict(Counter([str(c) for c in coordinates]))
    return len([k for k,v in Counter(coord_counter).items() if v>1])


aoc_utils.run(answer, cases)
