import itertools

from aoc_utils import aoc_utils
from tests import cases


def valid_check(n: int, seen: int) -> bool:
    sums = [sum(i) for i in itertools.combinations(seen, 2)]
    return n in sums


def find_encryption_weakness(invalid_number: int, numbers: list) -> int:
    for contiguous_range in range(2, len(numbers)):
        for number in range(len(numbers) - contiguous_range):
            range_end = number + contiguous_range
            if sum(numbers[number:range_end]) == invalid_number:
                min_range = min(numbers[number:range_end])
                max_range = max(numbers[number:range_end])
                return min_range + max_range


def answer(problem_input: str, level: int, test=False) -> int:
    preamble = 5 if test else 25
    numbers = [int(i) for i in problem_input.splitlines()]
    seen = numbers[:preamble]
    for n in numbers[preamble:]:
        if not valid_check(n, seen[-preamble:]):
            invalid_number = n
            break
        seen.append(n)

    return invalid_number if level == 1 else find_encryption_weakness(invalid_number, numbers)


aoc_utils.run(answer, cases)
