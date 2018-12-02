from collections import Counter

print("Part 1:")
inp = open('input.txt', 'r').read().strip().splitlines()
twos = 0
threes = 0

for box in inp:
    freqs = Counter(list(box))
    if 2 in freqs.values():
        twos += 1
    if 3 in freqs.values():
        threes += 1

print(twos * threes)
