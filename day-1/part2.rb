input = File.open("./input.txt").read.split('')
sum = 0
i = 0
length = input.length
half_way = length / 2

while i < length
  rotated_array = input.rotate(half_way)
  if input.first == rotated_array.first
    sum += input.first.to_i
    input.rotate!(1)
    i += 1
  else
    input.rotate!(1)
    i += 1
  end
end

puts sum