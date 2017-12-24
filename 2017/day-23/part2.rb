def resolve(n, values)
  n.to_i.to_s == n ? n.to_i : values[n]
end

def run(registers)
  values, current_position, mul_count = Hash.new(0), 0, 0
  values['a'] = 1

  while current_position >= 0 && (line = registers[current_position])
    i, x, y = line[0], line[1], line[2]
    case i
    when 'sub'
      values[x] -= resolve(y, values)
    when 'set'
      values[x] = resolve(y, values)
    when 'mul'
      mul_count += 1
      values[x] *= resolve(y, values)
    when 'jnz'
      current_position += (resolve(y, values) - 1) if resolve(x, values) != 0
    end
    current_position += 1
  end

  mul_count
end

registers = File.open('input.txt').read.split("\n").map(&:split)
puts "Part 1: #{run(registers)}"
