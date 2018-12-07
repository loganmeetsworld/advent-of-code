import networkx as nx
import re

graph = nx.DiGraph()
lines = open('input.txt', 'r').read().strip().splitlines()
steps = [re.findall(r'\s(\w{1})\s', line) for line in lines]
[graph.add_edge(step[0], step[1]) for step in steps]
sorted_steps = nx.lexicographical_topological_sort(graph)

print('Part 1:')
print(''.join(sorted_steps))
