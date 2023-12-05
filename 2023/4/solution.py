from aoc_utils import aoc_utils
from tests import cases

import re

def calculate_points(problem_input):
    all_points = 0
    for card in problem_input.splitlines():
        my_numbers, winning_numbers = [re.findall("\d+", n) for n in card.split(':')[1].split('|')]
        win_count = len(set(my_numbers) & set(winning_numbers))
        if win_count > 0:
            card_points = 1
            for i in range(1, win_count):
                points *= 2
                
            all_points += card_points

    return all_points


def answer(problem_input, level, test=False):
    if level == 1:
        return calculate_points(problem_input)
    elif level == 2:
        cards = []
        for card in problem_input.splitlines():
            card_number = int(card.split('Card ')[0])
            my_numbers, winning_numbers = [re.findall("\d+", n) for n in card.split(':')[1].split('|')]
            matches = len(set(my_numbers) & set(winning_numbers))
            range(card_number + 1, card_number + matches)


aoc_utils.run(answer, cases)
