from aoc_utils import aoc_utils
from tests import cases


def mutate_ints(integers, opscode, actionable_ints, new_place):
    if opscode == 1:
        new_value = integers[actionable_ints[0]] + integers[actionable_ints[1]]
    elif opscode == 2:
        new_value = integers[actionable_ints[0]] * integers[actionable_ints[1]]

    integers[new_place] = new_value

    return integers


def restore_state(integers):
    integers[1] = 12
    integers[2] = 2

    return integers


def answer(problem_input, part):
    integers = [int(i) for i in problem_input.split(',')]
    integers = restore_state(integers)

    opscode_pos = 0
    opscode = integers[opscode_pos]
    actionable_ints_min = opscode
    actionable_ints_max = opscode + 2
    new_place_pos = opscode_pos + 3
    actionable_ints = integers[actionable_ints_min:actionable_ints_max]
    new_place = integers[new_place_pos]

    while True:
        integers = mutate_ints(integers, opscode, actionable_ints, new_place)
        opscode_pos += 4
        opscode = integers[opscode_pos]
        if opscode == 99:
            return integers[0]
        actionable_ints_min = opscode_pos + 1
        actionable_ints_max = opscode_pos + 3
        new_place_pos = opscode_pos + 3
        actionable_ints = integers[actionable_ints_min:actionable_ints_max]
        new_place = integers[new_place_pos]

    return integers[0]


aoc_utils.run(answer)
