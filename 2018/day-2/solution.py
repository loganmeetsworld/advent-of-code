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

print("Part 2:")
# inspired by https://github.com/petertseng/adventofcode-rb-2018/blob/master/02_inventory_management.rb#L20-L26

seen = []
for box in inp:
    for idx, letter in enumerate(box):
        pair = [box[0:idx], box[(idx + 1):-1]]
        if pair in seen:
            print(''.join(pair))
        seen.append(pair)
