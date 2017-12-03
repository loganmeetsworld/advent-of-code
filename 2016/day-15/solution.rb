class Disc
  @@discs = []
  attr_reader :number, :positions, :position_at_zero
  
  def initialize(number, num_positions, position_at_zero)
    @number = number
    @num_positions = num_positions
    @position_at_zero = position_at_zero
    @@discs << self
  end

  def position_at(time)
    time <= 2 ? @position_at_zero + time : (@position_at_zero + time) % @num_positions
  end

  def passes_through?(time)
    position_at(time + @number) == 0
  end

  def self.all
    @@discs
  end
end

def press_button_at(input)
  input.each do |disc|
    matches = disc.scan(/(\d+)/).flatten
    number = matches[0].to_i
    num_positions = matches[1].to_i
    position_at_zero = matches[3].to_i
    Disc.new(number, num_positions, position_at_zero)
  end

  time = 0

  until Disc.all.select{|disc| disc.passes_through?(time) }.length == Disc.all.length
    time += 1
  end

  return time
end

input = File.open("./input.txt").readlines
input_2 = File.open("./input-2.txt").readlines

puts "Part 1: #{press_button_at(input)}"
puts "Part 2: #{press_button_at(input_2)}"
