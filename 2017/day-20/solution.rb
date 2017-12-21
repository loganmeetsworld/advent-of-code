instr = File.open('input.txt').read.lines.map(&:strip).map{|x| x.gsub!('<', '').gsub!('>', ''); [x.split(', ')[0].split('=')[1].split(',').map(&:to_i), x.split(', ')[1].split('=')[1].split(',').map(&:to_i), x.split(', ')[2].split('=')[1].split(',').map(&:to_i)]}

part1 = instr.each_with_index.min_by do |(p, v, a), _| 
  [a, v, p].map{ |x| x.sum(&:abs) }
end

puts "Part 1: #{part1[1]}"