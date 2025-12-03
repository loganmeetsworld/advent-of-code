from aoc_utils import aoc_utils
from tests import cases

def find_largest_joltage(bank, num_batteries):
    total_joltage = ""
    start_index = 0
    for battery in range(num_batteries-1, -1 , -1):
        end_index = len(bank) - battery
        bank_section = bank[start_index:end_index]
        max_in_section = max(bank_section)
        total_joltage += max_in_section
        original_index = bank.index(max_in_section, start_index, end_index)
        start_index = original_index + 1

    return int(total_joltage)

def answer(problem_input, level, test=False):
    banks = problem_input.splitlines()
    output_joltage = 0
    for bank in banks:
        if level == 1:
            output_joltage += find_largest_joltage(bank, 2)
        elif level == 2:
            output_joltage += find_largest_joltage(bank, 12)
    return output_joltage

aoc_utils.run(answer, cases)
