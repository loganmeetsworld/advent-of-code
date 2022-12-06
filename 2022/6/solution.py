from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    char_count = 4 if level == 1 else 14
    chunk, remaining_buffer = list(problem_input[0:char_count]), list(problem_input[char_count:])
    while len(set(chunk)) != len(chunk):
        char = remaining_buffer.pop(0)
        chunk.pop(0)
        chunk.append(char)
        char_count += 1
    return char_count


aoc_utils.run(answer, cases)
