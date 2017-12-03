def cal(text)
  array_2 = text.split('x')

  x = array_2[0].to_i
  y = array_2[1].to_i
  z = array_2[2].to_i

  total_1 = x.to_i * y.to_i * z.to_i

  nums = []
  nums << [x, y, z]

  nums.flatten!.sort!

  total_2 = nums[0].to_i + nums[0].to_i + nums[1].to_i + nums[1].to_i

  total = total_1.to_i + total_2.to_i 
end

new_str = a.split("\n")

sums = []

new_str.each do |t|
  sums << cal(t)
end

puts sums.inject(:+)