import copy

from aoc_utils import aoc_utils
from tests import cases


class Console():
    def __init__(self, program):
        self.run_length = 0
        self.accumulator = 0
        self.pointer = 0
        self.instrs = program
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
    for pos, (command, value) in enumerate(program):
        if command in translate.keys():
            new_program = copy.deepcopy(program)
            new_program[pos][0] = translate[command]
            inputs.append(new_program)
    return inputs


def answer(problem_input, level, test=False):
    program = [i.split(' ') for i in problem_input.splitlines()]
    if level == 1:
        console = Console(program)
        console.accumulate()
        return console.accumulator
    else:
        programs = build_inputs(program)
        for program in programs:
            console = Console(program)
            console.accumulate()
            if console.fixed:
                return console.accumulator


aoc_utils.run(answer, cases)
