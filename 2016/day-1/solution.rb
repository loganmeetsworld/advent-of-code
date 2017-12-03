require 'set'

def update_direction(cardinal_direction, turn_direction)
  directions = {'N' => 0, 'E' => 1, 'S' => 2, 'W' => 3}
  position = directions[cardinal_direction]
  position = turn_direction == "R" ? (position + 1) % 4 : (position - 1) % 4

  return directions.keys[position]
end

def update_location(current_direction, current_location, steps)
  case current_direction
  when 'N'
    current_location[:y] = current_location[:y] + steps
  when 'E'
    current_location[:x] = current_location[:x] + steps
  when 'S'
    current_location[:y] = current_location[:y] - steps
  when 'W'
    current_location[:x] = current_location[:x] - steps
  end

  return current_location
end

def part_1(input, current_direction="N", current_location={ x: 0, y: 0 })
  input.each do |turn|
    current_direction = update_direction(current_direction, turn[0])
    current_location = update_location(current_direction, current_location, turn[1..-1].to_i)
  end

  current_location.values.map(&:abs).inject(:+)
end

def part_2(input, current_direction="N", current_location={ x: 0, y: 0 })
  coords = Set.new
  input.each do |turn|
    current_direction = update_direction(current_direction, turn[0])
    steps = turn[1..-1].to_i
    (1..steps).to_a.each do |step|
      if coords.include? current_location.to_s
        return [current_location.values.map(&:abs).inject(:+), step]
      else
        coords << current_location.to_s
        current_location = update_location(current_direction, current_location, 1)
      end
    end
  end
end

input = File.open("./input.txt").read.split(", ")
puts "Part 1 Answer: HQ is #{part_1(input)} blocks away."
part_2_answer = part_2(input)
puts "Part 2 Answer: Took #{part_2_answer[1]} steps / #{input.length} steps to get to HQ which is #{part_2_answer[0]} blocks away."
