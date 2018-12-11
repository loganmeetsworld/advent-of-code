def power(x, y, grid_serial_number)
    rack_id = x + 10
    power = rack_id * y
    power += grid_serial_number
    power *= rack_id
    power = power.to_s.chars.map(&:to_i)[-3]
    power -= 5
    return power
end

def build_grid(grid_serial_number)
    grid = Hash.new(0)
    (1..300).each do |x|
        (1..300).each do |y|
            grid[[x, y]] = power(x, y, grid_serial_number)
        end
    end
    return grid
end

def find_max_area(grid)
    best_sum = -10000
    size = 0
    (1..300).each do |x|
        (1..300).each do |y|
            coords = [[x, y], [x, y + 1], [x, y + 2], [x + 1, y], [x + 2, y], [x + 1, y + 1], [x + 1, y + 2], [x + 2, y + 1], [x + 2, y + 2]]
            sum = coords.map{ |c| grid[c] }.inject(&:+)
            if sum > best_sum
                best_sum = sum
                best_coord = [x, y]
                puts best_sum
                puts best_coord.to_s
            end
        end
    end
end

grid_serial_number = 1308
grid = build_grid(grid_serial_number)
find_max_area(grid)