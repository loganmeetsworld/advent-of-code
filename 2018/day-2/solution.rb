input = File.open("./input.txt").readlines

puts "Part 1:"

twos, threes = 0, 0
input.each do |box|
    freq_hash = box.split('').each_with_object(Hash.new(0)) { |o, h| h[o] += 1 }
    twos += 1 if freq_hash.values.include?(2)
    threes += 1 if freq_hash.values.include?(3)
end

puts twos * threes

puts "Part 2:"
