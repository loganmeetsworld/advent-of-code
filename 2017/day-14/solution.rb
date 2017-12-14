require 'test/unit'
require_relative '../day-10/part_2.rb'
extend Test::Unit::Assertions

GRID_SIZE = 128

def knot_hash(input); day10_part2_answer(input); end

def knot_hash_map(key_string, map)
  (0...GRID_SIZE).each{ |i| map += knot_hash("#{key_string}-#{i.to_s}").to_i(16).to_s(2) + "\n" }
  map.gsub!('0', '.').gsub!('1', '#')
end

assert_equal knot_hash_map('flqrgnkx', '').count('#'), 8108
part_1 = knot_hash_map('nbysizxe', '').count('#')
puts "Part 1: #{part_1}"
