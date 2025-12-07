from aoc_utils import aoc_utils
from tests import cases

class Manifold():
    def __init__(self, problem_input):
        self.lines = [list(l) for l in problem_input.splitlines()]
        self.split_count = 0

    def print_manifold(self):
        [print(''.join(s)) for s in self.lines]
        print('\n')

    def beam(self):
        for ypos in range(len(self.lines)):
            for xpos in range(len(self.lines[0])):
                x = self.lines[ypos][xpos]
                if ypos + 1 >= len(self.lines):
                    break
                if x == "S":
                    self.lines[ypos + 1][xpos] = "|"
                if x == "|" and self.lines[ypos + 1][xpos] != "^":
                    self.lines[ypos + 1][xpos] = "|"
                if x == "^":
                    self.lines[ypos][xpos - 1] = "|"
                    self.lines[ypos][xpos + 1] = "|"
                    self.lines[ypos + 1][xpos - 1] = "|"
                    self.lines[ypos + 1][xpos + 1] = "|"

    def scan_manifold(self):
        for ypos in range(len(self.lines)):
            for xpos in range(len(self.lines[0])):
                x = self.lines[ypos][xpos]
                if x == "^":
                    if self.lines[ypos - 1][xpos] == "|":
                        self.split_count += 1



def answer(problem_input, level, test=False):
    manifold = Manifold(problem_input)
    manifold.beam()
    manifold.print_manifold()
    manifold.scan_manifold()
    return manifold.split_count


aoc_utils.run(answer, cases)
