from aoc_utils import aoc_utils
from tests import cases


def decode(digits, output):
    guide = {}
    one = [d for d in digits.split() if len(d) == 2][0]
    seven = [d for d in digits.split() if len(d) == 3][0]
    four = [d for d in digits.split() if len(d) == 4][0]
    eight = [d for d in digits.split() if len(d) == 7][0]

    # 6, 9, 0
    digits_with_six = [d for d in digits.split() if len(d) == 6]
    nine = [d for d in digits_with_six if all(elem in d for elem in four)][0]
    digits_with_six.remove(nine)
    zero = [d for d in digits_with_six if all(elem in d for elem in one)][0]
    digits_with_six.remove(zero)
    six = digits_with_six[0]

    # 2, 3, 5
    digits_with_five = [d for d in digits.split() if len(d) == 5]
    three = [d for d in digits_with_five if all(elem in d for elem in one)][0]
    digits_with_five.remove(three)
    five = [d for d in digits_with_five if all(elem in six for elem in d)][0]
    digits_with_five.remove(five)
    two = digits_with_five[0]

    guide = {
        ''.join(sorted(zero)): '0',
        ''.join(sorted(one)): '1',
        ''.join(sorted(two)): '2',
        ''.join(sorted(three)): '3',
        ''.join(sorted(four)): '4',
        ''.join(sorted(five)): '5',
        ''.join(sorted(six)): '6',
        ''.join(sorted(seven)): '7', 
        ''.join(sorted(eight)): '8',
        ''.join(sorted(nine)): '9'
    }
    return int(''.join([guide[''.join(sorted(n))] for n in output.split()]))


def answer(problem_input, level, test=False):
    if level == 1:
        outputs, acceptible_lengths = [], [2, 3, 4, 7]
        for line in problem_input.splitlines():
            outputs += line.split(' | ')[1].split()
        return sum(1 for i in outputs if len(i) in acceptible_lengths)
    else:
        return sum([decode(*line.split(' | ')) for line in problem_input.splitlines()])


aoc_utils.run(answer, cases)
