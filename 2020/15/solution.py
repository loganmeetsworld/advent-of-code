from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    last_turn = 2020 if level == 1 else 30000000
    numbers = [int(i) for i in problem_input.split(',')]
    tracker = {}
    for i, n in enumerate(numbers):
        tracker[n] = i + 1

    for turn in range(len(numbers), last_turn):
        current_play = numbers[-1]
        if tracker.get(current_play):
            numbers.append(turn - tracker[current_play])
        else:
            numbers.append(0)
        tracker[current_play] = turn

    return numbers[-1]


aoc_utils.run(answer, cases)
