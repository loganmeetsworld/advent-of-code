from aoc_utils import aoc_utils
from tests import cases


def part_1(binaries):
    rate = ''

    for vertical_bits in zip(*binaries):
        if sum([int(bit) for bit in vertical_bits]) >= len(binaries) / 2:
            rate += '1'
        else:
            rate += '0'

    return int(rate, 2) * int(''.join('1' if x == '0' else '0' for x in rate), 2)


def part_2(binaries, dominant, non_dominant):
    for idx in range(len(binaries[0])):
        ones_count = sum([int(i) for i in list(zip(*binaries))[idx]])
        
        if ones_count >= len(binaries) / 2:
            binaries = list(filter(lambda x: x[idx] == dominant, binaries))
        else:
            binaries = list(filter(lambda x: x[idx] == non_dominant, binaries))

        if len(binaries) == 1: break

    return int(binaries[0], 2)


def answer(problem_input, level, test=False):
    binaries = [binary for binary in problem_input.splitlines()]
    if level == 1:
        return part_1(binaries)
    elif level == 2:
        return part_2(binaries, '1', '0') * part_2(binaries, '0', '1')


aoc_utils.run(answer, cases)
