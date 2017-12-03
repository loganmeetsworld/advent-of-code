input = 325489
middle_cord = [0, 0]

def create_spiral(num)
  array_dim = Math.sqrt(num).round
  x = y = 0
  dx, dy = 0, -1
  coords = Array.new

  (array_dim ** 2).times do
    if x.abs == y.abs && [dx,dy] != [1,0] or x > 0 && y == 1 - x
      dx, dy = -dy, dx 
    end

    if x.abs > array_dim/2 or y.abs > array_dim/2
      dx, dy = -dy, dx
      x, y = -y + dx, x + dy
    end

    coords << [x, y]
    x, y = x + dx, y + dy
  end
  return coords
end

def find_coord(num)
  spiral = create_spiral(num)
  spiral[num - 1]
end

def find_shorest_distance(point1, point2)
  (point1[0] - point2[0]).abs + (point1[1] - point2[1]).abs
end

middle_cord = [0, 0]
point = find_coord(input)

puts find_shorest_distance(middle_cord, point)