from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    calories = []
    for ration in problem_input.split("\n\n"):
        calories.append(sum([int (meal) for meal in ration.splitlines()]))

    return max(calories) if level == 1 else sum(sorted(calories, reverse=True)[0:3])


aoc_utils.run(answer, cases)
