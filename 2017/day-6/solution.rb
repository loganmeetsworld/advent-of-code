memory_banks = File.open("./input.txt").read.split.map(&:to_i)
configurations, count = Hash.new, 0

while configurations[memory_banks.join(',')].nil?
  configurations[memory_banks.join(',')] = count
  max = memory_banks.max
  current_index = memory_banks.index(max)
  memory_banks[current_index] = 0
  max.times do
    current_index = (current_index + 1) % memory_banks.length
    memory_banks[current_index] += 1
  end
  count += 1
end

puts "Part 1: #{configurations.length}"
puts "Part 2: #{count - configurations[memory_banks.join(',')]}"