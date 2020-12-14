import re

from aoc_utils import aoc_utils
from tests import cases


def run_program(bitmask, rules):
    return 0


def answer(problem_input, level, test=False):
    sums = []
    for program in [p.rstrip('\n') for p in problem_input.split('mask = ') if p]:
        program = program.splitlines()
        bitmask, rules = program[0], [re.findall(r'\d+', i) for i in program[1:]]
        sums.append(run_program(bitmask, rules))

    return sum(sums)


aoc_utils.run(answer, cases)
