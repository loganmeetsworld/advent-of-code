input = File.open("./input.txt").readlines.map(&:chomp)

puts "Part 1:"

twos, threes = 0, 0
input.each do |box|
    freq_hash = box.split('').each_with_object(Hash.new(0)) { |o, h| h[o] += 1 }
    twos += 1 if freq_hash.values.include?(2)
    threes += 1 if freq_hash.values.include?(3)
end

puts twos * threes

puts "Part 2:"

solution = []
input.each_with_index do |box_one, pos|
    input[pos + 1..input.length].each do |box_two|
        conflict = box_one.each_char.with_index.count{ |k, v| k != box_two.chars[v] }
        if conflict == 1
            box_one.split('').each_with_index do |l, i|
                solution.push(l) if box_two[i] == l
            end
            break
        end
    end
end

puts solution.join('')