def dimensions(coords)
  return coords.max_by(&:first).max, coords.max_by(&:last).max
end

def find_shortest_distance(p1, p2)
  return (p1[0] - p2[0]).abs + (p1[1] - p2[1]).abs
end

puts 'Part 1:'
region_size = 10000
region_count = 0
coords = File.open('input.txt').readlines.map{ |c| c.split(', ').map(&:to_i) }
max_x, max_y = dimensions(coords)
area_counts = Array.new(coords.size, 0)
infinite_coords = []

max_x.times do |x|
  max_y.times do |y|
    distances = {}
    total_dist = 0
    point = [x, y]
    coords.each_with_index do |coord, idx|
      dist = find_shortest_distance(point, coord)
      distances[idx] = dist
      total_dist += dist
    end
    min_coords = distances.select { |idx, dist| dist == distances.values.min }
    min_coord_idx = min_coords.keys.first

    if total_dist < region_size
      region_count += 1
    end

    if min_coords.size == 1
      area_counts[min_coord_idx] += 1

      if x == 0 || y == 0 || x == max_x || y == max_y
        infinite_coords.push(min_coord_idx)
      end
    end
  end
end

infinite_coords.each{ |i| area_counts[i] = 0 }

puts area_counts.max

puts "Part 2:"
puts region_count
