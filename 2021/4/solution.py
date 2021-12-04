import re

from aoc_utils import aoc_utils
from tests import cases


class Board():
    def __init__(self, layout):
        self.tiles = self.parse_board(layout)
        self.winner = False
        self.winning_score = 0

    def parse_board(board):
        numbers = re.findall(r'(\d+)', board)
        return [numbers[i:i + 5] for i in range(0, len(numbers), 5)]

    def play(number):
        # X out number
        print(number)
        # Check for win, set winner to True if winner

    def score_board(self):
        self.winning_score = 0
        # set winning score to all unused tiles


def answer(problem_input, level, test=False):
    parsed_input = problem_input.split("\n\n")
    plays = parsed_input[0].split(',')
    boards = [Board(b) for b in parsed_input[1:]]
    for number in plays:
        for board in boards:
            board.play(number)
            if board.winner:
                return board.winning_score


aoc_utils.run(answer, cases)
