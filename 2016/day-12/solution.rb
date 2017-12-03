registers_part_1 = {'a' => 0, 'b' => 0, 'c' => 0, 'd' => 0}
registers_part_2 = {'a' => 0, 'b' => 0, 'c' => 1, 'd' => 0}

def execute_assembunny(registers)
  input = File.open("./input.txt").read.split("\n")
  idx = 0

  while input.length > idx
    line = input[idx]
    inst, x, y = line.split(' ')[0], line.split(' ')[1], line.split(' ')[2]
    case inst
    when 'cpy'
      registers[y] = registers[x] ? registers[x] : x.to_i
      idx += 1
    when 'inc'
      registers[x] += 1
      idx += 1
    when 'dec'
      registers[x] -= 1
      idx += 1
    when 'jnz'
      if registers[x] && registers[x].to_i > 0
        idx += y.to_i
      elsif x.to_i > 0
        idx += y.to_i
      else
        idx += 1
      end
    end
  end
  return registers['a'].to_s
end

puts "Part 1: #{execute_assembunny(registers_part_1)}"
puts "Part 2: #{execute_assembunny(registers_part_2)}"
