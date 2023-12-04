from aoc_utils import aoc_utils
from tests import cases

import re


def answer(problem_input, level, test=False):
    all_points = 0
    for card in problem_input.splitlines():
        my_numbers, winning_numbers = [re.findall("\d+", n) for n in card.split(':')[1].split('|')]
        win_count = len(set(my_numbers) & set(winning_numbers))
        if win_count > 0:
            points = 1
            for i in range(1, win_count):
                points *= 2
                
            all_points += points

    return all_points


aoc_utils.run(answer, cases)
