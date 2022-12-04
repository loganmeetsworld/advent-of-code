from aoc_utils import aoc_utils
from tests import cases

def process_pair(pair):
    pair = [elem.split('-') for elem in pair.split(',')]
    A = set(range(int(pair[0][0]), int(pair[0][1]) + 1))
    B = set(range(int(pair[1][0]), int(pair[1][1]) + 1))
    return A, B


def answer(problem_input, level, test=False):
    superset_count = 0
    for pair in problem_input.splitlines():
        A, B = process_pair(pair)
        if A.issuperset(B) or B.issuperset(A):
            superset_count += 1

    return superset_count


aoc_utils.run(answer, cases)
