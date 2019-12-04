import re

from aoc_utils import aoc_utils
from tests import cases


def has_double(i):
    found = [match[0] for match in re.findall(r'((\w)\2{1,})', str(i))]
    return len(found) > 0


def ascends_only(i):
    return int(''.join(sorted(str(i)))) == i


def check_criteria(i):
    return has_double(i) and ascends_only(i)


def answer(problem_input, level, test=False):
    if test:
        return check_criteria(problem_input)

    start, end = problem_input.split('-')
    meets_criteria = []
    for i in range(int(start), int(end)):
        meets_criteria.append(check_criteria(i))

    return meets_criteria.count(True)


aoc_utils.run(answer, cases)
