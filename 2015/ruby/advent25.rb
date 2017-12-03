require 'pry'
MULT = 252533
DIV = 33554393
MAX_ROW = 2981
MAX_COL = 3075
value = 20151125
col, row, incr_row = 1, 1, 1

def calculate(number)
  number * MULT % DIV
end

until col == MAX_COL && row == MAX_ROW
  value = calculate(value)

  if incr_row == col 
    row = incr_row + 1
    incr_row = row
    col = 1
    # binding.pry
  else
    row -= 1
    col += 1
  end
  # binding.pry
end

puts "The code at row #{row} and column #{col} is #{value}."