# rules_input = File.open('input.txt').readlines
rules_input = File.open('test-input.txt').readlines


def match_rule(rules, string)
    return rules[string]
end

def transform_garden(rules, garden, transformation_times)
    transformation_times.times do
        expanded_garden = garden.unshift('.').unshift('.').push('.').push('.')
        garden.each_with_index do |plot, idx|
            if match_rule(rules, expanded_garden.slice(idx, 5).join)
                garden[idx] = match_rule(rules, expanded_garden.slice(idx, 5).join)
            else
                garden[idx] = '.'
            end
        end
    end
end

rules = Hash.new()
rules_input.each do |line|
    plot_pattern, result = line.split(' => ').map(&:chomp)
    rules[plot_pattern] = result
end

# initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"
initial_state = "#..#.#..##......###...###"
garden = initial_state.chars
garden = transform_garden(rules, garden, 3)

puts "Part 1:"
puts garden.select{ |v| v == '#' }.count