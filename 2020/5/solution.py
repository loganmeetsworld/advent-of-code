from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    seat_ids = sorted([int(boarding_pass.translate(str.maketrans("FBLR", "0101")), 2) for boarding_pass in problem_input.splitlines()])
    return seat_ids[-1] if level == 1 else (set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids)).pop()


aoc_utils.run(answer, cases)
