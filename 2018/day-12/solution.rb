# rules_input = File.open('input.txt').readlines
rules_input = File.open('test-input.txt').readlines

# initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"
initial_state = "#..#.#..##......###...###"

TRANSFORMATION_TIMES = 20

rules = Hash.new()

rules_input.each do |line|
    plot_pattern, result = line.split(' => ').map(&:chomp)
    rules[plot_pattern] = result
end

current_generation = {}
initial_state.chars.each_with_index{ |p, i| current_generation[i] = p }

state_tracker = {
    :current_generation => current_generation,
    :next_generation => {}
}

def transform_garden(state_tracker, rules)
    current_state = state_tracker[:current_generation].values.join
    state_tracker[:current_generation].each do |k, v|

    end
    return state_tracker
end

# garden = '.' * initial_state.length + initial_state + '.' * (2*initial_state.length)
# garden_array = (-initial_state.length..2*initial_state.length)

TRANSFORMATION_TIMES.times do
    state_tracker = transform_garden(state_tracker, rules)
end

puts "Part 1:"
puts state_tracker[:current_generation].values.select{ |v| v == '#' }.count