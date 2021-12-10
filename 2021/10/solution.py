import re

from aoc_utils import aoc_utils
from tests import cases

BRACKET_REGEX = '\(\)|\{\}|\[\]|\<\>'
END_BRACKET_REGEX = '\)|\>|\}|\]'
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def answer(problem_input, level, test=False):
    total_score = 0
    for chunk in problem_input.splitlines():
        while True:
            prev_len = len(chunk)
            chunk = re.sub(BRACKET_REGEX, '', chunk)
            if prev_len == len(chunk):
                break

        r = re.search('\)|\>|\}|\]', chunk)
        if r: total_score += POINTS[r.group(0)]
        
    return total_score


aoc_utils.run(answer, cases)
