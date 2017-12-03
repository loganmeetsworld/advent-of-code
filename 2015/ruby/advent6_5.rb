LIGHT_MAP = 1000 
input = File.read('inputs/day6.txt')

def build_light_map
  map = []

  (0..999).each do |i|
    map[i] = Array.new(LIGHT_MAP, 0)
  end

  return map
end

def build_directions(row)
  single_direction = row.split(" ")

  if single_direction[0] == "turn"
    single_direction.delete_at(0)
  end
  single_direction.delete_at(-2)

  minimums = single_direction[1].split(",")
  maximums = single_direction[2].split(",")

  coordinate_index = {}

  coordinate_index[:minimums] = { x: minimums.first.to_i, y: minimums.last.to_i }
  coordinate_index[:maximums] = { x: maximums.first.to_i, y: maximums.last.to_i }

  case single_direction[0]
  when "on"
    coordinate_index[:instruction] = 1
  when "off"
    coordinate_index[:instruction] = 0
  when "toggle"
    coordinate_index[:instruction] = -1
  end

  return coordinate_index
end

def action(coordinate_index, map)
  min_x = coordinate_index[:minimums][:x]
  max_x = coordinate_index[:maximums][:x]
  min_y = coordinate_index[:minimums][:y]
  max_y = coordinate_index[:maximums][:y]

  (min_x..max_x).each do |x| 
    (min_y..max_y).each do |y|
      case coordinate_index[:instruction]
      when 1 
        map[x][y] += 1
      when 0
        unless map[x][y] <= 0
          map[x][y] -= 1
        end
      when -1 
        map[x][y] += 2
      end
    end
  end

  return map
end

def play_lights(input)
  map = build_light_map

  input.split("\n").each do |string|
    instruct = build_directions(string)
    map = action(instruct, map)
  end

  return map.flatten!.inject(:+)
end

puts play_lights(input)