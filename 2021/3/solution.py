from aoc_utils import aoc_utils
from tests import cases


def part_1(binaries):
    new_binary = ''

    # Zip all the lists of bits and iterate through their indexes
    for vertical_bits in zip(*binaries):
        # If the sum of that vertical slice of bits is more than half the length of the list, it's more 1s than 0s
        if sum([int(bit) for bit in vertical_bits]) >= len(binaries) / 2:
            new_binary += '1'
        else:
            new_binary += '0'

    # epsilon is just the reverse of gamma so replace all 1s and 0s and multiply the two
    return int(new_binary, 2) * int(''.join('1' if x == '0' else '0' for x in new_binary), 2)


def part_2(binaries, dominant, non_dominant):
    # For the length of each column
    for idx in range(len(binaries[0])):
        # Sum all the ones in that column
        ones_count = sum([int(i) for i in list(zip(*binaries))[idx]])
        
        # If more than half are ones
        if ones_count >= len(binaries) / 2:
            # Filter the binary strings out so  you only the "dominant" (0,1) trait in that column
            binaries = list(filter(lambda x: x[idx] == dominant, binaries))
        else:
            # If more than half are zeroes, use the non_dominant trait
            binaries = list(filter(lambda x: x[idx] == non_dominant, binaries))

        # Regardless of where we are, if there is only one left, break
        if len(binaries) == 1: break

    return int(binaries[0], 2)


def answer(problem_input, level, test=False):
    binaries = [binary for binary in problem_input.splitlines()]
    if level == 1:
        return part_1(binaries)
    elif level == 2:
        return part_2(binaries, '1', '0') * part_2(binaries, '0', '1')


aoc_utils.run(answer, cases)
