class Screen
  attr_reader :screen_map
  def initialize(a, b)
    @a = a
    @b = b
    @screen_map = Array.new(@b * @a){'.'}.each_slice(@b).to_a
  end

  def parse_instr(instr)
    case instr[0]
    when 'rotate'
      instr[1] == 'row' ? row(instr[2].split('=')[1].to_i, instr[4].to_i) : column(instr[2].split('=')[1].to_i, instr[4].to_i)
    when 'rect'
      rect(instr[1].split('x')[0].to_i, instr[1].split('x')[1].to_i)
    end
  end

  def rect(a, b)
    a.times { |x| b.times { |y| @screen_map[y][x] = "#" }}
  end

  def row(y, x)
    @screen_map[y].rotate!(-x)
  end

  def column(x, y)
    new_column = (0...@a).to_a.map{ |k| @screen_map[k][x] }.rotate(-y)
    new_column.each_with_index do |v, i|
      @screen_map[i][x] = v
    end
  end

  def pixels_on
    @screen_map.flatten.count('#')
  end

  def prt
    @screen_map.each{|x| puts x.flatten.join('') }
  end
end

instructions = File.open("./input.txt").read.split("\n")
screen = Screen.new(6, 50)

instructions.each do |instr|
  screen.parse_instr(instr.split(' '))
end

puts "Part 1: #{screen.pixels_on}\n#{screen.prt}"
