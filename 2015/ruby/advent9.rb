input = File.read('inputs/day9.txt')
require 'set'


locations = {}
set = Set.new

input.split("\n").each do |l|
  line_array = l.split(' ')
  line_array.delete_at(1)
  line_array.delete_at(2)
  locations[line_array[0..1]] = line_array[2]
  set << line_array[0]
  set << line_array[1]
end

set = set.to_a
perms = set.permutation.to_a


distances = Hash.new

perms.each do|perm|
  sum = 0
  perm.each_with_index do |a, i|
    if perm[i + 1] != nil
      loc = ["#{a}", "#{perm[i + 1]}"]
      if locations[loc] == nil
        loc = ["#{perm[i + 1]}", "#{a}"]
      end
      sum += locations[loc].to_i
    end
    distances[perm] = sum
  end
end

puts distances.values.min
puts distances.values.max
