LIGHT_MAP = 1000 

input = File.open('inputs/day6.txt')

def build_light_map
  map = Array.new(LIGHT_MAP)
  map.length.times do |i|
    map[i] = Array.new(LIGHT_MAP, false)
  end

  return map
end

def count_lights(map)
  count = 0 

  map.each do |x|
    x.each do |y|
      count += 1 if y
    end
  end

  return count 
end

def action(text_direction, map)
  min_x = text_direction[:first][:x]
  max_x = text_direction[:second][:x]
  min_y = text_direction[:first][:y]
  max_y = text_direction[:second][:y]

  (min_x..max_x).each do |x| 
    (min_y..max_y).each do |y|
      case text_direction[:light]
      when 1 
        map[x][y] = true
      when 0
        map[x][y] = false
      when -1 
        map[x][y] == true ? false : true
      end
    end
  end

  return map 
end

def text_direction(row)
  single_direction = row.split(" ")

  if single_direction[0] == "turn"
    single_direction.delete_at(0)
  end
  single_direction.delete_at(-2)

  dir = Hash.new

  case single_direction[1]
  when "on"
    dir[:light] = 1
  when "off"
    dir[:light] = 0
  when "toggle"
    dir[:light] = -1
  end

  first = row[1].split(",")
  second = row[2].split(",")

  dir[:first] = { x: first.first.to_i, y: first.last.to_i }
  dir[:second] = { x: second.first.to_i, y: second.last.to_i }

  return dir
end

def play_lights(input)
  map = build_light_map

  input.split("\n").each do |string|
    instruct = instr(string)
    map = action(text_direction, map)
  end

  return count(grid)
end


put play_lights(input)
