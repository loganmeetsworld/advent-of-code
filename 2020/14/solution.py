import re

from aoc_utils import aoc_utils
from tests import cases


def run_program(mask, decimal):
    value = f'{int(decimal):036b}'
    result = ''
    for x, y in zip(mask, value):
        if x == 'X' and y == '0':
            result += '0'
        elif x == 'X' and y == '1':
            result += '1'
        else:
            result += x

    return int(result, 2)


def answer(problem_input, level, test=False):
    addresses = {}
    for program in [p.rstrip('\n') for p in problem_input.split('mask = ') if p]:
        bitmask, rules = program.splitlines()[0], [re.findall(r'\d+', i) for i in program.splitlines()[1:]]
        for rule in rules:
            memory_address, decimal = rule
            addresses[memory_address] = run_program(bitmask, decimal)

    return sum(addresses.values())


aoc_utils.run(answer, cases)
