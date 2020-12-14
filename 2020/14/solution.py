import re

from aoc_utils import aoc_utils
from tests import cases


def run_1(mask, value):
    result = ''
    for x, y in zip(mask, value):
        if x == 'X' and y == '0':
            result += '0'
        elif x == 'X' and y == '1':
            result += '1'
        else:
            result += x

    return int(result, 2)


def run_2(mask, value):
    return 0


def answer(problem_input, level, test=False):
    addresses = {}
    for program in [p.rstrip('\n') for p in problem_input.split('mask = ') if p]:
        bitmask, rules = program.splitlines()[0], [re.findall(r'\d+', i) for i in program.splitlines()[1:]]
        for rule in rules:
            memory_address, decimal = rule
            if level == 1:
                addresses[memory_address] = run_1(bitmask, f'{int(decimal):036b}')
            else:
                addresses[memory_address] = run_2(bitmask, f'{int(decimal):036b}')

    return sum(addresses.values())


aoc_utils.run(answer, cases)
