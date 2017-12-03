input = File.open("./input.txt").read.split("\n")

first, second, third, fourth, fifth, sixth, seventh, eighth = [],[],[],[],[],[],[],[] 
part_1_code = ''
part_2_code = ''

def find_most_frequent(letters)
  freq = letters.inject(Hash.new(0)) { |hash,value| hash[value] += 1; hash }
  return letters.max_by { |value| freq[value] }
end

def find_least_frequent(letters)
  freq = letters.inject(Hash.new(0)) { |hash,value| hash[value] += 1; hash }
  return letters.min_by { |value| freq[value] }
end

input.each do |line|
  first << line[0]
  second << line[1]
  third << line[2]
  fourth << line[3]
  fifth << line[4]
  sixth << line[5]
  seventh << line[6]
  eighth << line[7]
end

[first, second, third, fourth, fifth, sixth, seventh, eighth].each do |x|
  part_1_code << find_most_frequent(x)
  part_2_code << find_least_frequent(x)
end

puts "Part 1: #{part_1_code}"
puts "Part 2: #{part_2_code}"
