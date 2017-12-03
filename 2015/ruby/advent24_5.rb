require "pry"

packages = [
  1, 3, 5, 11, 13, 17, 
  19, 23, 29, 31, 37, 
  41, 43, 47, 53, 59, 
  67, 71, 73, 79, 83, 
  89, 97, 101, 103, 107, 
  109, 113
]

max_weight = packages.inject(:+) / 4 # A good total

# Finding the min and max combo
packages.min(16).inject(:+)
packages.max(4).inject(:+)

(4..17).each do |i|
  combos = packages.combination(i)
  combos.each do |c|
    sum = c.reduce(:+)
    if sum == max_weight
      puts i 
      break # returns five (smallest)
    end
  #   # binding.pry
  end
end

array = []

five_combos = packages.combination(5).to_a

five_combos.each do |c|
  sum = c.reduce(:+)
  if sum == max_weight
    array << c
  end
end

qes = []

array.each do |c|
  qes << c.inject(:*)
end

# Part one
puts qes.min