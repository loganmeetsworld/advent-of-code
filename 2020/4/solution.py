from aoc_utils import aoc_utils
from tests import cases

REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
# OPTIONAL_ATTRIBUTES = ["cid"]


def answer(problem_input, level, test=False):
    valid_count = 0
    elves = [e.replace("\n", " ") for e in problem_input.split("\n\n")]
    for e in elves:
        attributes = [a.split(':')[0] for a in e.split(' ')]
        if len(list(set(REQUIRED_ATTRIBUTES) - set(attributes))) == 0:
            valid_count += 1
    return valid_count


aoc_utils.run(answer, cases)
