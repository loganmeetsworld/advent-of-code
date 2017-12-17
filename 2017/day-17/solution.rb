def answer(times_inserted)
  steps, current_position, spinlock, value = 335, 0, [0], 1

  until times_inserted.zero?
    current_position = (current_position + steps) % spinlock.length
    spinlock[current_position + 1] ? spinlock.insert(current_position + 1, value) : spinlock[current_position + 1] = value
    current_position += 1; times_inserted -= 1; value += 1
    puts 'hi' if times_inserted % 10_000_000 == 0
  end

  spinlock[spinlock.index(2017) + 1]
end

times_inserted_p1 = 2017
times_inserted_p2 = 50_000_000

puts "Part 1: #{answer(times_inserted_p1)}"
puts "Part 2: #{answer(times_inserted_p2)}"