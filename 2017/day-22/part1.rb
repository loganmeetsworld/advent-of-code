require 'pry'
input = File.open('input.txt').read.split("\n")
infinite_array_dim = 1003
sides = (infinite_array_dim - input.length) / 2
MAP = []
input.each{ |x| MAP.push(('.' * sides) + x + ('.' * sides)) }
sides.times { MAP.push('.' * infinite_array_dim); MAP.unshift('.' * infinite_array_dim) }
current_coords = [MAP.first.length / 2, MAP.length / 2]
current_node = MAP[MAP.first.length / 2][MAP.length / 2]
bursts = 10000
infect_action_count = 0
direction = 'N'

def infected?(node); node == '#'; end
def clean?(node); node == '.'; end
def infect_node(coords); MAP[coords.last][coords.first] = '#'; end
def clean_node(coords); MAP[coords.last][coords.first] = '.'; end
def print_map; puts; MAP.each{|x| puts x.split('').join(' ') }; end

def move_forward(direction, coords)
  case direction
  when 'N'
    current_coords = [coords.first, coords.last - 1]
  when 'S'
    current_coords = [coords.first, coords.last + 1]
  when 'W'
    current_coords = [coords.first + 1, coords.last]
  when 'E'
    current_coords = [coords.first - 1, coords.last]
  end
  current_coords
end

def change_direction(direction, right)
  if right
    arr = ['N', 'W', 'S', 'E']
    pos = arr.index(direction)
    new_direction = arr.rotate(pos + 1).first
  else
    arr = ['N', 'E', 'S', 'W']
    pos = arr.index(direction)
    new_direction = arr.rotate(pos + 1).first
  end
  new_direction
end

bursts.times do
  # print_map
  # puts current_coords.to_s
  if infected?(current_node)
    # binding.pry
    direction = change_direction(direction, true)
    clean_node(current_coords)
    current_coords = move_forward(direction, current_coords)
    current_node = MAP[current_coords.last][current_coords.first]
  elsif clean?(current_node)
    # binding.pry
    direction = change_direction(direction, false)
    infect_node(current_coords)
    infect_action_count += 1
    current_coords = move_forward(direction, current_coords)
    current_node = MAP[current_coords.last][current_coords.first]
  end
end
# print_map
puts "Part 1: #{infect_action_count}"