def run(registers)
  current_position, values, freq = 0, Hash.new(0), []

  while current_position >= 0 && (line = registers[current_position])
    i, x, y = line.split[0], line.split[1], line.split[2]
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
        values[x] %= y
    when 'rcv'
      if values[x] > 0 then break freq end
    when 'jgz'
      n = x.to_i.to_s != x ? values[x] : x
      current_position = (current_position + y) % registers.length - 1 if n > 0
    end
    current_position += 1
  end
end

registers = File.open('input.txt').read.lines
puts "Part 1: #{run(registers).last}"
