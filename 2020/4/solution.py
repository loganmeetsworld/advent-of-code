from aoc_utils import aoc_utils
from tests import cases

REQUIRED_ATTRIBUTES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate_attrs(atts):
    return [a for a in atts if len(list(set(REQUIRED_ATTRIBUTES) - set(a.keys()))) == 0]

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:

# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.


# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def validate_passport(e):
    if int(e['byr']) < 1920 or > 2002:
        return False

    if int(e['iyr']) < 2010 or > 2020:
        return False

    if int(e['eyr']) < 2020 or > 2030:
        return False

    return True

def answer(problem_input, level, test=False):
    elves = []
    for e in problem_input.split("\n\n"):
        edata = {}
        for attribute in e.replace("\n", " ").split(" "):
            edata[attribute.split(':')[0]] = attribute.split(':')[1]
        elves.append(edata)

    complete_passports = validate_attrs(elves)
    if level == 1:
        return len(complete_passports)
    else:
        valid_passports = [e for e in complete_passports if validate_passport(e)]
        return len(valid_passports)


aoc_utils.run(answer, cases)
