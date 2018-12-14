recipes = 607331
first_elf_pos = 0
second_elf_pos = 1
scoreboard = [3, 7]

for i in range(recipes + 10):
    score = scoreboard[first_elf_pos] + scoreboard[second_elf_pos]
    new_recipes = list(str(score))
    [scoreboard.append(int(r)) for r in new_recipes]
    first_elf_steps = scoreboard[first_elf_pos] + 1
    second_elf_steps = scoreboard[second_elf_pos] + 1
    first_elf_pos = (first_elf_pos + first_elf_steps) % len(scoreboard)
    second_elf_pos = (second_elf_pos + second_elf_steps) % len(scoreboard)

print(''.join([str(x) for x in scoreboard[recipes:recipes + 10]]))
