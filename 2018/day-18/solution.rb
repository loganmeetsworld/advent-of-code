def find_surrounding_acres(lumberyard, coord)
  xs, ys = (coord[0] - 1..coord[0] + 1).to_a, (coord[1] - 1..coord[1] + 1).to_a
  surrounding_acres_coords = xs.product(ys).select{ |x, y| x>= 0 && y >= 0 && x <= lumberyard.first.length - 1 && y <= lumberyard.length - 1 && coord != [x, y] }
  return surrounding_acres_coords.map{ |x, y| lumberyard[x][y] }
end

def new_state(lumberyard, coord)
  surrounding_acres = find_surrounding_acres(lumberyard, coord)

  case lumberyard[coord[0]][coord[1]]
  when '.' # open
    return surrounding_acres.count('|') >= 3 ? '|' : lumberyard[coord[0]][coord[1]]
  when '|' # tree
    return surrounding_acres.count('#') >= 3 ? '#' : lumberyard[coord[0]][coord[1]]
  when '#' # lumberyard
    return surrounding_acres.count('|') >= 1 && surrounding_acres.count('#') >= 1 ? lumberyard[coord[0]][coord[1]] : '.'
  end
end

def change_state(lumberyard)
  new_lumberyard = Array.new(lumberyard.length)
  new_lumberyard.length.times{ |i| new_lumberyard[i] = Array.new(lumberyard.first.length, nil) }
  lumberyard.each_with_index do |row, i|
    row.each_with_index do |_, j|
      new_lumberyard[i][j] = new_state(lumberyard, [i, j])
    end
  end
  return new_lumberyard
end

def resource_value(wooded_acres, lumberyards); return wooded_acres * lumberyards; end

puts "Part 1:"
lumberyard = File.open('input.txt').readlines.map(&:chomp).map(&:chars)
10.times{ lumberyard = change_state(lumberyard) }
puts resource_value(lumberyard.flatten.count('#'), lumberyard.flatten.count('|'))

# puts "Part 2:"
# lumberyard = File.open('input.txt').readlines.map(&:chomp).map(&:chars)
# 1000000000.times{ |t| lumberyard = change_state(lumberyard); puts t / 1000000000 if t % 10000000 == 0 }
# puts resource_value(lumberyard.flatten.count('#'), lumberyard.flatten.count('|'))