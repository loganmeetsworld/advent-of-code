from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    numbers = [int(i) for i in problem_input.split(',')]
    tracker = {}
    for i, n in enumerate(numbers):
        tracker[n] = i + 1

    for turn in range(4, 2021):
        # print(f'turn: {turn}')
        play = numbers[-1]
        # print(f'play: {play}')
        # print(f'tracker before: {tracker}')
        # print(f'numbers before: {numbers}')
        if tracker.get(play):
            numbers.append(turn - 1 - tracker[play])
        else:
            numbers.append(0)
        # print(f'changing tracker at {play}, to {turn - 1}')
        tracker[play] = turn - 1
        # print(f'tracker after: {tracker}')
        # print(f'numbers: {numbers}')

    return numbers[-1]


aoc_utils.run(answer, cases)
