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
        self.threshhold = 3 + level

    def get_occupied_seats(self):
        return sum([s.count('#') for s in self.seats])

    def print_seats(self):
        [print(''.join(s)) for s in self.seats]
        print('\n')

    def get_neighbors(self, ypos, xpos):
        surrounding_seats = []
        if 0 <= ypos <= self.height and 0 <= xpos - 1 <= self.width:
            surrounding_seats.append(self.seats[ypos][xpos - 1])
        if 0 <= ypos <= self.height and 0 <= xpos + 1 <= self.width:
            surrounding_seats.append(self.seats[ypos][xpos + 1])
        if 0 <= ypos - 1 <= self.height and 0 <= xpos <= self.width:
            surrounding_seats.append(self.seats[ypos - 1][xpos])
        if 0 <= ypos + 1 <= self.height and 0 <= xpos <= self.width:
            surrounding_seats.append(self.seats[ypos + 1][xpos])
        if 0 <= ypos - 1 <= self.height and 0 <= xpos + 1 <= self.width:
            surrounding_seats.append(self.seats[ypos - 1][xpos + 1])
        if 0 <= ypos - 1 <= self.height and 0 <= xpos - 1 <= self.width:
            surrounding_seats.append(self.seats[ypos - 1][xpos - 1])
        if 0 <= ypos + 1 <= self.height and 0 <= xpos + 1 <= self.width:
            surrounding_seats.append(self.seats[ypos + 1][xpos + 1])
        if 0 <= ypos + 1 <= self.height and 0 <= xpos - 1 <= self.width:
            surrounding_seats.append(self.seats[ypos + 1][xpos - 1])

        return surrounding_seats

    def get_visible(self, ypos, xpos):
        return []

    def simulate_seat_choices(self):
        seats_copy = copy.deepcopy(self.seats)
        for ypos, y in enumerate(self.seats):
            for xpos, x in enumerate(y):
                surrounding_seats = self.get_neighbors(ypos, xpos) if self.level == 1 else self.get_visible(ypos, xpos)
                if x == 'L' and surrounding_seats.count('#') == 0:
                    seats_copy[ypos][xpos] = '#'

                if x == '#' and surrounding_seats.count('#') >= self.threshhold:
                    seats_copy[ypos][xpos] = 'L'

        if self.seats == seats_copy:
            self.optimal_arrangement = True
        else:
            self.seats = seats_copy


def answer(problem_input, level, test=False):
    ferry = Ferry(problem_input, level)

    while True:
        ferry.simulate_seat_choices()
        # ferry.print_seats()
        if ferry.optimal_arrangement:
            break

    return ferry.get_occupied_seats()


aoc_utils.run(answer, cases)
