require 'set'

input = File.read('input/day3.txt')

class Santa
  attr_accessor :coodrinates

  def initialize(x, y)
    @coodrinates = [x, y]
  end

  def action!(c)
    case c 
    when '^'
      @coodrinates[1] = @coodrinates[1] + 1
    when'v'
      @coodrinates[1] = @coodrinates[1] - 1
    when '>'
      @coodrinates[0] = @coodrinates[0] + 1
    when '<'
      @coodrinates[0] = @coodrinates[0] - 1
    end
  end
end

set = Set.new


santa = Santa.new(0, 0)
robot = Santa.new(0, 0)

set.push(santa.coodrinates.dup)

input.each_char.with_index do |char, index|
  if index.even?
    santa.action!(char)
    set << santa.coodrinates.dup
  else
    robot.action!(char)
    set << robot.coodrinates.dup
  end
end

puts set.length