def parse(lines)
    data = []
    lines.each do |line|
        x, y_start, y_end = line.scan(/\d+/).map(&:to_i)
        (y_start..y_end).to_a.map{ |y| data.push([x, y]) } if line.chars.first == 'x'
        (y_start..y_end).to_a.map{ |y| data.push([y, x]) } if line.chars.first == 'y'
    end
    return data
end

def build_grid(data)
    grid = []
    min_x, max_x = data.min_by{ |x| x[1] }[1], data.max_by{ |x| x[1] }[1]
    min_y, max_y = data.min_by{ |x| x[0] }[0] - 1, data.max_by{ |x| x[0] }[0] + 1

    (0..max_x).each do |i|
        tracker = []
        (0..max_y - min_y).each do |j|
            tracker.push('.')
        end
        grid.push(tracker)
    end

    # begin the water flow
    grid[0][500 - min_y] = '+'
    data.each do |d|
        grid[d[1]][d[0] - min_y] = '#'
    end

    return grid
end

def let_the_water_fall_where_it_may(grid, data)
    unvisited = [[1, 500]]
    min_x, max_x = data.min_by{ |x| x[1] }[1], data.max_by{ |x| x[1] }[1]
    min_y, max_y = data.min_by{ |x| x[0] }[0] - 1, data.max_by{ |x| x[0] }[0] + 1

    while unvisited.length > 0
        next_location = unvisited.pop
        grid[next_location[0]][next_location[1] - min_y] = '|' if grid[next_location[0]][next_location[1] - min_y] == '.'
        next if next_location[0] == max_x

        if grid[next_location[0] + 1][next_location[1] - min_y] == '.'
            unvisited.push([next_location[0] + 1, next_location[1]])
            next
        elsif ['~', '#'].include?(grid[next_location[0] + 1][next_location[1] - min_y])
            unvisited.push([next_location[0],next_location[1] + 1]) if grid[next_location[0]][next_location[1] - min_y + 1] == '.'
            unvisited.push([next_location[0],next_location[1] - 1]) if grid[next_location[0]][next_location[1] - min_y - 1] == '.'

            if ['|','#'].include?(grid[next_location[0]][next_location[1] - min_y + 1]) && ['|','#'].include?(grid[next_location[0]][next_location[1]-min_y-1])
                flag, tracker = true, next_location[1]
                tracker += 1 while ['|','~'].include?(grid[next_location[0]][tracker - min_y + 1])
                next if grid[next_location[0]][tracker - min_y + 1] != '#'
                tracker = next_location[1]
                tracker -= 1 while ['|','~'].include?(grid[next_location[0]][tracker - min_y - 1])
                next if grid[next_location[0]][tracker - min_y - 1] != '#'
                tracker = next_location[1]
                grid[next_location[0]][tracker - min_y] = '~'
                unvisited.push([next_location[0] - 1, tracker]) if grid[next_location[0]-1][tracker - min_y] == '|'

                while ['|','~'].include?(grid[next_location[0]][tracker - min_y + 1])
                    grid[next_location[0]][tracker - min_y + 1] = '~'
                    tracker += 1
                    unvisited.push([next_location[0] - 1,tracker]) if grid[next_location[0] - 1][tracker-min_y] == '|'
                end

                while ['|','~'].include?(grid[next_location[0]][tracker - min_y - 1])
                    grid[next_location[0]][tracker - min_y - 1] = '~'
                    tracker -= 1
                    unvisited.push([next_location[0] - 1, tracker]) if grid[next_location[0] - 1][tracker - min_y] == '|'
                end
            end
        end
    end
    return grid
end

lines = File.open('input.txt').readlines.map(&:chomp)
data = parse(lines)
grid = build_grid(data)
final_grid = let_the_water_fall_where_it_may(grid, data)
puts final_grid.flatten.count('|') + final_grid.flatten.count('~')
puts final_grid.flatten.count('~')