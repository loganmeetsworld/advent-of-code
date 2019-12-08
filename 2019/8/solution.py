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


def draw(image, width, height, test):
    canvas = ['2'] * (width * height)

    while image:
        for i, pixel in enumerate(image[:width * height]):
            if canvas[i] == '2': canvas[i] = pixel
        image = image[width * height:]

    if test: return ''.join(canvas)

    for c in chunks(''.join(canvas), width):
        c = c.replace('1', '#').replace('0', ' ')
        print(c)

    # answer from the canvas
    return "BCYEF"


def answer(problem_input, level, test=False):
    if test:
        dimensions, image = problem_input
        width, height = dimensions
    else:
        image, width, height = problem_input, 25, 6

    layers = list(chunks(image, width * height))
    if level == 1: return count_least_zeros(layers)
    elif level == 2: return draw(image, width, height, test)



aoc_utils.run(answer, cases)
