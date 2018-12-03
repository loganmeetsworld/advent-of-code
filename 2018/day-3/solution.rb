lines = File.open("./input.txt").readlines.map(&:chomp).map(&:freeze).freeze
SQUARE_DIMENSION = 1000

def build_square(dim)
    square = Array.new(dim)
    square.length.times do |i|
        square[i] = Array.new(dim, '.')
    end

    return square
end

def parse(line)
    scan = line.scan(/(\d+)/).map(&:first)
    return {'id': scan[0], 'dist_from_left': scan[1], 'dist_from_top': scan[2], 'width': scan[3], 'height': scan[4]}
end

square = build_square(SQUARE_DIMENSION)
instructions = lines.map{ |x| parse(x) }

instructions.each do |instr|
    (0...instr[:width].to_i).to_a.each do |x|
        (0...instr[:height].to_i).to_a.each do |y|
            if square[instr[:dist_from_top].to_i + y][instr[:dist_from_left].to_i + x] == '.'
                square[instr[:dist_from_top].to_i + y][instr[:dist_from_left].to_i + x] = instr[:id]
            else
                square[instr[:dist_from_top].to_i + y][instr[:dist_from_left].to_i + x] = 'X'
            end
        end
    end
end

puts "Part 1:"
File.open("output.txt", "w+") do |f|
    square.each { |element| f.puts(element.join('')) }
end
puts square.flatten.count('X')

# puts "Part 2:"