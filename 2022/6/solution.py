from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    datastream_buffer = list(problem_input)
    four_chunk, remaining_buffer = datastream_buffer[0:4], datastream_buffer[4:]
    char_count = 4
    while len(set(four_chunk)) != len(four_chunk):
        popped = remaining_buffer.pop(0)
        four_chunk.pop(0)
        four_chunk.append(popped)
        char_count += 1
    return char_count


aoc_utils.run(answer, cases)
