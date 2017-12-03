eggnogs = [
  50, 44, 11, 49, 
  42, 46, 18, 32, 
  26, 40, 21, 7, 
  18, 43, 10, 47, 
  36, 24, 22, 40
]

# messing around with what I want to do
eggnogs.min(8).inject(:+) # maximum smalls (20 total)
eggnogs.max(4).inject(:+) # minimum smalls (20 total)

# ok this is what i want to do 

def combos_4(arr, n)
  arr.combination(4).find_all { |(a, b, c, d)| a + b + c + d == n }
end

def combos_5(arr, n)
  arr.combination(5).find_all { |(a, b, c, d, e)| a + b + c + d + e == n }
end

def combos_6(arr, n)
  arr.combination(6).find_all { |(a, b, c, d, e, f)| a + b + c + d + e + f == n }
end

def combos_7(arr, n)
  arr.combination(7).find_all { |(a, b, c, d, e, f, g)| a + b + c + d + e + f + g == n }
end

def combos_8(arr, n)
  arr.combination(8).find_all { |(a, b, c, d, e, f, g, h)| a + b + c + d + e + f + g + h == n }
end

#part 2
puts combos_4(eggnogs, 150).length

# part 1
puts combos_4(eggnogs, 150).length +
combos_5(eggnogs, 150).length +
combos_6(eggnogs, 150).length +
combos_7(eggnogs, 150).length +
combos_8(eggnogs, 150).length
