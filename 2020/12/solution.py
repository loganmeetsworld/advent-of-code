import re

from aoc_utils import aoc_utils
from tests import cases


class Ferry():
    def __init__(self):
        self.position = [0, 0]
        self.directions = ['E', 'S', 'W', 'N']

    def get_distance_traveled(self):
        return sum([abs(i) for i in self.position])

    def navigate(self, action, amount):
        if action == 'F':
            action = self.directions[0]
        if action == 'N':
            self.position[0] -= amount
        if action == 'S':
            self.position[0] += amount
        if action == 'E':
            self.position[1] += amount
        if action == 'W':
            self.position[1] -= amount
        if action == 'R':
            self.directions = self.directions[int(amount / 90):] + self.directions[:int(amount / 90)]
        if action == 'L':
            self.directions = self.directions[-int(amount / 90):] + self.directions[:-int(amount / 90)]


def answer(problem_input, level, test=False):
    ferry = Ferry()
    for move in problem_input.splitlines():
        match = re.match(r'([NSEWLRF])(\d+)', move)
        action, amount = match[1], int(match[2])
        ferry.navigate(action, amount)

    return ferry.get_distance_traveled()


aoc_utils.run(answer, cases)
