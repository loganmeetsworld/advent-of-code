import re

from aoc_utils import aoc_utils
from tests import cases

def normalize_numbers(line):
    numbers = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    normalized_numbers = ''
    for number in numbers:
        if number.isnumeric(): 
            normalized_numbers += number
        else:
            normalized_numbers += number.replace(number, str(words.index(number)))
    return normalized_numbers

def answer(problem_input, level, test=False):
    numbers_list = []
    for line in problem_input.splitlines():
        if level == 1:
            numbers = re.findall("\d", line)
        elif level == 2:
            numbers = normalize_numbers(line)
        first, last = numbers[0], numbers[-1]
        numbers_list.append(int(first + last))
 
    return sum(numbers_list)


aoc_utils.run(answer, cases)
