from aoc_utils import aoc_utils
from tests import cases


class Ferry():
    def __init__(self, seating_arrangement):
        self.seats = [list(s) for s in seating_arrangement.splitlines()]
        self.optimal_arrangement = False
        self.occupied_seats = sum([s.count('#') for s in self.seats])

    def print_seats(self):
        [print(''.join(s)) for s in self.seats]
        print('\n')

    def surrounding_count(self, ypos, xpos):
        surrounding_seats = []
        try:
            surrounding_seats = [
                self.seats[ypos - 1][xpos],
                self.seats[ypos][xpos - 1],
                self.seats[ypos - 1][xpos - 1],
                self.seats[ypos + 1][xpos],
                self.seats[ypos][xpos + 1],
                self.seats[ypos + 1][xpos + 1],
                self.seats[ypos + 1][xpos - 1],
                self.seats[ypos - 1][xpos + 1]
            ]
        except IndexError:
            pass

        return surrounding_seats

    def simulate_seat_choices(self):
        for ypos, y in enumerate(self.seats):
            for xpos, x in enumerate(y):
                self.optimal_arrangement = True
                if x == 'L' and self.surrounding_count(ypos, xpos).count('#') == 0:
                    self.seats[ypos][xpos] = '#'
                    self.optimal_arrangement = False

                if x == '#' and self.surrounding_count(ypos, xpos).count('L') >= 4:
                    self.seats[ypos][xpos] = 'L'
                    self.optimal_arrangement = False


def answer(problem_input, level, test=False):
    ferry = Ferry(problem_input)
    ferry.print_seats()
    while True:
        ferry.simulate_seat_choices()
        ferry.print_seats()
        if ferry.optimal_arrangement:
            break

    print(ferry.occupied_seats)
    return ferry.occupied_seats


aoc_utils.run(answer, cases)
