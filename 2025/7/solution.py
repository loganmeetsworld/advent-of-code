from aoc_utils import aoc_utils
from tests import cases
import collections

class Manifold():
    def __init__(self, problem_input):
        self.lines = problem_input.splitlines()
        self.split_count = 0
        self.beams = collections.defaultdict(int)

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
        self.beams[self.lines[0].index("S")] = 1
        for ypos in range(len(self.lines)-1):
            for xpos, count in list(self.beams.items()):
                x = self.lines[ypos + 1][xpos]
                if x == "^":
                    self.beams[xpos-1] += count
                    self.beams[xpos+1] += count
                    del self.beams[xpos]
                    self.split_count += 1



def answer(problem_input, level, test=False):
    manifold = Manifold(problem_input)
    # manifold.beam()
    # manifold.print_manifold()
    manifold.scan_manifold()
    if level == 1:
        return manifold.split_count
    else:
        return sum(manifold.beams.values())


aoc_utils.run(answer, cases)
