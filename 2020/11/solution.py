import copy

from aoc_utils import aoc_utils
from tests import cases


class Ferry():
    def __init__(self, seating_arrangement, level):
        self.seats = [list(s) for s in seating_arrangement.splitlines()]
        self.optimal_arrangement = False
        self.height = len(self.seats) - 1
        self.width = len(self.seats[0]) - 1
        self.level = level

    def get_occupied_seats(self):
        return sum([s.count('#') for s in self.seats])

    def print_seats(self):
        [print(''.join(s)) for s in self.seats]
        print('\n')

    def left(self, ypos, xpos, steps):
        if 0 <= ypos <= self.height and 0 <= xpos - steps <= self.width:
            return self.seats[ypos][xpos - steps]

    def right(self, ypos, xpos, steps):
        if 0 <= ypos <= self.height and 0 <= xpos + steps <= self.width:
            return self.seats[ypos][xpos + steps]

    def up(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos <= self.width:
            return self.seats[ypos - steps][xpos]

    def down(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos <= self.width:
            return self.seats[ypos + steps][xpos]

    def upright(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos + steps <= self.width:
            return self.seats[ypos - steps][xpos + steps]

    def upleft(self, ypos, xpos, steps):
        if 0 <= ypos - steps <= self.height and 0 <= xpos - steps <= self.width:
            return self.seats[ypos - steps][xpos - steps]

    def downright(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos + steps <= self.width:
            return self.seats[ypos + steps][xpos + steps]

    def downleft(self, ypos, xpos, steps):
        if 0 <= ypos + steps <= self.height and 0 <= xpos - steps <= self.width:
            return self.seats[ypos + steps][xpos - steps]

    def get_adjacent(self, ypos, xpos, steps=1):
        surrounding_seats = []
        for f in [self.up, self.down, self.left, self.right, self.upleft, self.upright, self.downleft, self.downright]:
            seat = f(ypos, xpos, steps)
            if seat:
                surrounding_seats.append(seat)

        return surrounding_seats

    def get_visible(self, ypos, xpos):
        seats = []
        for f in [self.up, self.down, self.left, self.right, self.upleft, self.upright, self.downleft, self.downright]:
            steps = 1
            while True:
                seat = f(ypos, xpos, steps)
                if seat is None:
                    break
                if seat != '.':
                    seats.append(seat)
                    break
                steps += 1
        return seats

    def simulate_seat_choices(self):
        seats_copy = copy.deepcopy(self.seats)
        for ypos, y in enumerate(self.seats):
            for xpos, x in enumerate(y):
                if self.level == 1:
                    if x == 'L' and self.get_adjacent(ypos, xpos).count('#') == 0:
                        seats_copy[ypos][xpos] = '#'

                    if x == '#' and self.get_adjacent(ypos, xpos).count('#') >= 4:
                        seats_copy[ypos][xpos] = 'L'
                else:
                    if x == 'L' and self.get_visible(ypos, xpos).count('#') == 0:
                        seats_copy[ypos][xpos] = '#'

                    if x == '#' and self.get_visible(ypos, xpos).count('#') >= 5:
                        seats_copy[ypos][xpos] = 'L'

        if self.seats == seats_copy:
            self.optimal_arrangement = True
        else:
            self.seats = seats_copy


def answer(problem_input, level, test=False):
    ferry = Ferry(problem_input, level)

    while not ferry.optimal_arrangement:
        ferry.simulate_seat_choices()
        # ferry.print_seats()

    return ferry.get_occupied_seats()


aoc_utils.run(answer, cases)
