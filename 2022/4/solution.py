from aoc_utils import aoc_utils
from tests import cases

def process_pair(pair):
    A, B = [elem.split('-') for elem in pair.split(',')]
    A = set(range(int(A[0]), int(A[1]) + 1))
    B = set(range(int(B[0]), int(B[1]) + 1))
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
