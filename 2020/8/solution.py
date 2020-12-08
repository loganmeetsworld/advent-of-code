from aoc_utils import aoc_utils
from tests import cases


class Console():
    def __init__(self, program):
        self.run_length = 0
        self.accumulator = 0
        self.pointer = 0
        self.instrs = [i.split(' ') for i in program.splitlines()]
        self.travel_log = []

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


def answer(problem_input, level, test=False):
    console = Console(problem_input)
    console.accumulate()
    return console.accumulator


aoc_utils.run(answer, cases)
