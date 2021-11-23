import argparse
import os
import sys


def main(year):
    path = os.getcwd()
    year_path = f"{path}/{year}"
    os.mkdir(year_path)
    os.chdir(year_path)

    for day in range(1, 25):
        day_path = f"{path}/{year}/{day}/"
        os.mkdir(day_path)
        os.chdir(day_path)

        test_cases = """cases = [
    {'level': 1, 'input': None, 'output': None},
]"""

        solution = """from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    return 0


aoc_utils.run(answer, cases)
"""

        with open("solution.py", "w") as s:
            s.write(solution)

        with open("tests.py", "w") as tc:
            tc.write(test_cases)

        os.chdir(year_path)


if __name__ == '__main__':
    cl = argparse.ArgumentParser(description="This script generates python templates for each AoC day.")
    cl.add_argument("--year", required=True, help="the year of AoC we are working with")
    args = cl.parse_args()
    sys.exit(main(args.year))
