input = File.read('inputs/day13.txt')

@hash = Hash.new { |k, v| k[v] = {} }

input.each_line.map do |line|
  signs = {"n" => 1, "e" => -1}
  arrange = line.scan(/(\w+).+(\w) (\d+).+?(\w+)\./)
  person, happy_count, seat = arrange[0][0], signs[arrange[0][1]].to_i * arrange[0][2].to_i, arrange[0][3]

  @hash[person][seat] = happy_count
end

def calculate_optimality(people)
  max_happy = people.map do |seating|
    seating.each_with_index.reduce(0) do |sum, (person, index)|
      next_index = index + 1
      if next_index >= seating.length then next_index = 0 end

      sum + @hash[person][seating[index - 1]] + @hash[person][seating[next_index]]
    end
  end
  puts max_happy.max
end

calculate_optimality(@hash.keys.permutation.to_a)

# Part 2, adding myself

input.each_line.map do |line|
  arrange = line.scan(/(\w+).+(\w) (\d+).+?(\w+)\./)
  person, seat = arrange[0][0], arrange[0][3]

  @hash["Logan"][seat] = 0
  @hash[person]["Logan"] = 0
end

calculate_optimality(@hash.keys.permutation.to_a)
