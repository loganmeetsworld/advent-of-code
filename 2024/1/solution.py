from aoc_utils import aoc_utils
from tests import cases


def answer(problem_input, level, test=False):
    if level == 1:
        list_1 = []
        list_2 = []
        total = 0
        for line in problem_input.splitlines():
            num_1, num_2 = line.split('   ')
            list_1.append(num_1)
            list_2.append(num_2)
        
        list_1 = sorted(list_1)
        list_2 = sorted(list_2)
        for i in range(len(list_1)):
            total += abs(int(list_1[i]) - int(list_2[i]))
        return total
    if level == 2:
        similarity_score = 0
        list_1 = []
        list_2 = []
        total = 0
        for line in problem_input.splitlines():
            num_1, num_2 = line.split('   ')
            list_1.append(num_1)
            list_2.append(num_2)

        for i in list_1:
            similarity_score += (list_2.count(i) * int(i))

        return similarity_score

aoc_utils.run(answer, cases)
