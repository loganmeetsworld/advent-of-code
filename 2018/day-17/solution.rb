def parse(lines)
    data = []
    lines.each do |line|
        x, y_start, y_end = line.scan(/\d+/).map(&:to_i)
        (y_start..y_end).to_a.map{ |y| data.push([x, y]) } if line.chars.first == 'x'
        (y_start..y_end + 1).to_a.map{ |y| data.push([y, x]) } if line.chars.first == 'y'
    end
    return data
end

def build_grid(data)
    grid = []
    min_x = data.min_by{ |x| x[1] }[1]
    max_x = data.max_by{ |x| x[1] }[1]
    min_y = data.min_by{ |x| x[0] }[0] - 1
    max_y = data.max_by{ |x| x[0] }[0] + 1

    (0..max_x + 1).each do |i|
        tmp = []
        (0..max_y - min_y + 1).each do |j|
            tmp.push('.')
        end
        grid.push(tmp)
    end

    grid[0][500-min_y] = '+'
    data.each do |d|
        grid[d[1]][d[0] - min_y] = '#'
    end

    return grid
end

# lines = File.open('input.txt').readlines.map(&:chomp)
lines = "x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504".split("\n").map(&:chomp)
data = parse(lines)
graph = build_grid(data)
puts graph.to_s