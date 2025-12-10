from aoc_utils import aoc_utils
from tests import cases

import re
import copy
from collections import deque

class Machine():
    def __init__(self, light_diagram, button_wiring_schematic, joltage_requirements):
        self.state = [0 for _ in range(len(light_diagram))]
        self.desired_state = [1 if char == "#" else 0 if char == '.' else char for char in list(light_diagram)]
        self.fewest_presses = 0
        self.buttons = [b.split(',') for b in button_wiring_schematic]
        self.target_joltages = [int(i) for i in joltage_requirements[0].split(',')]

    def play_lights(self):
        lights_matrix = self.build_lights_matrix()
        matrix_original = copy.deepcopy(lights_matrix)
        pivot_cols = self.gaussian_elimination_gf2(lights_matrix)
        min_presses, solution = self.find_minimum_presses(matrix_original, pivot_cols)
        self.fewest_presses = min_presses
        print(f"Min presses: {min_presses}")
        print(f"Solution: {solution}")

    def build_lights_matrix(self):
        n_lights = len(self.desired_state)
        n_buttons = len(self.buttons)
        lights_matrix = [[0] * (n_buttons + 1) for _ in range(n_lights)]
        for button_idx, button in enumerate(self.buttons):
            for light_idx in button:
                lights_matrix[int(light_idx)][button_idx] = 1
        
        for light_idx in range(n_lights):
            lights_matrix[int(light_idx)][n_buttons] = self.desired_state[light_idx]
        
        return lights_matrix
    
    def gaussian_elimination_gf2(self, lights_matrix):
        n_rows = len(lights_matrix)
        n_cols = len(lights_matrix[0]) - 1
        
        pivot_row = 0
        pivot_cols = []
        
        for col in range(n_cols):
            found_pivot = False
            for row in range(pivot_row, n_rows):
                if lights_matrix[row][col] == 1:
                    lights_matrix[pivot_row], lights_matrix[row] = lights_matrix[row], lights_matrix[pivot_row]
                    found_pivot = True
                    pivot_cols.append(col)
                    break
            
            if not found_pivot:
                continue
            
            for row in range(pivot_row + 1, n_rows):
                if lights_matrix[row][col] == 1:
                    for c in range(len(lights_matrix[0])):
                        lights_matrix[row][c] ^= lights_matrix[pivot_row][c]
            
            pivot_row += 1
        
        return pivot_cols

    def back_substitution_gf2(self, lights_matrix, pivot_cols):
        n_cols = len(lights_matrix[0]) - 1
        solution = [0] * n_cols
        
        for row in lights_matrix:
            if all(row[i] == 0 for i in range(n_cols)) and row[-1] == 1:
                return None
        
        for i in range(len(pivot_cols) - 1, -1, -1):
            pivot_col = pivot_cols[i]
            row = lights_matrix[i]
            
            val = row[-1]
            for col in range(pivot_col + 1, n_cols):
                val ^= (row[col] * solution[col])
            
            solution[pivot_col] = val
        
        return solution

    def find_minimum_presses(self, matrix_original, pivot_cols):    
        n_cols = len(matrix_original[0]) - 1
        free_vars = [col for col in range(n_cols) if col not in pivot_cols]
        
        if not free_vars:
            matrix_copy = copy.deepcopy(matrix_original)
            self.gaussian_elimination_gf2(matrix_copy)
            solution = self.back_substitution_gf2(matrix_copy, pivot_cols)
            if solution is None:
                return None, None
            return sum(solution), solution
        
        min_presses = float('inf')
        best_solution = None
        
        for combo in range(2 ** len(free_vars)):
            matrix_copy = copy.deepcopy(matrix_original)
            self.gaussian_elimination_gf2(matrix_copy)
            
            solution = [0] * n_cols
            for i, free_var in enumerate(free_vars):
                solution[free_var] = (combo >> i) & 1
            
            for i in range(len(pivot_cols) - 1, -1, -1):
                pivot_col = pivot_cols[i]
                row = matrix_copy[i]
                
                val = row[-1]
                for col in range(pivot_col + 1, n_cols):
                    val ^= (row[col] * solution[col])
                
                solution[pivot_col] = val
                
            if self.verify_solution(matrix_original, solution):
                presses = sum(solution)
                if presses < min_presses:
                    min_presses = presses
                    best_solution = solution
        
        return min_presses, best_solution
    
    def verify_solution(self, matrix_original, solution):
        n_rows = len(matrix_original)
        n_cols = len(matrix_original[0]) - 1
        
        for row_idx in range(n_rows):
            result = 0
            for col_idx in range(n_cols):
                result ^= (matrix_original[row_idx][col_idx] * solution[col_idx])
            
            if result != matrix_original[row_idx][-1]:
                return False
        
        return True
    
    def min_button_presses_for_joltage(self):
        start = tuple([0] * len(self.target_joltages))
        target = tuple(self.target_joltages)
        
        if start == target:
            return 0
        
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            state, presses = queue.popleft()
            
            for button in self.buttons:
                new_state = list(state)
                for pos in button:
                    new_state[int(pos)] += 1
                new_state = tuple(new_state)
                
                if new_state == target:
                    print(presses + 1)
                    return presses + 1
                
                if all(new_state[i] <= target[i] for i in range(len(target))):
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, presses + 1))
        return -1


def answer(problem_input, level, test=False):
    machine_instruction = problem_input.splitlines()
    total = 0
    for machine_instruction in machine_instruction:
        light_diagram_pattern = re.compile(r'\[([^\]]+)\]')
        light_diagram = light_diagram_pattern.findall(machine_instruction)[0]
        button_wiring_schematic_pattern = re.compile(r'\(([^)]+)\)')
        button_wiring_schematic = button_wiring_schematic_pattern.findall(machine_instruction)
        joltage_requirements_pattern = re.compile(r'\{([^}]+)\}')
        joltage_requirements = joltage_requirements_pattern.findall(machine_instruction)
        machine = Machine(light_diagram, button_wiring_schematic, joltage_requirements)
        if level == 1:
            machine.play_lights()
            total += machine.fewest_presses
        if level == 2:
            total += machine.min_button_presses_for_joltage()

    return total


aoc_utils.run(answer, cases)
