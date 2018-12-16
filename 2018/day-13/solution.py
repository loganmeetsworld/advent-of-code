import collections
import re

def track(lines):
    return [
        l.replace('>', '-').replace('<', '-').replace('^', '|').replace('v', '|')
        for l in lines
    ]

def carts(lines):
    carts = []
    for y, l in enumerate(lines):
        for m in re.finditer(r'[<>v\^]', l):
            carts.append((y, m.start(), m.group(0), 0))
    
    return carts

def find_new_position(y, x, change, k):
    if (y, x) in crashed:
        return
    if change == '>':
        n = (y, x + 1)
    elif change == '<':
        n = (y, x - 1)
    elif change == '^':
        n = (y - 1, x)
    elif change == 'v':
        n = (y + 1, x)
    
    return n


lines = [l.rstrip('\n') for l in open('input.txt', 'r').read().splitlines()]
track = track(lines)
carts = carts(lines)

part_one = False
while True:
    crashed = set()
    for i in range(len(carts)):
        (y, x, change, k) = carts[i]
        if not find_new_position(y, x, change, k):
            continue
        n = find_new_position(y, x, change, k)
        (ny, nx) = n
        if any(ay == ny and ax == nx for (ay, ax, ac, ak) in carts):
            if not part_one:
                print('{},{}'.format(nx, ny))
                part_one = True
            crashed.add(n)
        if track[ny][nx] in '\\/':
            change = {
                '>\\': 'v',
                '<\\': '^',
                '^\\': '<',
                'v\\': '>',
                '>/': '^',
                '</': 'v',
                '^/': '>',
                'v/': '<',
            }[change + track[ny][nx]]
        elif track[ny][nx] == '+':
            change = {
                '>0': '^',
                '>1': '>',
                '>2': 'v',
                '<0': 'v',
                '<1': '<',
                '<2': '^',
                '^0': '<',
                '^1': '^',
                '^2': '>',
                'v0': '>',
                'v1': 'v',
                'v2': '<',
            }[change + str(k)]
            k = (k + 1) % 3
        carts[i] = (ny, nx, change, k)
    else:
        carts = [c for c in carts if (c[0], c[1]) not in crashed]
        if len(carts) == 1:
            print('{},{}'.format(carts[0][1], carts[0][0]))
            break
        carts.sort()
        continue
    break