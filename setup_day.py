import argparse
import os
import sys

def main(path, year, day):
    day_path = f"{path}/{year}/day-{day}/"
    os.mkdir(day_path)
    os.chdir(day_path)

    python_code = """from aoc_utils import aoc_utils

def answer(problem_input, part):
    print(problem_input)
    # TODO: Put your answer here :)

test_cases = [
    {'level': 1, 'input': '', 'output': ''},
    {'level': 1, 'input': '', 'output': ''},
    {'level': 1, 'input': '', 'output': ''},
]
problem_input = aoc_utils.fetch_and_save()
aoc_utils.test_and_submit(test_cases, problem_input, answer)
    """

    with open("solution.py", "w") as solution:
        solution.write(python_code)

if __name__ == '__main__':
    cl = argparse.ArgumentParser(description="This script finds docket ids on NYSCEF.")
    cl.add_argument("--year", required=True, help="the year of AoC we are working with")
    cl.add_argument("--day", required=True, help="the day of AoC we are working with")
    cl.add_argument("--path", required=True)
    args = cl.parse_args()
    sys.exit(main(args.path, args.year, args.day))
