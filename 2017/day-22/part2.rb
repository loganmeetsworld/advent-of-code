require 'pry'
input = File.open('input.txt').read.split("\n")
infinite_array_dim = 1003
sides = (infinite_array_dim - input.length) / 2
MAP = []
input.each{ |x| MAP.push(('.' * sides) + x + ('.' * sides)) }
sides.times { MAP.push('.' * infinite_array_dim); MAP.unshift('.' * infinite_array_dim) }
current_coords = [MAP.first.length / 2, MAP.length / 2]
current_node = MAP[MAP.first.length / 2][MAP.length / 2]
bursts = 10000000
infect_action_count = 0
direction = 'N'

def infected?(node); node == '#'; end
def clean?(node); node == '.'; end
def weakened?(node); node == 'W'; end
def flagged?(node); node == 'F'; end
def infect_node(coords); MAP[coords.last][coords.first] = '#'; end
def clean_node(coords); MAP[coords.last][coords.first] = '.'; end
def weaken_node(coords); MAP[coords.last][coords.first] = 'W'; end
def flag_node(coords); MAP[coords.last][coords.first] = 'F'; end
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

def change_direction(direction, state)
  case state
  when 'infected'
    arr = ['N', 'W', 'S', 'E']
    pos = arr.index(direction)
    new_direction = arr.rotate(pos + 1).first
  when 'cleaned'
    arr = ['N', 'E', 'S', 'W']
    pos = arr.index(direction)
    new_direction = arr.rotate(pos + 1).first
  when 'flagged'
    opp_hash = {'N' => 'S', 'S' => 'N', 'E' => 'W', 'W' => 'E'}
    new_direction = opp_hash[direction]
  when 'weakened'
    new_direction = direction
  end
  new_direction
end

bursts.times do
  if infected?(current_node)
    direction = change_direction(direction, 'infected')
    flag_node(current_coords)
    current_coords = move_forward(direction, current_coords)
  elsif clean?(current_node)
    direction = change_direction(direction, 'cleaned')
    weaken_node(current_coords)
    current_coords = move_forward(direction, current_coords)
  elsif weakened?(current_node)
    direction = change_direction(direction, 'weakened')
    infect_node(current_coords)
    infect_action_count += 1
    current_coords = move_forward(direction, current_coords)
  elsif flagged?(current_node)
    direction = change_direction(direction, 'flagged')
    clean_node(current_coords)
    current_coords = move_forward(direction, current_coords)
  end
  current_node = MAP[current_coords.last][current_coords.first]
end
# print_map
puts "Part 2: #{infect_action_count}"