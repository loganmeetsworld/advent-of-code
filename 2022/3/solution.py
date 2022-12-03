from aoc_utils import aoc_utils
from tests import cases


def chunks(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


def find_common_item(parts):
    return set.intersection(*map(set, parts)).pop()


def score_letter(letter):
    if letter.isupper():
        return ord(letter) - 38
    elif letter.islower():
        return ord(letter) - 96


def answer(problem_input, level, test=False):
    rucksacks = problem_input.splitlines()
    total_sum = 0
    if level == 1:
        for rucksack in rucksacks:
            rucksack_groups = chunks(rucksack, int(len(rucksack)/2))
            total_sum += score_letter(find_common_item(rucksack_groups))
    elif level == 2:
        rucksack_groups = chunks(rucksacks, 3)
        for rucksack_group in rucksack_groups:
            total_sum += score_letter(find_common_item(rucksack_group))

    return total_sum


aoc_utils.run(answer, cases)
