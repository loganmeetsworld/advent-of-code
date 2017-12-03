input = File.open("./input.txt").read.split('')
sum = 0
i = 0
length = input.length

while i < length
  if input[i + 1].nil? then input[i + 1] = input[0] end
  if input[i] == input[i + 1]
    while input[i] == input[i + 1]
      sum += input[i].to_i
      i += 1
    end
  else
    i += 1
  end
end

puts sum