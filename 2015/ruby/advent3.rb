require 'set'

cords = Array.new
init_cord = [0, 0]

text.each_char do |t|
  case t
  when "^"
    cords << [init_cord[0], init_cord[1] += 1]
  when ">"
    cords << [init_cord[0] += 1, init_cord[1]]
  when "v"
    cords << [init_cord[0], init_cord[1] -= 1]
  when "<"
    cords << [init_cord[0] -= 1, init_cord[1]]
  end
end

puts cords.length