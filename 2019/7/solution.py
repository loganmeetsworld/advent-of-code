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

        while True:
            full_opcode = str(self.integers[self.opcode_pos]).zfill(5)
            opcode = int(full_opcode[-2:])
            first_param = self.integers[self.opcode_pos + 1] if full_opcode[2] == '0' else self.opcode_pos + 1
            second_param = self.integers[self.opcode_pos + 2] if full_opcode[1] == '0' else self.opcode_pos + 2
            third_param = self.integers[self.opcode_pos + 3] if full_opcode[0] == '0' else self.opcode_pos + 3

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

            if opcode in [1, 2, 3, 7, 8]: self.opcode_pos += self.jump_steps[opcode]


def calculate_thruster_signal(settings, amp_controller_software, level):
    intcodes = [Intcode(amp_controller_software, [setting]) for setting in settings]
    if level == 1:
        result = 0
        for intcode in intcodes:
            result = intcode.run([result])
        return result
    elif level == 2:
        result, results = 0, []
        while result is not None:
            for intcode in intcodes:
                results.append(result)
                result = intcode.run([result])

        return max(list(filter(lambda a: a != None, results)))


def calculate_max_thruster_signal_part_1(amp_controller_software, level):
    results = []
    for settings in itertools.permutations(range(5)):
        result = calculate_thruster_signal(settings, amp_controller_software, level)
        results.append(result)
    return max(results)


def calculate_max_thruster_signal_part_2(amp_controller_software, level):
    results = []
    for settings in itertools.permutations(range(5,10)):
        result = calculate_thruster_signal(settings, amp_controller_software, level)
        results.append(result)

    return max(results)


def answer(problem_input, level, test=False):
    if test:
        settings, amp_controller_software = problem_input
        settings, amp_controller_software = [int(s) for s in settings.split(',')], [int(s) for s in amp_controller_software.split(',')]
        return calculate_thruster_signal(settings, amp_controller_software, level)
    else:
        amp_controller_software = [int(s) for s in problem_input.split(',')]
        if level == 1:
            return calculate_max_thruster_signal_part_1(amp_controller_software, level)
        elif level == 2:
            return calculate_max_thruster_signal_part_2(amp_controller_software, level)


aoc_utils.run(answer, cases)
