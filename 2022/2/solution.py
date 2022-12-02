from aoc_utils import aoc_utils
from tests import cases

def translate_input(lines):
    lookup = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }
    players = []
    for line in lines:
        players.append([line.split(' ')[0], lookup[line.split(' ')[1]]])

    return players

def score_game(game):
    win = 6
    lose = 0
    draw = 3
    score_guide = {
        'A': 1,
        'B': 2,
        'C': 3,
        'AB': lose,
        'BA': win,
        'AC': win,
        'CA': lose,
        'BC': lose,
        'CB': win,
        'AA': draw,
        'BB': draw,
        'CC': draw
    }

    return score_guide[game[1]] + score_guide[''.join(game)]

def answer(problem_input, level, test=False):
    total_score = 0
    games = translate_input(problem_input.splitlines())
    for game in games:
        total_score += score_game(game)
    return total_score


aoc_utils.run(answer, cases)
