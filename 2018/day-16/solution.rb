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

input = File.open('input.txt').read
part_1, part_2 = input.split("\n\n\n")

chunks = part_1.split("\n\n")
# chunks = ["Before: [3, 2, 1, 1]
# 9 2 1 2
# After:  [3, 2, 2, 1]"]
instructions = chunks.map{ |c| c.split("\n").map{ |l| l.scan(/\d+/).map(&:to_i) } }
three_or_more_valid_opcodes = 0
opcode_names = 'addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr'
require 'set'
possible_real_codes = Hash.new { |h,k| h[k] = Set.new }

instructions.each do |before, effect, after|
  valid_opcodes = []
  opcode_names.each do |opcode|
    valid_opcodes.push(opcode) if send(opcode, effect[1], effect[2], effect[3], before.dup) == after.dup
    possible_real_codes[effect[0]].add(opcode) if send(opcode, effect[1], effect[2], effect[3], before.dup) == after.dup
  end
  three_or_more_valid_opcodes += 1 if valid_opcodes.length >= 3
end

until possible_real_codes.select{ |k, v| v.length == 1 }.length == 16
  found = possible_real_codes.select{ |k, v| v.length == 1 }
  not_found = possible_real_codes.select{ |k, v| v.length != 1 }
  not_found.keys.each do |k|
    found.values.map(&:to_a).flatten.each do |v|
      possible_real_codes[k].delete(v)
    end
  end
end

puts "part 1:"
puts three_or_more_valid_opcodes

puts "part 2:"
possible_real_codes.map{ |k, v| possible_real_codes[k] = v.to_a.first }
test_input = part_2.strip.split("\n").map{ |x| x.split(' ').map(&:to_i) }
state = [0, 0, 0, 0]

test_input.each do |i|
  send(possible_real_codes[i[0]], i[1], i[2], i[3], state)
end

puts state[0]