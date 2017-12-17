def part1_answer
  steps, current_position, spinlock, value, times_inserted = 335, 0, [0], 1, 2017

  until times_inserted.zero?
    current_position = (current_position + steps) % spinlock.length
    spinlock[current_position + 1] ? spinlock.insert(current_position + 1, value) : spinlock[current_position + 1] = value
    current_position += 1; times_inserted -= 1; value += 1
  end

  spinlock[spinlock.index(2017) + 1]
end

def part2_answer
  steps, current_position, value_after_zero, times_inserted = 335, 0, 0, 1

  until times_inserted == 50_000_000
    current_position = (current_position + steps) % times_inserted
    if current_position == 0 then value_after_zero = times_inserted end
    current_position += 1; times_inserted += 1
  end

  value_after_zero
end

puts "Part 1: #{part1_answer()}"
puts "Part 2: #{part2_answer()}"