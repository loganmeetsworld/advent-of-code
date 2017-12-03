input = 325489
middle_cord = [0, 0]

def create_spiral_hash(num)
  array_dim = Math.sqrt(num).round
  x = y = 0
  next_x, next_y = 0, -1
  coords = Array.new
  coords_hash = Hash.new
  value = 0

  (array_dim ** 2).times do
    if x.abs == y.abs && [next_x,next_y] != [1,0] or x > 0 && y == 1 - x
      next_x, next_y = -next_y, next_x 
    end

    if x.abs > array_dim/2 or y.abs > array_dim/2
      next_x, next_y = -next_y, next_x
      x, y = -y + next_x, x + next_y
    end

    unless value > num
      value = find_surrounding_coords_value([x, y], coords_hash)
    end

    coords << [x, y]
    coords_hash[[x, y]] = value
    x, y = x + next_x, y + next_y
  end
  return coords_hash
end

def find_surrounding_coords_value(coord, coords_hash)
  if coord == [0, 0]
    return 1
  else
    sum = 0
    i, j = coord[0], coord[1]
    surrounding_coords = [
      [i-1, j],
      [i, j-1],
      [i-1, j-1],
      [i+1, j],
      [i, j+1],
      [i+1, j+1],
      [i+1, j-1],
      [i-1, j+1]
    ]

    surrounding_coords.each do |arr|
      if !coords_hash[arr].nil?
        sum += coords_hash[arr]
      end
    end
    return sum
  end
end

def answers(num)
  spiral = create_spiral_hash(num)
  return [spiral.keys[num - 1], spiral.values[num - 1]]
end


def find_shorest_distance(point1, point2)
  (point1[0] - point2[0]).abs + (point1[1] - point2[1]).abs
end

middle_cord = [0, 0]
answers = answers(input)
point = answers.first
next_largest_value_part_2 = answers.last

puts find_shorest_distance(middle_cord, point)
puts next_largest_value_part_2