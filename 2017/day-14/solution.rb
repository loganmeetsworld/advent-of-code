require 'test/unit'
require_relative '../day-10/part_2.rb'
extend Test::Unit::Assertions

GRID_SIZE = 128

def knot_hash(input); day10_part2_answer(input); end

def create_map(key_string)
  map = ''
  (0...GRID_SIZE).each do |i|
    map += knot_hash("#{key_string}-#{i.to_s}").to_i(16).to_s(2) + "\n"
  end
  map
end

def part1_answer(key_string)
  create_map(key_string).count('1')
end

assert_equal part1_answer('flqrgnkx'), 8108
part_1 = part1_answer('nbysizxe')
puts "Part 1: #{part_1}"