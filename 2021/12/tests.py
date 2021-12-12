TEST_INPUT_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST_INPUT_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

TEST_INPUT_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

cases = [
    {'level': 1, 'input': TEST_INPUT_1, 'output': 10},
    # {'level': 1, 'input': TEST_INPUT_2, 'output': 19},
    # {'level': 1, 'input': TEST_INPUT_3, 'output': 226},
    # {'level': 2, 'input': TEST_INPUT_1, 'output': 0},
]