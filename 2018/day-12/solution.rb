require 'set'

def match_rule(rules, string)
    return rules[string]
end

def transform_garden(current_generation, rules)
  beginging, final = current_generation.min, current_generation.max
  new_garden = Set.new()

  (beginging - 3..final + 4).each do |plot|
    pattern = [-2, -1, 0, 1, 2].map{ |k| current_generation.include?(plot + k) ? '#' : '.' }.join
    if match_rule(rules, pattern)
      new_garden.add(plot)
    end
  end

  return new_garden
end

rules_input = File.open('input.txt').readlines
# rules_input = File.open('test-input.txt').readlines
rules = Hash.new()
rules_input.each do |line|
    plot_pattern, result = line.split(' => ').map(&:chomp)
    rules[plot_pattern] = result
end

initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"
# initial_state = "#..#.#..##......###...###"
garden = initial_state.chars
current_generation = Set.new()
garden.each_with_index{ |plot, idx| current_generation.add(idx) if plot == '#' }

puts "Part 1:"

20.times do
  current_generation = transform_garden(current_generation, rules)
end

puts current_generation.inject(&:+)

current_generation = Set.new()
garden.each_with_index{ |plot, idx| current_generation.add(idx) if plot == '#' }

puts "Part 2:"
last_sum = 0
2000.times do |time|
  current_generation = transform_garden(current_generation, rules)
  sum = current_generation.inject(&:+)
  # puts [time, sum, (sum - last_sum)].to_s
  last_sum = sum
end

puts current_generation.inject(&:+) + (50000000000 - 2000) * 55
