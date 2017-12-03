# diagram = [
#   [
#     [:gen, :thulium],    [:gen, :plutonium], [:gen, :strontium],   [:chip, :thulium]
#   ], 
#   [
#     [:chip, :plutonium], [:chip, :strontium], nil, nil
#   ],
#   [
#     [:gen, :promethium], [:gen, :ruthenium], [:chip, :promethium], [:chip, :ruthenium]
#   ], 
#   [
#     nil, nil, nil, nil
#   ]
# ]

part_1 = [4, 2, 4, 0]
part_1_total = 0
part_2 = [8, 2, 4, 0]
part_2_total = 0

for i in (1...4).to_a
  part_1_total += 2 * part_1[0...i].inject(:+) - 3
  part_2_total += 2 * part_2[0...i].inject(:+) - 3
end

puts "Part 1: #{part_1_total}"
puts "Part 2: #{part_2_total}"
