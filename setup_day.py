import argparse
import os
import sys


def main(path, year, day):
    day_path = f"{path}/{year}/day-{day}/"
    os.mkdir(day_path)
    os.chdir(day_path)

    test_cases = """cases = [
    {'level': 1, 'input': None, 'output': None},
    {'level': 1, 'input': None, 'output': None},
    {'level': 1, 'input': None, 'output': None},
]"""

    solution = """from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, part):
    return 0


aoc_utils.test_and_submit(answer, cases)"""

    with open("solution.py", "w") as s:
        s.write(solution)

    with open("tests.py", "w") as tc:
        tc.write(test_cases)


if __name__ == '__main__':
    cl = argparse.ArgumentParser(description="This script finds docket ids on NYSCEF.")
    cl.add_argument("--year", required=True, help="the year of AoC we are working with")
    cl.add_argument("--day", required=True, help="the day of AoC we are working with")
    cl.add_argument("--path", required=True)
    args = cl.parse_args()
    sys.exit(main(args.path, args.year, args.day))
