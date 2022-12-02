from aoc_utils import aoc_utils
from tests import cases

def answer(problem_input, level, test=False):
    win = 6
    lose = 0
    draw = 3

    play_value = {
        'A': 1,
        'B': 2,
        'C': 3,
    }

    losing_plays = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    winning_plays = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    games = [line.split(' ') for line in problem_input.splitlines()]
    total_score = 0
    for game in games:
        if game[1] == 'Y':
            choice = game[0]
            total_score += play_value[choice] + draw
        if game[1] == 'X':
            choice = losing_plays[game[0]]
            total_score += play_value[choice] + lose
        if game[1] == 'Z':
            choice = winning_plays[game[0]]
            total_score += play_value[choice] + win

    return total_score


aoc_utils.run(answer, cases)
