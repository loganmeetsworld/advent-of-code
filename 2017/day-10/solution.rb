require 'test/unit'
extend Test::Unit::Assertions

def reverse_list(current_position, list, length)
  list = list.rotate(current_position)
  list[0...length] = list[0...length].reverse
  return list.rotate(-current_position)
end

def answer(lengths, last_num_in_list)
  list = (0..last_num_in_list).to_a
  current_position = 0
  skip_size = 0
  lengths.each do |length|
    list = reverse_list(current_position, list, length)
    current_position = (current_position + length + skip_size) % list.length
    skip_size += 1
  end

  return list[0] * list[1]
end

input_lengths = '3,4,1,5'.split(',').map(&:to_i)
assert_equal answer(input_lengths, 4), 12

input_lengths = '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'.split(',').map(&:to_i)
puts answer(input_lengths, 255)