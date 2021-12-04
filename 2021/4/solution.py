import re

from aoc_utils import aoc_utils
from tests import cases


class Board():
    def __init__(self, layout):
        self.tiles = self.parse_board(layout)
        self.winner = False
        self.winning_score = 0

    def parse_board(self, layout):
        return [int(i) for i in re.findall(r'(\d+)', layout)]

    def organize_board(self):
        return [self.tiles[i:i + 5] for i in range(0, len(self.tiles), 5)]

    def play(self, number):
        if number in self.tiles:
            self.tiles[self.tiles.index(number)] = 'X'
            self.check_for_win()    

    def row_win(self):
        board = self.organize_board()
        for row in board:
            if len(set(row)) <= 1:
                return True
        return False

    def col_win(self):
        board = self.organize_board()
        columns = zip(*board)
        for column in columns:
            if len(set(column)) <= 1:
                return True
        return False

    def check_for_win(self):
        if self.row_win() or self.col_win():
            self.winner = True

    def score_board(self):
        self.winning_score = sum(filter(lambda n: n != 'X', self.tiles))


def answer(problem_input, level, test=False):
    parsed_input = problem_input.split("\n\n")
    plays = [int(i) for i in parsed_input[0].split(',')]
    boards = [Board(b) for b in parsed_input[1:]]
    for number in plays:
        for board in boards:
            board.play(number)
            if board.winner:
                board.score_board()
                return board.winning_score * number


aoc_utils.run(answer, cases)
