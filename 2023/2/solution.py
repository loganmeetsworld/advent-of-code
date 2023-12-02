import re

from aoc_utils import aoc_utils
from tests import cases


def part_one(problem_input):
    game_possibilities = {'red': 12, 'green': 13, 'blue': 14}
    possible_games = []
    for game in problem_input.splitlines():
        game_id = re.findall("Game (\d+):", game)[0]
        possible = True
        just_gameplays = game.split(': ')
        for draw in just_gameplays[1].split('; '):
            for pick in draw.split(', '):
                split_pick = pick.split(' ')
                if int(split_pick[0]) > game_possibilities[split_pick[1]]:
                    possible = False

        if possible:
            possible_games.append(int(game_id))

    return sum(possible_games)



def answer(problem_input, level, test=False):
    if level == 1: 
        return part_one(problem_input)
    else:
        powers = []
        for game in problem_input.splitlines():
            game_map = {'red': 0, 'blue': 0, 'green': 0}
            just_gameplays = game.split(': ')
            for draw in just_gameplays[1].split('; '):
                for pick in draw.split(', '):
                    split_pick = pick.split(' ')
                    if int(split_pick[0]) > game_map[split_pick[1]]:
                        game_map[split_pick[1]] = int(split_pick[0])

            powers.append(game_map['red'] * game_map['blue'] * game_map['green'])
        
        return sum(powers)
            

aoc_utils.run(answer, cases)
