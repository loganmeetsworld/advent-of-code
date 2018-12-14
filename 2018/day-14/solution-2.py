recipes = '607331'
first_elf_pos = 0
second_elf_pos = 1
scoreboard = '37'

while recipes not in scoreboard[-7:]:
    scoreboard += str(int(scoreboard[first_elf_pos]) + int(scoreboard[second_elf_pos]))
    first_elf_steps = int(scoreboard[first_elf_pos]) + 1
    second_elf_steps = int(scoreboard[second_elf_pos]) + 1
    first_elf_pos = (first_elf_pos + first_elf_steps) % len(scoreboard)
    second_elf_pos = (second_elf_pos + second_elf_steps) % len(scoreboard)

print("part 2:")
print(len(scoreboard) - len(recipes))
