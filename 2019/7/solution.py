import itertools

from aoc_utils import aoc_utils
from tests import cases


class Intcode:
    def __init__(self, integers, inputs):
        self.integers = integers.copy()
        self.inputs = inputs
        self.opcode_pos = 0
        self.jump_steps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

    def run(self, inputs):
        self.inputs += inputs

        while self.opcode_pos < len(self.integers):
            # Get the full five digits of the code even if it isn't filled out, then get the actual opcode
            # which will be 1, 2, 3, 4, 5, 6, 7, or 8
            full_opcode = str(self.integers[self.opcode_pos]).zfill(5)
            opcode = int(full_opcode[-2:])

            # We set the "params" or positions for our three numbers based on their "mode" 
            # If the mode is 0, that's "position mode" and the param position is the number found at the
            # index where the index is the value of the param. If the mode is "1" it is "immediate" mode
            # and just assigned to that number itself
            first_param = self.integers[self.opcode_pos + 1] if full_opcode[2] == '0' else self.opcode_pos + 1
            second_param = self.integers[self.opcode_pos + 2] if full_opcode[1] == '0' else self.opcode_pos + 2
            third_param = self.integers[self.opcode_pos + 3] if full_opcode[0] == '0' else self.opcode_pos + 3

            # Now the rest is just following exactly what the instructions say happens for each opcode
            # being careful for 5 and 6 to only use JUMP_STEPS when we haven't already overwritten the 
            # self.opcode_pos
            if opcode == 1:
                self.integers[third_param] = self.integers[first_param] + self.integers[second_param]
            elif opcode == 2:
                self.integers[third_param] = self.integers[first_param] * self.integers[second_param]
            elif opcode == 3:
                self.integers[first_param] = self.inputs.pop(0)
            elif opcode == 4:
                self.opcode_pos += self.jump_steps[opcode]
                return self.integers[first_param]
            elif opcode == 5:
                self.opcode_pos = self.integers[second_param] if self.integers[first_param] != 0 else self.opcode_pos + self.jump_steps[opcode]
            elif opcode == 6:
                self.opcode_pos = self.integers[second_param] if self.integers[first_param] == 0 else self.opcode_pos + self.jump_steps[opcode]
            elif opcode == 7:
                self.integers[third_param] = 1 if self.integers[first_param] < self.integers[second_param] else 0
            elif opcode == 8:
                self.integers[third_param] = 1 if self.integers[first_param] == self.integers[second_param] else 0
            elif opcode == 99:
                break

            if opcode in [1, 2, 3, 4, 7, 8]:
                self.opcode_pos += self.jump_steps[opcode]


def calculate_thruster_signal(phase_settings, amp_controller_software, level):
    input_signal, input_signals = 0, []
    intcodes = [Intcode(amp_controller_software, [setting]) for setting in phase_settings]
    if level == 2:
        while input_signal is not None:
            input_signals.append(input_signal)
            for intcode in intcodes:
                input_signal = intcode.run([input_signal])
        return max(input_signals)
    else:
        input_signals.append(input_signal)
        for intcode in intcodes:
            input_signal = intcode.run([input_signal])
        return input_signal
    

def calculate_thruster_signal_part_2(amp_controller_software):
    input_signals = []

    for phase_settings in itertools.permutations(range(5, 10)):
        input_signal = 0
        intcodes = [Intcode(amp_controller_software, [setting]) for setting in phase_settings]
        while input_signal is not None:
            input_signals.append(input_signal)
            for intcode in intcodes:
                input_signal = intcode.run([input_signal])

    return max(input_signals)


def answer(problem_input, level, test=False):
    if test:
        phase_settings, amp_controller_software = problem_input
        phase_settings = [int(s) for s in phase_settings.split(',')]
        amp_controller_software = [int(s) for s in amp_controller_software.split(',')]
        thruster_signal = calculate_thruster_signal(phase_settings, amp_controller_software, level)
        return thruster_signal
    else:
        if level == 1:
            max_result = 0
            for perms in itertools.permutations([0, 1, 2, 3, 4]):
                phase_settings = list(perms)
                amp_controller_software = [int(s) for s in problem_input.split(',')]
                result = calculate_thruster_signal(phase_settings, amp_controller_software, level)
                if result > max_result:
                    max_result = result

            return max_result
        else:
            amp_controller_software = [int(s) for s in problem_input.split(',')]
            return calculate_thruster_signal_part_2(amp_controller_software)
            # max_results = []
            # amp_controller_software = [int(s) for s in problem_input.split(',')]
            # for perms in itertools.permutations([5, 6, 7, 8, 9]):
            #     phase_settings = list(perms)
            #     result = calculate_thruster_signal(phase_settings, amp_controller_software, level)
            #     print(result)
            #     max_results += result

            # return max(max_results)


aoc_utils.run(answer, cases)
