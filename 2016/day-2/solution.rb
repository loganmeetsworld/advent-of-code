def find_number(current_number_position, count, string, numbers_array) 
  x = current_number_position[0]
  y = current_number_position[1]

  if count == string.length
    return [x, y]
  else
    direction = string[count]
    case direction
    when 'U'
      x -= 1
      unless numbers_array[x].nil? || numbers_array[x][y].nil? || x < 0
        current_number_position[0] -= 1
      end
    when 'D'
      x += 1
      unless numbers_array[x].nil? || numbers_array[x][y].nil?
        current_number_position[0] += 1
      end
    when 'L'
      y -= 1
      unless numbers_array[x][y].nil? || y < 0
        current_number_position[1] -= 1
      end
    when 'R'
      y += 1
      unless numbers_array[x][y].nil?
        current_number_position[1] += 1
      end
    end

    count += 1
    find_number(current_number_position, count, string, numbers_array)
  end
end

def sum_code_string(input, starting_point, numbers_array)
  bathroom_code = ''
  for i in input
    count = 0
    coords = find_number(starting_point, count, i, numbers_array)
    starting_point = coords
    bathroom_code += numbers_array[coords[0]][coords[1]].to_s
  end

  return bathroom_code
end

input = File.open("./input.txt").read.split("\n")
starting_point_part_1 = [1, 1]
numbers_array_part_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
starting_point_part_2 = [2, 0]
numbers_array_part_2 = [[nil, nil, 1, nil, nil], [nil, 2, 3, 4, nil], [5, 6, 7, 8, 9], [nil, 'A', 'B', 'C', nil], [nil, nil, 'D', nil, nil]]

puts sum_code_string(input, starting_point_part_1, numbers_array_part_1)
puts sum_code_string(input, starting_point_part_2, numbers_array_part_2)
