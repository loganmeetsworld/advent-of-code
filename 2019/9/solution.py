from aoc_utils import aoc_utils
from tests import cases


class Intcode:
    def __init__(self, integers, inputs=[]):
        self.integers = integers.copy() + [0] * 10000
        self.inputs = inputs
        self.opcode_pos = 0
        self.relative_base = 0
        self.jump_steps = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}

    def build_opcode(self):
        full_opcode = str(self.integers[self.opcode_pos]).zfill(5)
        return int(full_opcode[-2:])

    def build_params(self, opcode):
        first_param, second_param, third_param = None, None, None
        if opcode == 99:
            return first_param, second_param, third_param
        full_opcode = str(self.integers[self.opcode_pos]).zfill(5)

        if full_opcode[2] == '0':
            first_param = self.integers[self.opcode_pos + 1]
        elif full_opcode[2] == '1':
            first_param = self.opcode_pos + 1
        elif full_opcode[2] == '2':
            first_param = self.integers[self.opcode_pos + 1] + self.relative_base

        if opcode in [1, 2, 7, 8, 5, 6]:
            if full_opcode[1] == '0':
                second_param = self.integers[self.opcode_pos + 2]
            elif full_opcode[1] == '1':
                second_param = self.opcode_pos + 2
            elif full_opcode[1] == '2':
                second_param = self.integers[self.opcode_pos + 2] + self.relative_base

        if opcode in [1, 2, 7, 8]:
            if full_opcode[0] == '0':
                third_param = self.integers[self.opcode_pos + 3]
            elif full_opcode[0] == '1':
                third_param = self.opcode_pos + 3
            elif full_opcode[0] == '2':
                third_param = self.integers[self.opcode_pos + 3] + self.relative_base

        return first_param, second_param, third_param

    def run(self):
        while True:
            opcode = self.build_opcode()
            first_param, second_param, third_param = self.build_params(opcode)

            if opcode == 1:
                self.integers[third_param] = self.integers[first_param] + self.integers[second_param]
            elif opcode == 2:
                self.integers[third_param] = self.integers[first_param] * self.integers[second_param]
            elif opcode == 3:
                self.integers[first_param] = self.inputs.pop(0)
            elif opcode == 4:
                return self.integers[first_param]
            elif opcode == 5:
                self.opcode_pos = self.integers[second_param] if self.integers[first_param] != 0 else self.opcode_pos + self.jump_steps[opcode]
            elif opcode == 6:
                self.opcode_pos = self.integers[second_param] if self.integers[first_param] == 0 else self.opcode_pos + self.jump_steps[opcode]
            elif opcode == 7:
                self.integers[third_param] = 1 if self.integers[first_param] < self.integers[second_param] else 0
            elif opcode == 8:
                self.integers[third_param] = 1 if self.integers[first_param] == self.integers[second_param] else 0
            elif opcode == 9:
                self.relative_base += self.integers[first_param]
            elif opcode == 99:
                break

            if opcode in [1, 2, 3, 7, 8, 9]: self.opcode_pos += self.jump_steps[opcode]


def calculate_boost_keycode(program, level):
    intcode_computer = Intcode(program, [level])
    return intcode_computer.run()


def answer(problem_input, level, test=False):
    boost_program = [int(i) for i in problem_input.split(',')]
    return calculate_boost_keycode(boost_program, level)


aoc_utils.run(answer, cases)
