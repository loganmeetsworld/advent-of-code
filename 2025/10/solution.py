from aoc_utils import aoc_utils
from tests import cases

import re

class Machine():
    def __init__(self, light_diagram, button_wiring_schematic):
        self.state = [0 for _ in range(len(light_diagram))]
        self.desired_state = [1 if char == "#" else 0 if char == '.' else char for char in list(light_diagram)]
        self.fewest_presses = 0
        self.buttons = [b.split(',') for b in button_wiring_schematic]

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

    def play_lights(self):
        lights_matrix = self.build_lights_matrix()
        print(lights_matrix)


def answer(problem_input, level, test=False):
    machine_instruction = problem_input.splitlines()
    total = 0
    for machine_instruction in machine_instruction:
        light_diagram_pattern = re.compile(r'\[([^\]]+)\]')
        light_diagram = light_diagram_pattern.findall(machine_instruction)[0]
        button_wiring_schematic_pattern = re.compile(r'\(([^)]+)\)')
        button_wiring_schematic = button_wiring_schematic_pattern.findall(machine_instruction)
        # joltage_requirements_pattern = re.compile(r'\{([^}]+)\}')
        # joltage_requirements = joltage_requirements_pattern.findall(machine_instruction)
        machine = Machine(light_diagram, button_wiring_schematic)
        machine.play_lights()
        total += machine.fewest_presses

    return total


aoc_utils.run(answer, cases)
