import sys
sys.path.append('../../')
from aoc_automation import problem_input, submit
import os

part_1_tests_passed = False
part_2_tests_passed = False
problem_path = os.path.abspath(__file__)
problem_input = problem_input(problem_path)

answer_1 = ''
answer_2 = ''

if part_1_tests_passed:
  submit(problem_path, "1", answer_1)

if part_2_tests_passed:
  submit(problem_path, "2", answer_2)
