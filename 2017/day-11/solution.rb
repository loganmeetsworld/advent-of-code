def calculate_hex_distances(steps)
  directions, moves, max_moves, cardinal_distances = { 'n' => 0, 'e' => 0, 's' => 0, 'w' => 0 }, 0, 0, []

  steps.each do |s|
    if s.length == 1 then directions[s] += 2 else directions[s[0]] += 1; directions[s[1]] += 1 end
    cardinal_distances = [(directions['n'] - directions['s']).abs, (directions['e' ]- directions['w']).abs]
    if cardinal_distances.max > max_moves then max_moves = cardinal_distances.max end
  end

  moves = cardinal_distances.max
  return moves, max_moves
end

steps = File.open('input.txt').read.split(',')
answer = calculate_hex_distances(steps)

puts "Part 1: #{answer.first}"
puts "Part 2: #{answer.last}"