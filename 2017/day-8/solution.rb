instrs = File.open("./input.txt").read.split("\n")
elements = File.open("./input.txt").read.gsub!(/(\W|\d)/, ' ').gsub!('if', ' ').gsub!('inc', ' ').gsub!('dec', ' ').split.uniq
elements_hash = Hash.new
elements.each{|e| elements_hash[e] = 0 }
part_2_max = 0

instrs.each do |n|
  instr_array = n.chomp.split
  element, dir, amount, comp_num, cond, cond_num = instr_array[0], instr_array[1], instr_array[2].to_i, instr_array[4], instr_array[5], instr_array[6].to_i
  if elements_hash[comp_num].send(cond, cond_num)
    dir == 'inc' ? elements_hash[element] += amount : elements_hash[element] -= amount
  end

  if elements_hash.values.max > part_2_max
    part_2_max = elements_hash.values.max
  end
end

puts "Largest value at end: #{elements_hash.values.max}"
puts "Largest value during: #{part_2_max}"
puts elements_hash.to_s