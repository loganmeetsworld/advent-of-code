from aoc_utils import aoc_utils
from tests import cases
import math
from itertools import combinations

def sort_distances(coords):
    distances_with_pairs = []
    for p1, p2 in combinations(coords, 2):
        distance = math.dist(p1, p2)
        distances_with_pairs.append((distance, (p1, p2)))

    distances_with_pairs.sort(key=lambda x: x[0])
    return distances_with_pairs

def answer(problem_input, level, test=False):
    junct_box_coords = [[int(n) for n in l.split(",")] for l in problem_input.splitlines()]
    distances = sort_distances(junct_box_coords)
    if test and level == 1:
        top_distances = distances[0:10]
    elif level == 1:
        top_distances = distances[0:1000]
    else:
        top_distances = distances
    
    circuits = []
    for distance in top_distances:
        coords = distance[1]
        found_in_circuits = []
        for circuit in circuits:
            if str(coords[0]) in circuit or str(coords[1]) in circuit:
                found_in_circuits.append(circuit)
                circuit.add(str(coords[0]))
                circuit.add(str(coords[1]))

        if len(found_in_circuits) > 1:
            mega_circuit = found_in_circuits[0].union(*found_in_circuits[1:])
            for circuit in found_in_circuits:
                circuits.remove(circuit)
            circuits.append(mega_circuit) 
        
        if not found_in_circuits:
            new_circuit = set()
            new_circuit.add(str(coords[0]))
            new_circuit.add(str(coords[1]))
            circuits.append(new_circuit)

        if level == 2 and len(circuits) == 1 and len(circuits[0]) == len(junct_box_coords):
            return coords[0][0] * coords[1][0]

    top_three_longest = sorted(circuits, key=len, reverse=True)[:3]
    return math.prod([len(c) for c in top_three_longest])


aoc_utils.run(answer, cases)
