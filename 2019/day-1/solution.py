import sys
sys.path.append('../../')
from aoc_automation import problem_input, submit
import os

problem_input = problem_input(os.path.abspath(__file__))

answer = ''
submit(answer)
