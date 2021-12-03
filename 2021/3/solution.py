from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    gamma_rate, epsilon_rate = '', ''
    binaries = [i for i in problem_input.splitlines()]

    for b in zip(*binaries):
        if sum([int(i) for i in b]) > (len(binaries) / 2):
            gamma_rate += '1'; epsilon_rate += '0'
        else:
            gamma_rate += '0'; epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


aoc_utils.run(answer, cases)
