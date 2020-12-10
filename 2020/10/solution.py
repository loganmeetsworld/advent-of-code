from aoc_utils import aoc_utils
from tests import cases


def find_differences(numbers, delta) -> int:
    count = 0
    for pos, n in enumerate(numbers):
        if len(numbers) == pos + 1:
            continue
        if n - numbers[pos + 1] == delta:
            count += 1
    return count


def answer(problem_input, level, test=False):
    numbers = sorted([int(i) for i in problem_input.splitlines()], reverse=True)
    numbers.insert(0, max(numbers) + 3)
    numbers.append(0)
    ones = find_differences(numbers, 1)
    threes = find_differences(numbers, 3)
    return threes * ones


aoc_utils.run(answer, cases)
