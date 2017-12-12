require 'set'
input = File.open('input.txt').read.split("\n")
program_hash = Hash.new
input.map{ |x| program_hash[x.split(' <-> ')[0]] = x.split(' <-> ')[1].scan(/(\d+)/).flatten }
initial_program = '0'

def answer(initial_program, program_hash)
  program_set = Set.new
  program_set.add(initial_program)
  next_programs = program_hash[initial_program]

  while !next_programs.empty?
    next_program = next_programs.shift
    next_program_connections = program_hash[next_program]

    if next_program_connections.find{ |pcs| program_set.include?(pcs) } && !program_set.include?(next_program)
      program_set.add(next_program)
      next_programs += next_program_connections
    end
  end
  return program_set
end

program_set = answer(initial_program, program_hash)

puts "Part 1: #{program_set.length}"