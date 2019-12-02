from aoc_utils import aoc_utils
from functools import reduce
import operator
from tests import cases


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


OPSCODE_INSTR = {1: sum, 2: prod}
PART_ONE_INIT_STATE = [12, 2]
PART_TWO_OUTPUT = 19690720


def next_integers(integers, opscode, int_one, int_two, next_place):
    manipulator = OPSCODE_INSTR[opscode]
    integers[next_place] = manipulator([integers[int_one], integers[int_two]])
    return integers


def part_two_final_calculation(noun, verb):
    return 100 * noun + verb


def restore_state(integers, init_state):
    integers[1], integers[2] = init_state
    return integers


def run(problem_input, init_state, test=False):
    integers = [int(i) for i in problem_input.split(',')]
    if not test:
        # None of our tests were made for the 1202 state, so only use when not in test mode.
        integers = restore_state(integers, init_state)

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


def answer(problem_input, level, test=False):
    if level == 1:
        return run(problem_input, PART_ONE_INIT_STATE, test)
    if level == 2:
        for a in range(0, 99):
            for b in range(0, 99):
                output = run(problem_input, [a, b])
                if output == PART_TWO_OUTPUT:
                    return part_two_final_calculation(a, b)


aoc_utils.run(answer, cases)
