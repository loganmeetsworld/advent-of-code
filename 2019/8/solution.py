from collections import Counter

from aoc_utils import aoc_utils
from tests import cases

WIDTH = 25
HEIGHT = 6

def chunks(string, n):
    for i in range(0, len(string), n): yield string[i:i + n]


def count_least_zeros(layers):
    counters = [Counter(l) for l in layers]
    least_zero = [c for c in counters if c['0'] == min(c['0'] for c in counters)][0]
    
    return least_zero['1'] * least_zero['2']


def draw(picture):
    # TODO: do this part
    return 0


def answer(problem_input, level, test=False):
    layers = list(chunks(problem_input, WIDTH * HEIGHT))
    if level == 1: return count_least_zeros(layers)
    elif level == 2: return draw(problem_input)



aoc_utils.run(answer, cases)
