import re

from aoc_utils import aoc_utils
from tests import cases


class Ferry():
    def __init__(self):
        self.position = [0, 0]
        self.waypoint_position = [-1, 10]
        self.directions = ['E', 'S', 'W', 'N']

    def get_distance_traveled(self):
        return sum([abs(i) for i in self.position])

    def handle_cardinal_direction(self, action, amount, pos):
        if action == 'N':
            pos[0] -= amount
        elif action == 'S':
            pos[0] += amount
        elif action == 'E':
            pos[1] += amount
        elif action == 'W':
            pos[1] -= amount

    def navigate_ship_and_waypoint(self, action, amount):
        if action == 'F':
            self.position[0] += (self.waypoint_position[0] * amount)
            self.position[1] += (self.waypoint_position[1] * amount)

        if action in self.directions:
            self.handle_cardinal_direction(action, amount, self.waypoint_position)
        elif action == 'R':
            if amount == 90:
                self.waypoint_position = [self.waypoint_position[1], -self.waypoint_position[0]]
            elif amount == 270:
                self.waypoint_position = [-self.waypoint_position[1], self.waypoint_position[0]]
            elif amount == 180:
                self.waypoint_position = [-self.waypoint_position[0], -self.waypoint_position[1]]
        elif action == 'L':
            if amount == 90:
                self.waypoint_position = [-self.waypoint_position[1], self.waypoint_position[0]]
            elif amount == 270:
                self.waypoint_position = [self.waypoint_position[1], -self.waypoint_position[0]]
            elif amount == 180:
                self.waypoint_position = [-self.waypoint_position[0], -self.waypoint_position[1]]

    def navigate_ship(self, action, amount):
        if action == 'F':
            action = self.directions[0]
        if action in self.directions:
            self.handle_cardinal_direction(action, amount, self.position)
        if action == 'R':
            self.directions = self.directions[int(amount / 90):] + self.directions[:int(amount / 90)]
        if action == 'L':
            self.directions = self.directions[-int(amount / 90):] + self.directions[:-int(amount / 90)]


def answer(problem_input, level, test=False):
    ferry = Ferry()
    for move in problem_input.splitlines():
        match = re.match(r'([NSEWLRF])(\d+)', move)
        action, amount = match[1], int(match[2])
        ferry.navigate_ship(action, amount) if level == 1 else ferry.navigate_ship_and_waypoint(action, amount)

    return ferry.get_distance_traveled()


aoc_utils.run(answer, cases)
