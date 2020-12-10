from aoc_utils import aoc_utils
from tests import cases


def find_differences(numbers: list, delta: int) -> int:
    numbers.append(0)
    differences = 0
    for pos, n in enumerate(numbers):
        if len(numbers) == pos + 1:
            continue
        if n - numbers[pos + 1] == delta:
            differences += 1
    return differences


def find_arrangements(numbers: list) -> int:
    arrangement_tracker = {0: 1}
    for n in numbers:
        arrangement_tracker[n] = sum([arrangement_tracker.get(n - i, 0) for i in [1, 2, 3]])

    return arrangement_tracker[max(numbers)]


def answer(problem_input, level, test=False):
    numbers = [int(i) for i in problem_input.splitlines()]
    numbers += [max(numbers) + 3]
    if level == 1:
        numbers = sorted(numbers, reverse=True)
        ones, threes = find_differences(numbers, 1), find_differences(numbers, 3)
        return threes * ones
    elif level == 2:
        numbers = sorted(numbers)
        return find_arrangements(numbers)


aoc_utils.run(answer, cases)
