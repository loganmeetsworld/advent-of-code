def answer(registers)
  values, current_position, freq = {}, 0, []
  registers.map{|x| values[x.split(' ')[1]] = 0}

  until current_position > registers.length
    i, x, y = registers[current_position].split(' ')[0], registers[current_position].split(' ')[1], registers[current_position].split(' ')[2]
     y = values[y] if y.to_i.to_s != y if y
    case i
    when 'snd'
      freq << values[x]; current_position += 1
    when 'set'
      values[x] = y.to_i; current_position += 1
    when 'add'
      values[x] += y.to_i; current_position += 1
    when 'mul'
      values[x] *= y.to_i; current_position += 1
    when 'mod'
      values[x] = values[x] % y.to_i; current_position += 1
    when 'rcv'
      if freq[-1] > 0 then return freq; break else current_position += 1 end
    when 'jgz'
      values[x] > 0 ? current_position = (current_position + y.to_i) % registers.length : current_position += 1
    end
  end
end

registers = File.open('input.txt').read.split("\n")
puts "Part 1: #{answer(registers)[-1]}"

sound = []