# part 1
a = File.open("./input.txt")
        .read
        .gsub(/(\W|\d)/, " ")
        .split
        .group_by { |w| w }
        .select { |k, v| v.size.eql? 1 }
        .keys

puts a