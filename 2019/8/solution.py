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


def draw(layers, width, height, test):
    canvas = ['2'] * (width * height)
    layer_level = 0

    while layer_level < len(layers):
        for idx, pixel in enumerate(canvas):
            if pixel == '2':
                canvas[idx] = layers[layer_level][idx]
        layer_level += 1

    if test: return ''.join(canvas)

    for c in chunks(''.join(canvas), width):
        c = c.replace('1', '#').replace('0', ' ')
        print(c)

    # answer from the canvas
    return input()


def answer(problem_input, level, test=False):
    if test:
        dimensions, image = problem_input
        width, height = dimensions
    else:
        image, width, height = problem_input, 25, 6

    layers = list(chunks(image, width * height))
    if level == 1: return count_least_zeros(layers)
    elif level == 2: return draw([list(l) for l in layers], width, height, test)



aoc_utils.run(answer, cases)
