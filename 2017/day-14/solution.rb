require_relative '../day-10/part_2.rb'

def knot_hash(input); day10_part2_answer(input); end
def knot_hash_map(key_string)
  coords = []
  (0...128).each do |i| 
    kh = knot_hash("#{key_string}-#{i.to_s}")
    coords[i] = kh.hex.to_s(2).rjust(kh.size * 4, ?0).chars.map(&:to_i)
  end
  coords
end

KHM = knot_hash_map('nbysizxe')
SEEN = Array.new(128) { Array.new(128, false) }
regions = 0

def depth_first_search(x, y)
  return if SEEN[x][y] || KHM[x][y] == 0
  SEEN[x][y] = true
  depth_first_search(x - 1, y) if x > 0
  depth_first_search(x + 1, y) if x < 127
  depth_first_search(x, y - 1) if y > 0
  depth_first_search(x, y + 1) if y < 127
end

(0...128).each do |x|
  (0...128).each do |y|
    next if SEEN[x][y] || KHM[x][y] == 0
    regions += 1
    depth_first_search(x, y)
  end
end

puts "Part 1: #{KHM.flatten.count(1)}"
puts "Part 2: #{regions}"
