import re

from aoc_utils import aoc_utils
from tests import cases


class Ferry():
    def __init__(self, level):
        self.level = level
        self.position = [0, 0]
        self.waypoint = [-1, 10]
        self.directions = ['E', 'S', 'W', 'N']

    def get_distance_traveled(self):
        return sum([abs(i) for i in self.position])

    def navigate(self, action, amount):
        if action == 'F':
            if self.level == 1:
                action = self.directions[0]
            else:
                self.position[0] += (self.waypoint[0] * amount)
                self.position[1] += (self.waypoint[1] * amount)
        if action == 'N':
            if self.level == 1:
                self.position[0] -= amount
            else:
                self.waypoint[0] -= amount
        if action == 'S':
            if self.level == 1:
                self.position[0] += amount
            else:
                self.waypoint[0] += amount
        if action == 'E':
            if self.level == 1:
                self.position[1] += amount
            else:
                self.waypoint[1] += amount
        if action == 'W':
            if self.level == 1:
                self.position[1] -= amount
            else:
                self.waypoint[1] -= amount
        if action == 'R':
            if self.level == 1:
                self.directions = self.directions[int(amount / 90):] + self.directions[:int(amount / 90)]
            else:
                if amount == 90:
                    self.waypoint = [self.waypoint[1], -self.waypoint[0]]
                elif amount == 270:
                    self.waypoint = [-self.waypoint[1], self.waypoint[0]]
                elif amount == 180:
                    self.waypoint = [-self.waypoint[0], -self.waypoint[1]]
        if action == 'L':
            if self.level == 1:
                self.directions = self.directions[-int(amount / 90):] + self.directions[:-int(amount / 90)]
            else:
                if amount == 90:
                    self.waypoint = [-self.waypoint[1], self.waypoint[0]]
                elif amount == 270:
                    self.waypoint = [self.waypoint[1], -self.waypoint[0]]
                elif amount == 180:
                    self.waypoint = [-self.waypoint[0], -self.waypoint[1]]


def answer(problem_input, level, test=False):
    ferry = Ferry(level)
    for move in problem_input.splitlines():
        match = re.match(r'([NSEWLRF])(\d+)', move)
        action, amount = match[1], int(match[2])
        ferry.navigate(action, amount)

    return ferry.get_distance_traveled()


aoc_utils.run(answer, cases)
