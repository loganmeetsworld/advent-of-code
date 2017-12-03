def cal(text)


  array_2 = text.split('x')

  x = 2 * array_2[0].to_i * array_2[1].to_i
  y = 2 * array_2[1].to_i * array_2[2].to_i
  z = 2 * array_2[0].to_i * array_2[2].to_i

  nums = []
  nums << [(x/2), (y/2), (z/2)]

  sum = x + y + z

  extra = nums.flatten.min

  total = sum + extra 
end

array_1 = a.split("\n")

sums = []
array_1.each do |t|
  sums << cal(t)
end

puts sums.inject(:+)