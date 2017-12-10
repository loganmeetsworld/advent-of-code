require 'test/unit'
extend Test::Unit::Assertions

def reverse_list(current_position, list, length)
  list = list.rotate(current_position)
  list[0...length] = list[0...length].reverse
  return list.rotate(-current_position)
end

def sparse_hash(input)
  list = (0..255).to_a
  current_position = 0
  skip_size = 0
  64.times do
    lengths = input.chomp.bytes + [17, 31, 73, 47, 23]    
    lengths.each do |length|
      list = reverse_list(current_position, list, length)
      current_position = (current_position + length + skip_size) % list.length
      skip_size += 1
    end
  end
  return list
end

def answer(input)
  dense_hash = sparse_hash(input).each_slice(16).map{ |part| part.reduce(&:^) }  
  dense_hash.map{ |char| char.to_s(16).rjust(2,"0") }.join
end

input = '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'
puts answer(input)