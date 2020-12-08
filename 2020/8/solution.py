import copy

from aoc_utils import aoc_utils
from tests import cases


class Console():
    def __init__(self, program):
        self.run_length = 0
        self.accumulator = 0
        self.pointer = 0
        self.instrs = [i.split(' ') for i in program.splitlines()]
        self.travel_log = []
        self.fixed = False

    def translate(self):
        self.travel_log.append(self.pointer % len(self.instrs))
        command, value = self.instrs[self.pointer % len(self.instrs)]
        if command == 'acc':
            self.accumulator += int(value)
            self.pointer += 1
        elif command == 'nop':
            self.pointer += 1
        elif command == 'jmp':
            self.pointer += int(value)

        self.run_length += 1

    def accumulate(self):
        while self.pointer not in self.travel_log:
            self.translate()
            if self.pointer == len(self.instrs):
                self.fixed = True
                break


def build_inputs(program):
    inputs = []
    translate = {'jmp': 'nop', 'nop': 'jmp'}
    program = [i.split(' ') for i in program.splitlines()]
    for pos, (command, value) in enumerate(program):
        p = copy.copy(program)
        if command == 'jmp' or command == 'nop':
            p[pos][0] = translate[command]
        inputs.append('\n'.join([' '.join(i) for i in p]))
    return inputs


def answer(problem_input, level, test=False):
    if level == 1:
        console = Console(problem_input)
        console.accumulate()
        return console.accumulator
    else:
        possible_inputs = build_inputs(problem_input)
        for i in possible_inputs:
            console = Console(i)
            console.accumulate()
            if console.fixed:
                return console.accumulator


aoc_utils.run(answer, cases)
