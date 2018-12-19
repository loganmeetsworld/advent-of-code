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

input = File.open('input.txt').readlines.map(&:chomp)
instruction_pointer = input.first.scan(/\d+/).first.to_i
instructions = input[1..-1]

registers = [0, 0, 0, 0, 0, 0]

while true
  begin
    ip = registers[instruction_pointer]
    opcode = instructions[ip].split()
    args = opcode[1..-1].map(&:to_i)
    instr = opcode[0]
    registers = send(instr, *args, registers)
    registers[instruction_pointer] += 1
  rescue NoMethodError => e
    puts registers.to_s
    break
  end
end

puts "Part 1: "
puts registers[0]


# For part 2 I completely followed https://www.youtube.com/watch?v=74vojWBORpo