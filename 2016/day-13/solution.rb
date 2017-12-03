require 'set'

def calc(x,y,input)
  sum = (x*x) + (3*x) + (2*x*y) + y + (y*y) + input.to_i
  sum.to_s(2).split('').select{|x| x == '1'}.length % 2 == 0 ? '.' : '#'
end

def build_map
  map = []
  for x in (0..50).to_a
    horizontal_map = []
    for y in (0..50).to_a
      horizontal_map << calc(x, y, 1350)
    end
    map << horizontal_map
  end
  map
end

def open?(x, y)
  map = build_map
  map[x][y] == '.'
end

def not_seen?(visited, x, y)
  !visited.include?([x, y])
end

def not_neg?(x, y)
  !(x < 0 || y < 0)
end

def print_map
  build_map.map{|x| puts x.join('')}
end

def find_shortest_paths(end_x,end_y)
  visited = Set.new
  up_next = [[1, 1, 0]]
  visited.add(up_next.first[0..1])

  while up_next.any?
    current = up_next.shift

    if current[0..1] == [end_x, end_y]
      puts "Part 1: #{current[2]}"
      exit
    end

    x = current[0]
    y = current[1]
    step_count = current[2]

    [[x+1, y], [x-1, y], [x, y+1], [x, y-1]].each do |x, y|
      if not_neg?(x, y) && open?(x, y) && not_seen?(visited, x, y)
        visited.add([x, y])
        next_location = [x, y, step_count + 1]
        if next_location[2] == 50
          puts "Part 2: #{visited.length}"
        end
        up_next << next_location
      end
    end
  end
end

puts print_map
puts find_shortest_paths(31,39)
