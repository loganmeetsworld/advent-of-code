from aoc_utils import aoc_utils
from tests import cases


class RollDiagram():
    def __init__(self, map, level):
        self.spots = [list(s) for s in map.splitlines()]
        self.height = len(self.spots) - 1
        self.width = len(self.spots[0]) - 1
        self.access_spots = 0

    def print_spots(self):
        [print(''.join(s)) for s in self.spots]
        print('\n')

    def left(self, ypos, xpos, steps):
        if 0 <= ypos <= self.height and 0 <= xpos - steps <= self.width:
            return self.spots[ypos][xpos - steps]

    def right(self, ypos, xpos, steps):
        if 0 <= ypos <= self.height and 0 <= xpos + steps <= self.width:
            return self.spots[ypos][xpos + steps]

    def up(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos <= self.width:
            return self.spots[ypos - steps][xpos]

    def down(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos <= self.width:
            return self.spots[ypos + steps][xpos]

    def upright(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos + steps <= self.width:
            return self.spots[ypos - steps][xpos + steps]

    def upleft(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos - steps <= self.width:
            return self.spots[ypos - steps][xpos - steps]

    def downright(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos + steps <= self.width:
            return self.spots[ypos + steps][xpos + steps]

    def downleft(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos - steps <= self.width:
            return self.spots[ypos + steps][xpos - steps]

    def get_adjacent(self, ypos, xpos, steps=1):
        surrounding_spots = []
        for f in [self.up, self.down, self.left, self.right, self.upleft, self.upright, self.downleft, self.downright]:
            spot = f(ypos, xpos, steps)
            if spot:
                surrounding_spots.append(spot)

        return surrounding_spots
    
    def count_access_spots(self):
        for ypos, y in enumerate(self.spots):
            for xpos, x in enumerate(y):
                if self.spots[ypos][xpos] == '@' and self.get_adjacent(ypos, xpos).count("@") < 4:
                    self.access_spots += 1


def answer(problem_input, level, test=False):
    diagram = RollDiagram(problem_input, level)
    diagram.count_access_spots()
    # diagram.print_spots()
    return diagram.access_spots


aoc_utils.run(answer, cases)
