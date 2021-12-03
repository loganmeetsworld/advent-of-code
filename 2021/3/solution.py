from aoc_utils import aoc_utils
from tests import cases


def part_1_rates(binaries):
    rate = ''

    # Zip(*binaries) will take the list of lists and organize them by index, creating collections of vertical bits
    for vertical_bits in zip(*binaries):
        # If the sum of the vertical line is more or equal to half the length of the whole list we know that there are more 1s than 0s
        if sum([int(bit) for bit in vertical_bits]) >= (len(binaries) / 2):
            rate += '1'
        else:
            rate += '0'

    return rate

def part_2_rate(binaries):
    binary_length = len(binaries[0])

    for idx in range(binary_length):
        dominant = sum([int(i) for i in list(zip(*binaries))[idx]]) >= len(binaries) / 2
        if dominant:
            binaries = list(filter(lambda x: x[idx] == '1', binaries))
        else:
            binaries = list(filter(lambda x: x[idx] == '0', binaries))

        if len(binaries) == 1:
            break

    return int(binaries[0], 2)

def co2_scrub_rate(binaries):
    binary_length = len(binaries[0])

    for idx in range(binary_length):
        print(binaries)
        dominant = sum([int(i) for i in list(zip(*binaries))[idx]]) >= len(binaries) / 2
        if dominant:
            binaries = list(filter(lambda x: x[idx] == '0', binaries))
        else:
            binaries = list(filter(lambda x: x[idx] == '1', binaries))

        if len(binaries) == 1:
            break


    return int(binaries[0], 2)


def answer(problem_input, level, test=False):
    binaries = [binary for binary in problem_input.splitlines()]
    tracker = part_1_rates(binaries)
    inverse_tracker = ''.join('1' if x == '0' else '0' for x in tracker)
    if level == 1:
        return int(tracker, 2) * int(inverse_tracker, 2)
    elif level == 2:
        return part_2_rate(binaries) * co2_scrub_rate(binaries)


aoc_utils.run(answer, cases)
