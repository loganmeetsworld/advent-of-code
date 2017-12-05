require 'test/unit'
extend Test::Unit::Assertions

def answer(input, part)
  i = 0
  jumps = 0
  jumps_to_exit = 0
  old_i = 0
  offsets_length = input.length

  while i < offsets_length
    jumps = input[i]
    old_i = i
    i += jumps.to_i
    if part == '1'
      input[old_i] += 1
    elsif part == '2'
      input[old_i] = jumps >= 3 ? input[old_i] -= 1 : input[old_i] += 1
    end
    jumps_to_exit += 1    
  end

  return jumps_to_exit
end

test_input = "0\n3\n0\n1\n-3".split("\n").map(&:to_i)
assert_equal answer(test_input, '1'), 5
test_input = "0\n3\n0\n1\n-3".split("\n").map(&:to_i)
assert_equal answer(test_input, '2'), 10

input = File.open("./input.txt").read.split("\n").map(&:to_i)
puts "Part 1: #{answer(input, '1')}"
input = File.open("./input.txt").read.split("\n").map(&:to_i)
puts "Part 2: #{answer(input, '2')}"
