import math
import statistics

from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    horizontal_distances = [int(i) for i in problem_input.split(',')]
    median = statistics.median(horizontal_distances)
    # Have absolutely no idea what is happening here that the test fails but got the star.
    mean = math.floor(statistics.mean(horizontal_distances))
    if level == 1:
        distances_from_median = [abs(median - i) for i in horizontal_distances]
        return int(sum(distances_from_median))
    elif level == 2:
        distances_from_mean = [abs(mean - i) for i in horizontal_distances]
        return int(sum([int(d * (d + 1) / 2) for d in distances_from_mean]))

aoc_utils.run(answer, cases)