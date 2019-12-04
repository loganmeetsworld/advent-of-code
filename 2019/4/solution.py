import re

from aoc_utils import aoc_utils
from tests import cases


def has_repeats(i, level):
    found = [match[0] for match in re.findall(r'((\d)\2{1,})', str(i))]
    if level == 2:
        found = [f for f in found if len(f) == 2]
    return len(found) > 0


def ascends_only(i):
    return int(''.join(sorted(str(i)))) == i


def check_criteria(i, level):
    return has_repeats(i, level) and ascends_only(i)


def answer(problem_input, level, test=False):
    if test:
        return check_criteria(problem_input, level)
    start, end = problem_input.split('-')
    meets_criteria = []
    for i in range(int(start), int(end)):
        meets_criteria.append(check_criteria(i, level))
    return meets_criteria.count(True)


aoc_utils.run(answer, cases)
