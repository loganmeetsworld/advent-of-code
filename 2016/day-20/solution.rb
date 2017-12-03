input = File.open("./input.txt").read.split("\n").map{|x| [x.split('-')[0].to_i, x.split('-')[1].to_i]}.sort_by{|x| x[0]}

last_max = input[0][1]
last_min = input[1][0]

input.each_with_index do |x, i|
  if last_min - last_max >= 2
    puts 'Part 1: ' + (last_min - 1).to_s
    break
  end
  last_max = input[i][1]
  last_min = input[i + 1][0]
end


input.each_with_index do |x, i|
  if last_min < last_max
end