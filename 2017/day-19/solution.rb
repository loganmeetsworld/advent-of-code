input = File.open('input.txt').read.lines.map{|l| l.chars }
start_index, road = [0, input[0].index('|')], {}
letter_count, pos, direction, letter_collector, steps = input.flatten.join.scan(/\p{L}/ ).length, start_index.dup, [1, 0], [], 0
input.each_with_index{|i, x| i.each_with_index{|j, y| 
  if j =~ /\p{L}/ then road[[x, y]] = j elsif j =~ /\S/ then road[[x, y]] = 'x' end
}}

def rotate_left(dir); [dir[1], -dir[0]]; end
def rotate_right(dir); [-dir[1], dir[0]]; end
def next_position(pos, dir); [pos[0] + dir[0], pos[1] + dir[1]]; end

until letter_collector.length == letter_count do
  steps += 1
  letter_collector.push road[pos] if road[pos] != 'x'
  if !road[next_position(pos, direction)]
    if road[next_position(pos, rotate_left(direction))]
      direction = rotate_left(direction)
    elsif road[next_position(pos, rotate_right(direction))]
      direction = rotate_right(direction)
    end
  end
  pos = next_position(pos, direction)
end

puts "Part 1: #{letter_collector.join}"
puts "Part 2: #{steps}"