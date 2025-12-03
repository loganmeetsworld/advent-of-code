from aoc_utils import aoc_utils
from tests import cases

def find_max_joltage(bank):
    max_joltage = max(bank[0:-1])
    index_max_joltage = bank.index(max_joltage)
    remaining_bank = bank[index_max_joltage+1:len(bank)]
    return int(max_joltage + max(remaining_bank))

def answer(problem_input, level, test=False):
    banks = problem_input.splitlines()
    output_joltage = 0
    for bank in banks:
        output_joltage += find_max_joltage(bank)
    return output_joltage

aoc_utils.run(answer, cases)
