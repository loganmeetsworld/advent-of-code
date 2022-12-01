from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    rations = problem_input.split("\n\n")
    calories = []
    for ration in rations:
        calories.append(sum([int (r) for r in ration.splitlines()]))
    if level == 1:
        return max(calories)
    elif level == 2:
        return sum(sorted(calories, reverse=True)[0:3])


aoc_utils.run(answer, cases)
