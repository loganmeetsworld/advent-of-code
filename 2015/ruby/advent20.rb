max_presents = 29000000
div_presents = max_presents / 11
decimal_presents = max_presents / 10
max_houses = 50
house_hash = Hash.new(0)
lowest_number = nil
house_hash_2 = Hash.new(0)
lowest_number_2 = nil

1.upto(decimal_presents) do |e|
  1.upto(decimal_presents / e) do |n|
    house_hash[n * e] += e * 10
  end
end

house_hash.find do |key, value|
  if value >= max_presents
    lowest_number = key
  end
end

puts "Part 1: " + lowest_number.to_s

1.upto(div_presents) do |e|
  1.upto([50, (div_presents / e)].min) do |n|
    house_hash_2[n * e] += e * 11
  end
end

house_hash_2.find do |key, value|
  if value >= max_presents
    lowest_number_2 = key
  end
end

puts "Part 2: " + lowest_number_2.to_s