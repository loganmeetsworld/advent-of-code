require 'pry'
class Bitwise
  attr_accessor :bit_machine, :output

  def initialize(input)
    @bit_machine = Hash.new
    @output = Hash.new
    @input = input
    input.each do |line|
      val_1 = line.chomp.split('->')[0]
      val_2 = line.chomp.split('->')[1]
      val_2 = val_2.lstrip
      @bit_machine[val_2] = val_1.split
    end
  end

  def calc_bitwise(variable)
    if variable.match(/^\d+$/)
      return variable.to_i
    end

    if ! @output.has_key?(variable)
      operation = @bit_machine[variable]
      if operation.length == 1
        value = calc_bitwise(operation[0])
      else
        x = operation[-2]
        case x
        when 'RSHIFT'
          value = calc_bitwise(operation[0]) >> calc_bitwise(operation[2])
        when 'LSHIFT'
          value = calc_bitwise(operation[0]) << calc_bitwise(operation[2])
        when 'AND'
          value = calc_bitwise(operation[0]) & calc_bitwise(operation[2])
        when 'OR'
          value = calc_bitwise(operation[0]) | calc_bitwise(operation[2])
        when 'NOT'
          value = ~calc_bitwise(operation[1])
        end
      end
      @output[variable] = value
    end
    return @output[variable]
  end
end

input = File.readlines('inputs/day7.txt')
input_part_2 = File.read('inputs/day7.txt').gsub(/\d\d\d\d\d -> b/, '3176 -> b')

b = Bitwise.new(input)
b_part_two = Bitwise.new(input_part_2.split("\n"))
b.calc_bitwise("a")
b_part_two.calc_bitwise("a")