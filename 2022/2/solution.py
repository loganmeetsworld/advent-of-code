from aoc_utils import aoc_utils
from tests import cases

SCORE_GUIDE = {
    'AB': 0,
    'BA': 6,
    'AC': 6,
    'CA': 0,
    'BC': 0,
    'CB': 6,
    'AA': 3,
    'BB': 3,
    'CC': 3
}

TRANSLATE = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

LOSING_PLAYS = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

WINNING_PLAYS = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}


def play_linear(games):
    total_score = 0
    for game in games:
        total_score += SCORE_GUIDE[game[0] + TRANSLATE[game[1]]] + ord(TRANSLATE[game[1]]) - 64

    return total_score


def play_strategy(games):
    total_score = 0
    for game in games:
        if game[1] == 'X':
            choice = LOSING_PLAYS[game[0]]
            total_score += + 3
        elif game[1] == 'Y':
            choice = game[0]
        elif game[1] == 'Z':
            choice = WINNING_PLAYS[game[0]]
            total_score += 6

        total_score += (ord(choice) - 64) 

    return total_score


def answer(problem_input, level, test=False):
    games = [line.split(' ') for line in problem_input.splitlines()]
    return play_linear(games) if level == 1 else play_strategy(games)


aoc_utils.run(answer, cases)
