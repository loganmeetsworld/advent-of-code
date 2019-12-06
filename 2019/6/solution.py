from aoc_utils import aoc_utils
from tests import cases


def create_tree(edges):
    tree = {}
    for child, parent in edges:
        tree.setdefault(parent, []).append(child)
        tree.setdefault(child, []).append(parent)
    
    return tree


def orbit_count(edges):
    tree = create_tree(edges)
    print(tree)
  
    return 1


def answer(problem_input, level, test=False):
    edges = problem_input.splitlines()
    return orbit_count([e.split(')') for e in edges])


aoc_utils.run(answer, cases)
