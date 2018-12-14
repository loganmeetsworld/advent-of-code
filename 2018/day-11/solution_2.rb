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
    grid = [0] * (300 * 300)
    (1..300).each do |x|
      (1..300).each do |y|
        grid[y * 300 + x] = power(x, y, grid_serial_number)
      end
    end
    return grid
  end

  def find_max_area(grid)
    best_sum, best_coord = -10000, [0, 0]
    (1..300).each do |size_boxes|
      puts size_boxes
      (1..300 - size_boxes).each do |x|
        (1..300 - size_boxes).each do |y|
          sum = 0
          (0..size_boxes - 1).each do |dx|
            (0..size_boxes - 1).each do |dy|
              sum += grid[(dy + y) * 300 + dx + x]
            end
          end
          if sum > best_sum
            puts "#{x}, #{y}, #{size_boxes}: #{sum}"
            best_sum = sum
          end
        end
      end
    end
  end

  grid_serial_number = 1308
  grid = build_grid(grid_serial_number)
  puts find_max_area(grid)