input = File.open('input.txt').read.split("\n")
frequencies = []
values = {}
input.map{|x| values[x.split(' ')[1]] = 0}
current_position = 0
last_freq = nil

class String
  def is_integer?
    self.to_i.to_s == self
  end
end

until current_position > input.length
  instr = input[current_position]
  x = instr.split(' ')[1]
  if instr.split(' ')[2]
    y = instr.split(' ')[2]
    if !y.is_integer?
      y = values[y]
    end
  end
  case instr.split(' ')[0]
  when 'snd'
    last_freq = values[x]
    current_position += 1
  when 'set'
    values[x] = y.to_i
    current_position += 1
  when 'add'
    values[x] += y.to_i
    current_position += 1
  when 'mul'
    values[x] *= y.to_i
    current_position += 1
  when 'mod'
    values[x] = values[x] % y.to_i
    current_position += 1
  when 'rcv'
    if last_freq > 0
      puts last_freq
      break
    else
      current_position += 1
    end
  when 'jgz'
    if values[x] > 0
      current_position = (current_position + y.to_i) % input.length
    else
      current_position += 1
    end
  end
end
