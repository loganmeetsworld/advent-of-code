from aoc_utils import aoc_utils
from tests import cases


def find_max_viewed(asteroid_map):
    views = []
    for line in asteroid_map.splitlines():
        view = line.count('#')
        views.append(view)

    return max(views)


def answer(problem_input, level, test=False):
    max_viewed = find_max_viewed(problem_input)
    return max_viewed


aoc_utils.run(answer, cases)
