steps = 335
current_position = 0
times_inserted = 2017
spinlock = [0]
value = 1

until times_inserted == 0
  current_position = (current_position + steps) % spinlock.length
  if spinlock[current_position + 1]
    spinlock.insert(current_position + 1, value)
  else
    spinlock[current_position + 1] = value
  end
  current_position += 1
  times_inserted -= 1
  value += 1
end

puts spinlock[spinlock.index(2017) + 1]