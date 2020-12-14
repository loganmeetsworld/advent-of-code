import re

from aoc_utils import aoc_utils
from tests import cases


def run_program(bitmask, rules):
    for rule in rules:
        memory_address, decimal = rule
        decimal_as_binary = f'{int(decimal):036b}'
        for x, y in zip(bitmask, decimal_as_binary):
            print(x)
            print(y)
    return 0


def answer(problem_input, level, test=False):
    sums = []
    for program in [p.rstrip('\n') for p in problem_input.split('mask = ') if p]:
        bitmask, rules = program.splitlines()[0], [re.findall(r'\d+', i) for i in program.splitlines()[1:]]
        sums.append(run_program(bitmask, rules))

    return sum(sums)


aoc_utils.run(answer, cases)
