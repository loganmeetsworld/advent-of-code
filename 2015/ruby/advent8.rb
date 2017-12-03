input = File.read('inputs/day8.txt')

all_chars = 0
non_chars = 0
encode_chars = 0

input.split.each do |l|
  non_chars += l.size
end

input.split.each do |l|
  all_chars += eval(l).size
end

input.split.each do |l|
  encode_chars += l.inspect.size
end

puts non_chars - all_chars
puts encode_chars - non_chars

