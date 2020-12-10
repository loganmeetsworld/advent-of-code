from collections import defaultdict

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
    # Tracker for all adapter's compatabilities starting with a single adapter
    arrangement_tracker = defaultdict(lambda: 0)
    # If there were no adapter, there would be 1 compatible pattern
    arrangement_tracker[0] = 1
    for n in numbers:
        # For each number, sum its adapter compatibility at the last 3 positions
        # And save it as the compatability number for that position and in subsequent sums it will be tallied
        # Because we use defaultdict, if there is no adapter at that position indexing will return 0
        arrangement_tracker[n] = sum([arrangement_tracker[n - i] for i in [1, 2, 3]])

    # By the end, the biggest slot should have all the possible compatabilities
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
