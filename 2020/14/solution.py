import re

from aoc_utils import aoc_utils
from tests import cases


def run_version_1(mask, value):
    result = ''
    for x, y in zip(mask, value):
        if x == 'X' and y == '0':
            result += '0'
        elif x == 'X' and y == '1':
            result += '1'
        else:
            result += x

    return int(result, 2)


def run_version_2(mask, value):
    result = []
    holder = ''
    for pos, v in enumerate(mask):
        if v == 'X':
            holder += '{}'
        elif v == '1':
            holder += '1'
        else:
            holder += value[pos]

    for n in range(2**mask.count('X')):
        n = bin(n)[2:].zfill(mask.count('X'))
        # Kind of a cool trick to take a bunch of empty {} and append string to them
        result.append(holder.format(*n))

    return [int(x, 2) for x in result]


def answer(problem_input, level, test=False):
    addresses = {}
    for program in [p.rstrip('\n') for p in problem_input.split('mask = ') if p]:
        bitmask, rules = program.splitlines()[0], [re.findall(r'\d+', i) for i in program.splitlines()[1:]]
        for rule in rules:
            memory_address, decimal = rule
            if level == 1:
                addresses[memory_address] = run_version_1(bitmask, f'{int(decimal):036b}')
            else:
                for address in run_version_2(bitmask, f'{int(memory_address):036b}'):
                    addresses[address] = int(decimal)

    return sum(addresses.values())


aoc_utils.run(answer, cases)
