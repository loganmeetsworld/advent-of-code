from aoc_utils import aoc_utils
from tests import cases


def orbit_count(orbits):
    for orbit in orbits:
        orbitted, orbitting = orbit.split(')')
        # MAKE A TREE

    return 1


def answer(problem_input, level, test=False):
    orbits = problem_input.splitlines()
    return orbit_count(orbits)


aoc_utils.run(answer, cases)
