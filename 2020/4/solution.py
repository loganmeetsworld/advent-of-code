import re

from aoc_utils import aoc_utils
from tests import cases

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_fields(atts):
    return [a for a in atts if len(list(set(REQUIRED_FIELDS) - set(a.keys()))) == 0]


def invalid_hgt(h):
    if h.endswith('cm'):
        return int(h.split('cm')[0]) < 150 or int(h.split('cm')[0]) > 193

    if h.endswith('in'):
        return int(h.split('in')[0]) < 59 or int(h.split('in')[0]) > 76

    return True


def valid_passport(e):
    if int(e['byr']) < 1920 or int(e['byr']) > 2002:
        return False

    if int(e['iyr']) < 2010 or int(e['iyr']) > 2020:
        return False

    if int(e['eyr']) < 2020 or int(e['eyr']) > 2030:
        return False

    if invalid_hgt(e['hgt']):
        return False

    if not re.match('#[0-9a-f]{6}', e['hcl']):
        return False

    if e['ecl'] not in VALID_EYE_COLORS:
        return False

    if not re.match('^\d{9}$', e['pid']):
        return False

    return True


def answer(problem_input, level, test=False):
    passports = []
    for passport in problem_input.split('\n\n'):
        data = {}
        for field in passport.replace('\n', ' ').split(' '):
            data[field.split(':')[0]] = field.split(':')[1]
        passports.append(data)

    complete_passports = valid_fields(passports)
    return len(complete_passports) if level == 1 else len([e for e in complete_passports if valid_passport(e)])


aoc_utils.run(answer, cases)
