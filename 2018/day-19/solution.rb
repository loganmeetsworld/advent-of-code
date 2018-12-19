def addr(a, b, c, before)
  before[c] = before[a] + before[b]
  return before
end

def addi(a, b, c, before)
  before[c] = before[a] + b
  return before
end

def mulr(a, b, c, before)
  before[c] = before[a] * before[b]
  return before
end

def muli(a, b, c, before)
  before[c] = before[a] * b
  return before
end

def banr(a, b, c, before)
  before[c] = before[a] & before[b]
  return before
end

def bani(a, b, c, before)
  before[c] = before[a] & b
  return before
end

def borr(a, b, c, before)
  before[c] = before[a] | before[b]
  return before
end

def bori(a, b, c, before)
  before[c] = before[a] | b
  return before
end

def setr(a, b, c, before)
  before[c] = before[a]
  return before
end

def seti(a, b, c, before)
  before[c] = a
  return before
end

def gtir(a, b, c, before)
  before[c] = a > before[b] ? 1 : 0
  return before
end

def gtri(a, b, c, before)
  before[c] = before[a] > b ? 1 : 0
  return before
end

def gtrr(a, b, c, before)
  before[c] = before[a] > before[b] ? 1 : 0
  return before
end

def eqir(a, b, c, before)
  before[c] = a == before[b] ? 1 : 0
  return before
end

def eqri(a, b, c, before)
  before[c] = before[a] == b ? 1 : 0
  return before
end

def eqrr(a, b, c, before)
  before[c] = before[a] == before[b] ? 1 : 0
  return before
end


input = File.open('test-input.txt').readlines.map(&:chomp)
registers = [0, 0, 0, 0, 0, 0]
instruction_pointer = input.first.scan(/\d+/).first.to_i
count = input.first.scan(/\d+/).first.to_i
instructions = input[1..-1]

while true
  i = instructions[instruction_pointer].split(' ')
  registers[0] = instruction_pointer
  send(i[0], i[1].to_i, i[2].to_i, i[3].to_i, registers)
  instruction_pointer = registers[0]
  instruction_pointer += 1
  break if !instructions[instruction_pointer]
end

puts "Part 1: "
puts registers.to_s
puts registers[0]