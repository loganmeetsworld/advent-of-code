input = 325489
middle_cord = [0, 0]

def create_spiral(num)
  array_dim = Math.sqrt(num).round
  x = y = 0
  dx, dy = 0, -1
  coords = Array.new
  coords_hash = Hash.new
  value = nil

  (array_dim ** 2).times do
    if x.abs == y.abs && [dx,dy] != [1,0] or x > 0 && y == 1 - x
      dx, dy = -dy, dx 
    end

    if x.abs > array_dim/2 or y.abs > array_dim/2
      dx, dy = -dy, dx
      x, y = -y + dx, x + dy
    end

    if value == nil
      value = 1
    elsif value > num
      value = value
    else
      value = find_surrounding_coords_value([x, y], coords_hash)
    end

    coords << [x, y]
    coords_hash[[x, y]] = value
    x, y = x + dx, y + dy
  end
  return coords_hash
end

def find_surrounding_coords_value(coord, coords_hash)
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

def answer(num)
  spiral = create_spiral(num)
  return [spiral.keys[num - 1], spiral.values[num - 1]]
end


def find_shorest_distance(point1, point2)
  (point1[0] - point2[0]).abs + (point1[1] - point2[1]).abs
end

middle_cord = [0, 0]
answer = answer(input)
point = answer.first
value = answer.last

puts find_shorest_distance(middle_cord, point)
puts value