from aoc_utils import aoc_utils
from tests import cases


def bsp(code, arrow, max_range):
    r = [0, max_range]
    for letter in code:
        range_length = (r[1] - r[0] + 1) / 2
        if letter == arrow:
            r[0] += range_length
        else:
            r[1] -= range_length

    return r[0]


def answer(problem_input, level, test=False):
    seat_ids = []
    for boarding_pass in problem_input.splitlines():
        row = bsp(boarding_pass[:7], 'B', 127)
        column = bsp(boarding_pass[7:], 'R', 7)
        seat_ids.append(row * 8 + column)

    max_seat_id = int(max(seat_ids))
    min_seat_id = int(min(seat_ids))
    if level == 1:
        return max_seat_id
    else:
        return list(set(range(min_seat_id, max_seat_id)) - set([int(i) for i in seat_ids]))[0]


aoc_utils.run(answer, cases)
