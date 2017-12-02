rows = File.open("./input.txt").read.gsub(' ', '').gsub("\t", ",").split("\n")

first_sum = 0 

rows.each do |x|
  row = x.split(',').map(&:to_i)
  first_sum += row.max - row.min
end

puts first_sum 

second_sum = 0 

rows.each do |x|
  row = x.split(',').map(&:to_i)
  combos = row.combination(2).to_a.map{|x| x.sort.reverse }
  nums = nil
  combos.each do |x|
    if x[0] % x[1] == 0
      nums = x
    end
  end
  second_sum += (nums.max / nums.min)
end

puts second_sum 
