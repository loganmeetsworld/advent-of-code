from aoc_utils import aoc_utils
from tests import cases


def track_rates(binaries):
    tracker = ''

    for vertical_slice in zip(*binaries):
        if sum([int(i) for i in vertical_slice]) >= (len(binaries) / 2):
            tracker += '1'
        else:
            tracker += '0'

    return tracker


def life_support_rate(tracker, binaries):
    print("BALH")


def answer(problem_input, level, test=False):
    binaries = [l for l in problem_input.splitlines()]
    tracker = track_rates(binaries)
    inverse_tracker = ''.join('1' if x == '0' else '0' for x in tracker)
    if level == 1:
        return int(tracker, 2) * int(inverse_tracker, 2)
    elif level == 2:
        return life_support_rate(tracker, binaries)


aoc_utils.run(answer, cases)
