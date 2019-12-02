from aoc_utils import aoc_utils
from functools import reduce
import operator
from tests import cases


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


OPSCODE_INSTR = {1: sum, 2: prod}


def next_integers(integers, opscode, int_one, int_two, next_place):
    manipulator = OPSCODE_INSTR[opscode]
    integers[next_place] = manipulator([integers[int_one], integers[int_two]])
    return integers


def restore_1202_state(integers):
    integers[1] = 12
    integers[2] = 2

    return integers


def answer(problem_input, level, test=False):
    integers = [int(i) for i in problem_input.split(',')]
    if not test:
        # None of our tests were made for the 1202 state, so only use when not in test mode.
        integers = restore_1202_state(integers)

    opscode_pos = 0
    opscode = integers[opscode_pos]
    int_one, int_two = integers[opscode_pos + 1:opscode_pos + 3]
    next_place = integers[opscode_pos + 3]

    while True:
        integers = next_integers(integers, opscode, int_one, int_two, next_place)
        opscode_pos += 4
        opscode = integers[opscode_pos]
        if opscode == 99:
            return integers[0]
        int_one, int_two = integers[opscode_pos + 1:opscode_pos + 3]
        next_place = integers[opscode_pos + 3]

    return integers[0]


aoc_utils.run(answer, cases)
