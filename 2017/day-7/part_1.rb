# part 1
def part_1
  File.open("./input.txt")
      .read
      .gsub(/(\W|\d)/, " ")
      .split
      .group_by{ |w| w }
      .select{ |k, v| v.length.eql? 1 }
      .keys
      .first
end

puts part_1