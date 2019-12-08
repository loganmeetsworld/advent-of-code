import itertools

from aoc_utils import aoc_utils
from tests import cases

# List of prescriptive jumps we make for a given opcode, this is where we will
# move the instruction pointer after each "test"
JUMP_STEPS = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}


def run(integers, inputs):
    opcode_pos, input_idx = 0, 0

    while integers[opcode_pos] != 99:
        # Get the full five digits of the code even if it isn't filled out, then get the actual opcode
        # which will be 1, 2, 3, 4, 5, 6, 7, or 8
        full_opcode = str(integers[opcode_pos]).zfill(5)
        opcode = int(full_opcode[-2:])

        # We set the "params" or positions for our three numbers based on their "mode" 
        # If the mode is 0, that's "position mode" and the param position is the number found at the
        # index where the index is the value of the param. If the mode is "1" it is "immediate" mode
        # and just assigned to that number itself
        first_param = integers[opcode_pos + 1] if full_opcode[2] == '0' else opcode_pos + 1
        second_param = integers[opcode_pos + 2] if full_opcode[1] == '0' else opcode_pos + 2
        third_param = integers[opcode_pos + 3] if full_opcode[0] == '0' else opcode_pos + 3

        # Now the rest is just following exactly what the instructions say happens for each opcode
        # being careful for 5 and 6 to only use JUMP_STEPS when we haven't already overwritten the 
        # opcode_pos
        if opcode == 1:
            integers[third_param] = integers[first_param] + integers[second_param]
        elif opcode == 2:
            integers[third_param] = integers[first_param] * integers[second_param]
        elif opcode == 3:
            integers[first_param] = inputs[input_idx]
            input_idx += 1
        elif opcode == 5:
            opcode_pos = integers[second_param] if integers[first_param] != 0 else opcode_pos + JUMP_STEPS[opcode]
        elif opcode == 6:
            opcode_pos = integers[second_param] if integers[first_param] == 0 else opcode_pos + JUMP_STEPS[opcode]
        elif opcode == 7:
            integers[third_param] = 1 if integers[first_param] < integers[second_param] else 0
        elif opcode == 8:
            integers[third_param] = 1 if integers[first_param] == integers[second_param] else 0

        if opcode in [1, 2, 3, 4, 7, 8]:
            opcode_pos += JUMP_STEPS[opcode]

    # Our first available param, which should be 0 until the end, should be our output
    return integers[first_param]


def calculate_thruster_signal(phase_settings, amp_controller_software):
    input_signal = 0
    for setting in phase_settings:
        input_signal = run(amp_controller_software, [setting, input_signal])
    
    return input_signal


def answer(problem_input, level, test=False):
    if test:
        phase_settings, amp_controller_software = problem_input
        phase_settings = [int(s) for s in phase_settings.split(',')]
        amp_controller_software = [int(s) for s in amp_controller_software.split(',')]
        thruster_signal = calculate_thruster_signal(phase_settings, amp_controller_software)
        return thruster_signal
    else:
        max_result = 0
        for perms in itertools.permutations([0,1,2,3,4]):
            phase_settings = list(perms)
            amp_controller_software = [int(s) for s in problem_input.split(',')]
            result = calculate_thruster_signal(phase_settings, amp_controller_software)
            if result > max_result:
                max_result = result

        return max_result


aoc_utils.run(answer, cases)
