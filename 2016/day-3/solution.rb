input = File.open("./input.txt").read.strip.split("\n")
horizontal_triangles = input.map{|triangle| triangle.strip.split.map(&:to_i) }
vertical_triangles = horizontal_triangles.each_slice(3).flat_map{ |a, b, c| a.zip b, c }

def valid_triangle?(triangle)
  triangle.inject(:+).to_i - triangle.max.to_i > triangle.max.to_i ? true : false
end

puts 'Part 1: ' + horizontal_triangles.select{ |triangle| valid_triangle?(triangle) }.count.to_s
puts 'Part 2: ' + vertical_triangles.select{ |triangle| valid_triangle?(triangle) }.count.to_s
