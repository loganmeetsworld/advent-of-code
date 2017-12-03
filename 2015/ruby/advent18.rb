input = File.readlines('inputs/day18.txt')

NUMS = [-1, -1, 0, 1, 1]
COORDS = NUMS.permutation(2).to_a.uniq
ALWAYS_ON = [[0, 0], [0, 99], [99, 0], [99, 99]] # Part Two
light_hash = Hash.new

input.each_with_index do |l, y|
  l.strip!
  l.split(//).each_with_index do |c, x|
    if c == "#"
      light_hash[[x, y]] = true
    else
      light_hash[[x, y]] = false
    end
  end
end

def find_nearby(light_hash, x, y)
  count = 0
  COORDS.each do |coord_x, coord_y|
    if light_hash[[x + coord_x, y + coord_y]]
      count += 1
    end
  end
  return count
end

def calc_lights(light_hash)
  result = {}
  100.times do |y|
    100.times do |x|

      # # Add for Part Two !!!
      # ALWAYS_ON.each do |x, y|
      #   light_hash[[x, y]] = true 
      # end

      current = light_hash[[x, y]]
      nearby = find_nearby(light_hash, x, y)

      if current
        if nearby == 2 || nearby == 3
          result[[x, y]] = true          
        end
      else
        if nearby == 3
          result[[x, y]] = true
        end
      end
    end
  end

  # # Add for Part Two !!!
  # ALWAYS_ON.each do |x, y|
  #   light_hash[[x, y]] = true 
  # end

  result
end

100.times do |i|
  light_hash = calc_lights(light_hash)
end

puts light_hash.length