from aoc_utils import aoc_utils
from tests import cases


JUMP_STEPS = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}


def run(problem_input, level):
    input_id = 1 if level == 1 else 5
    integers = [int(i) for i in problem_input.split(",")]
    opscode_pos, next_pos, first_param = 0, 0, 0

    while True:
        full_opcode = str(integers[opscode_pos]).zfill(5)
        opcode = int(full_opcode[-2:])

        if opcode == 99:
            return first_param

        next_pos = JUMP_STEPS[opcode]
        position_mode = True if full_opcode[2] == '1' else False
        immediate_mode = True if full_opcode[1] == '1' else False
        first_param_pos, second_param_pos, third_param_pos = opscode_pos + 1, opscode_pos + 2, opscode_pos + 3

        first_param = integers[first_param_pos] if position_mode else integers[integers[first_param_pos]]
        if opcode in [1, 2, 5, 6, 7, 8]:
            second_param = integers[second_param_pos] if immediate_mode else integers[integers[second_param_pos]]
            third_param = integers[third_param_pos] 

        if opcode == 1:
            integers[third_param] = first_param + second_param
        elif opcode == 2:
            integers[third_param] = first_param * second_param
        elif opcode == 3:
            # opcode 3 takes a single integer as input and saves it 
            # to the position given by its only param (first param)
            integers[integers[first_param_pos]] = input_id
        elif opcode == 5:
            if first_param != 0:
               opscode_pos = second_param
        elif opcode == 6:
            if first_param == 0:
               opscode_pos = second_param
        elif opcode == 7:
            if first_param < second_param:
                integers[third_param_pos] = 1
            else:
                integers[third_param_pos] = 0
        elif opcode == 8:
            if first_param == second_param:
                integers[third_param_pos] = 1
            else:
                integers[third_param_pos] = 0
            
        if opcode not in [5, 6]:
            opscode_pos += next_pos

    return first_param


def answer(problem_input, level, test=False):
    return run(problem_input, level)


aoc_utils.run(answer, cases)
