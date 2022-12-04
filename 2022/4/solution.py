from aoc_utils import aoc_utils
from tests import cases

def process_pair(pair):
    pair = [elem.split('-') for elem in pair.split(',')]
    A = set(range(int(pair[0][0]), int(pair[0][1]) + 1))
    B = set(range(int(pair[1][0]), int(pair[1][1]) + 1))
    return A, B


def answer(problem_input, level, test=False):
    count = 0
    for pair in problem_input.splitlines():
        A, B = process_pair(pair)
        if level == 1:
            if A.issuperset(B) or B.issuperset(A): count += 1
        elif level == 2:
            if A.intersection(B): count += 1
    return count


aoc_utils.run(answer, cases)
