import re

from aoc_utils import aoc_utils
from tests import cases

def word_to_number(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    for i in words:
        number = number.replace(i, str(words.index(i)))
    return number

def answer(problem_input, level, test=False):
    numbers_list = []

    if level == 1:
        for line in problem_input.splitlines():
            numbers = re.findall("\d", line)
            first, last = numbers[0], numbers[-1]
            numbers_list.append(int(first + last))
    elif level == 2:
        for line in problem_input.splitlines():
            numbers = re.findall("(one|two|three|four|five|six|seven|eight|nine|\d)", line)
            numbers_string = ''
            for number in numbers:
                numbers_string += word_to_number(number)
            first, last = numbers_string[0], numbers_string[-1]
            numbers_list.append(int(first + last))

    return sum(numbers_list)            


aoc_utils.run(answer, cases)
