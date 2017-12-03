require 'pry'
input = File.readlines('inputs/day23.txt')

increments = Hash.new

# Just change the first zero below to 1 for answer for part 2
increments['a'], increments['b'], step = 0, 0, 0

while step < input.length
  instructions = input[step].split(" ")
  case instructions[0]
  when "hlf"
    increments[instructions[1]] /= 2
  when "tpl"
    increments[instructions[1]] *= 3
  when "inc"
    increments[instructions[1]] += 1
  when "jmp"
    number = instructions[1].to_i
    step += (number - 1)
  when "jie"
    register = register = instructions[1].chomp(",")
    number = instructions[2].to_i

    # binding.pry
    if increments[register] % 2 == 0
      step += (number - 1)
    end
  when "jio"
    register = instructions[1].chomp(",")
    number = instructions[2].to_i

    if increments[register] == 1
      step += (number - 1)
    end
  end

  step += 1
end

puts increments['b']