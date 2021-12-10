import re
from statistics import median

from aoc_utils import aoc_utils
from tests import cases

BRACKET_REGEX = '\(\)|\{\}|\[\]|\<\>'
END_BRACKET_REGEX = '\)|\>|\}|\]'
POINTS = {
    ')': [3, 1],
    ']': [57, 2],
    '}': [1197, 3],
    '>': [25137, 4]
}

def score_incomplete(chunk):
    autocomplete_score = 0
    tr = str.maketrans('(){}<>[]', ')(}{><][')
    for char in list(chunk[::-1].translate(tr)):
        autocomplete_score = (autocomplete_score * 5) + POINTS[char][1]
    return autocomplete_score


def answer(problem_input, level, test=False):
    syntax_scores, autocomplete_scores = [], []
    for chunk in problem_input.splitlines():
        # Remove all adjacent pairs () [] <> {} until none are left
        while True:
            prev_len = len(chunk)
            chunk = re.sub(BRACKET_REGEX, '', chunk)
            if prev_len == len(chunk): break

        # The corrupted ones will include hanging ending brackets ) ] > }
        corrupted = re.search(END_BRACKET_REGEX, chunk)
        if corrupted: 
            syntax_scores.append(POINTS[corrupted.group(0)][0])
        # Incomplete ones have no loose ending brackets and just need to be autocompleted
        else:
            autocomplete_scores.append(score_incomplete(chunk))

    if level == 1:
        return sum(syntax_scores)
    elif level == 2:
        return median(autocomplete_scores)


aoc_utils.run(answer, cases)
