input = File.open("./input.txt").read

def build_next_row(current_row)
  new_row = []

  current_row.split('').each_with_index do |char, idx|
    min = idx - 1 < 0 ? '.' : current_row[idx - 1]
    max = idx + 2 > current_row.length ? '.' : current_row[idx + 1]
    if trap?(min, char, max)
      new_row << '^'
    else
      new_row << '.'
    end
  end

  return new_row.join('')
end

def left_center_trap_right_safe(min, char, max)
  min == '^' && char == '^' && max == '.'
end

def center_right_trap_left_safe(min, char, max)
  min == '.' && char == '^' && max == '^'
end

def left_only_trap(min, char, max)
  min == '^' && char == '.' && max == '.'
end

def right_only_trap(min, char, max)
  min == '.' && char == '.' && max == '^'
end

def trap?(min, char, max)
  left_center_trap_right_safe(min, char, max) || center_right_trap_left_safe(min, char, max) || left_only_trap(min, char, max) || right_only_trap(min, char, max)
end

rows = [input]
row = input

39999.times do
  rows << build_next_row(row)
  row = build_next_row(row)
end

puts rows.map{|x| x.split('').find_all{|y| y == '.'}.length }.inject(:+)
