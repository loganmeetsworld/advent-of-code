from aoc_utils import aoc_utils
from tests import cases
import math
from itertools import combinations


def sort_distances(coords):
    distances_with_pairs = []
    for p1, p2 in combinations(coords, 2):
        distance = math.dist(p1, p2)
        distances_with_pairs.append((distance, (p1, p2)))

    distances_with_pairs.sort(key=lambda x: x[0], reverse=True)
    return distances_with_pairs


def answer(problem_input, level, test=False):
    coords = [[int(n) for n in l.split(",")] for l in problem_input.splitlines()]
    distances = sort_distances(coords)
    point_one, point_two = distances[0][1]
    return (abs(point_one[0] - point_two[0]) + 1) * (abs(point_one[1] - point_two[1]) + 1)


aoc_utils.run(answer, cases)
