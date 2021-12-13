import re

from aoc_utils import aoc_utils
from tests import cases


class Paper():
    def __init__(self, dots, folds):
        self.dots = dots
        self.folds = folds

    def fold(self, times):
        for direction, length in self.folds[0:times]:
            if direction == 'y':
                new_dots = []
                top_half = self.dots[:int(length)]
                bottom_half = self.dots[int(length) + 1:]
                flipped_bottom = list(reversed(bottom_half))
                for idx in range(len(top_half)):
                    new_line = []
                    for k, m in zip(top_half[idx], flipped_bottom[idx]):
                        if m == '#' or k == '#':
                            new_line.append('#')
                        else:
                            new_line.append('.')
                    new_dots.append(new_line)
                self.dots = new_dots
            elif direction == 'x':
                new_dots = []
                for x in self.dots:
                    right = x[0:int(length)]
                    flipped_left = list(reversed(x[int(length) + 1:]))
                    new_line = []
                    for i, j in zip(right, flipped_left):
                        if i == '#' or j == '#':
                            new_line.append('#')
                        else:
                            new_line.append('.')
                    new_dots.append(new_line)
                self.dots = new_dots

    def get_visible(self):
        return sum([l.count('#') for l in self.dots])

    def print_dots(self):
        [print("".join(['\033[1m' + str(i) + '\033[0m' if i == '#' else str(i) for i in line])) for line in self.dots]
        print()

def create_dot_map(dot_locations):
    width = max(i[0] for i in dot_locations) + 1
    height = max(i[1] for i in dot_locations) + 1
    grid = []
    [grid.append(['.'] * width) for _ in range(height)]
            
    for x, y in dot_locations:
        grid[y][x] = "#"

    return grid


def answer(problem_input, level, test=False):
    dot_locations, fold_instructions = problem_input.split("\n\n")
    dots = create_dot_map([[int(i) for i in l.split(',')] for l in dot_locations.splitlines()])
    folds = folds = re.findall('(\w+)=(\d+)', fold_instructions)
    paper = Paper(dots, folds)
    if level == 1:
        paper.print_dots()
        paper.fold(1)
        paper.print_dots()
    return paper.get_visible()


aoc_utils.run(answer, cases)
