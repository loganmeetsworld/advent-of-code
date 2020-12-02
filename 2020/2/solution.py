import re

from aoc_utils import aoc_utils
from tests import cases


def validate_rule(rule, level):
    mn, mx, letter, password = list(re.findall(r"(\d+)-(\d+) (\w): (\w+)", rule)[0])
    if level == 1:
        return password.count(letter) >= int(mn) and password.count(letter) <= int(mx)
    elif level == 2:
        return (password[int(mn) - 1] == letter or password[int(mx) - 1] == letter) and not (password[int(mn) - 1] == letter and password[int(mx) - 1] == letter)


def answer(problem_input, level, test=False):
    valid_pw_count = 0
    password_rules = problem_input.splitlines()
    for password_rule in password_rules:
        if validate_rule(password_rule, level):
            valid_pw_count += 1
    return valid_pw_count


aoc_utils.run(answer, cases)
