import re
import statistics

from aoc_utils import aoc_utils
from tests import cases

BRACKET_REGEX = '\(\)|\{\}|\[\]|\<\>'
END_BRACKET_REGEX = '\)|\>|\}|\]'
SYNTAX_CHECKER_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def answer(problem_input, level, test=False):
    syntax_score = 0
    autocomplete_scores = []
    for chunk in problem_input.splitlines():
        while True:
            prev_len = len(chunk)
            chunk = re.sub(BRACKET_REGEX, '', chunk)
            if prev_len == len(chunk):
                break

        r = re.search('\)|\>|\}|\]', chunk)
        if r: 
            syntax_score += SYNTAX_CHECKER_POINTS[r.group(0)]
        else:
            print(chunk)
            score = 0
            tr = str.maketrans('(){}<>[]', ')(}{><][')
            reversed_chunk = chunk[::-1].translate(tr)
            print(reversed_chunk)
            for s in list(reversed_chunk):
                score = score * 5
                score += AUTOCOMPLETE_POINTS[s]
            autocomplete_scores.append(score)

    if level == 1:
        return syntax_score
    else:
        return statistics.median(autocomplete_scores)


aoc_utils.run(answer, cases)
