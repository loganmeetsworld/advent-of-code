from aoc_utils import aoc_utils
from tests import cases


def find_differences(numbers: list, delta: int) -> int:
    differences = 0
    for pos, n in enumerate(numbers):
        if len(numbers) == pos + 1:
            continue
        if n - numbers[pos + 1] == delta:
            differences += 1
    return differences


def find_arrangements(numbers: list) -> int:
    return 0


def answer(problem_input, level, test=False):
    numbers = sorted([int(i) for i in problem_input.splitlines()], reverse=True)
    numbers.insert(0, max(numbers) + 3)
    numbers.append(0)
    if level == 1:
        ones, threes = find_differences(numbers, 1), find_differences(numbers, 3)
        return threes * ones
    elif level == 2:
        return find_arrangements(numbers)


aoc_utils.run(answer, cases)
