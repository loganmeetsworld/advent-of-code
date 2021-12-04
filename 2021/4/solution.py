import re

from aoc_utils import aoc_utils
from tests import cases


class Board():
    def __init__(self, layout):
        self.tiles = [int(i) for i in re.findall(r'(\d+)', layout)]
        self.bingo = False

    def partition(self):
        return [self.tiles[i:i + 5] for i in range(0, len(self.tiles), 5)]

    def play(self, number):
        if number in self.tiles:
            self.tiles[self.tiles.index(number)] = 'X'
            self.check_for_win()    

    def check_for_win(self):
        board = self.partition()
        self.bingo = self.check_bingo(board) or self.check_bingo(zip(*board))

    @staticmethod
    def check_bingo(collection):
        for item in collection:
            # Get a set of items in the row or column, if it's length is one, they are all 'X'
            if len(set(item)) <= 1: return True
        return False


def answer(problem_input, level, test=False):
    parsed_input = problem_input.split("\n\n")
    numbers, boards = [int(i) for i in parsed_input[0].split(',')], [Board(b) for b in parsed_input[1:]]
    for number in numbers:
        for board in boards:
            if board.bingo: continue
            board.play(number)
            if board.bingo:
                # If level 1 or everyone has reached bingo, return the score
                if level == 1 or len(set([b.bingo for b in boards])) == 1:
                    return sum(filter(lambda n: n != 'X', board.tiles)) * number


aoc_utils.run(answer, cases)
