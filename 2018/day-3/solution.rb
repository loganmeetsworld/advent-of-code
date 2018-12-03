lines, square_dims = File.open("./input.txt").readlines.map(&:chomp).map(&:freeze).freeze, 1000

def build_square(dim)
    square = Array.new(dim)
    square.length.times{ |i| square[i] = Array.new(dim, '.') }
    return square
end

def parse(line)
    scan = line.scan(/(\d+)/).map(&:first)
    return {'id': scan[0], 'dist_from_left': scan[1].to_i, 'dist_from_top': scan[2].to_i, 'width': scan[3].to_i, 'height': scan[4].to_i}
end

square = build_square(square_dims)
claims = lines.map{ |x| parse(x) }

claims.each do |claim|
    (0...claim[:width]).to_a.each do |x|
        (0...claim[:height]).to_a.each do |y|
            if square[claim[:dist_from_top] + y][claim[:dist_from_left] + x] == '.'
                square[claim[:dist_from_top] + y][claim[:dist_from_left] + x] = claim[:id]
            else
                square[claim[:dist_from_top] + y][claim[:dist_from_left] + x] = 'X'
            end
        end
    end
end

puts "Part 1:"
puts square.flatten.count('X')

puts "Part 2:"
claims.each do |claim|
    part_two_found = true
    (0...claim[:width]).to_a.each do |x|
        (0...claim[:height]).to_a.each do |y|
            if square[claim[:dist_from_top] + y][claim[:dist_from_left] + x] == 'X'
                part_two_found = false
                break
            end
        end
    end
    puts claim[:id] if part_two_found
end
