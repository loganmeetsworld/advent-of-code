def run(registers, id, freq, received)
  current_position, count, values = 0, 0, Hash.new(0)
  resolve = ->(e) { e.to_i.to_s == e ? e.to_i : values[e] }

  -> {
    ran = false
    while current_position >= 0 && (line = registers[current_position])
      i, x, y = line.split[0], line.split[1], line.split[2]
      case i
      when 'snd'
        freq << resolve[x]
      when 'set'
        values[x] = resolve[y]
      when 'add'
        values[x] += resolve[y]
      when 'mul'
        values[x] *= resolve[y]
      when 'mod'
          values[x] %= resolve[y]
      when 'rcv'
        return ran ? :wait : :still_waiting unless (val = received[count])
        count += 1
        values[x] = val
      when 'jgz'
        current_position += (resolve[y] - 1) if resolve[x] > 0
      end
      current_position += 1
      ran = true
    end
  }
end

registers = File.open('input.txt').read.lines
programs = [[], []]
runners = [0, 1].map { |id| run(registers, id, programs[id], programs[1 - id]) }
partner_waiting = false

0.step do |n|
  status = runners[n % 2][]
  if status == :still_waiting && partner_waiting
    puts "Part 2: #{programs[1].count}"
    break
  end
  partner_waiting = status == :still_waiting
end
