def run(registers)
  current_position, values, freq = 0, {}, []
  registers.map{|x| values[x.split[1]] = 0}

  until current_position > registers.length
    i, x, y = registers[current_position].split[0], registers[current_position].split[1], registers[current_position].split[2]
    y = values[y] if y.to_i.to_s != y if y; y = y.to_i
    case i
    when 'snd'
      freq << values[x]
    when 'set'
      values[x] = y
    when 'add'
      values[x] += y
    when 'mul'
      values[x] *= y
    when 'mod'
      values[x] = values[x] % y
    when 'rcv'
      if freq[-1] > 0 then break freq end
    when 'jgz'
      current_position = (current_position + y) % registers.length - 1 if values[x] > 0
    end
    current_position += 1
  end
end

registers = File.open('input.txt').read.lines
puts "Part 1: #{run(registers).last}"
