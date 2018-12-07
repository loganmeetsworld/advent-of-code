require 'rgl/adjacency'
require 'rgl/connected_components'
require 'rgl/dot'
require 'rgl/topsort'
require 'graphviz'

puts 'Part 1:'

input = File.open('input.txt').readlines
steps = input.map{ |s| s.scan(/\s(\w{1})\s/).flatten}
dg=RGL::DirectedAdjacencyGraph[]
steps.each{ |s1, s2| dg.add_edge s1, s2 }
available = []
s = ''
stb = dg.topsort_iterator.set_to_begin

min = stb.map{ |x| stb[x] }.min
available = stb.select{ |x| stb[x] == min }.keys
available = available.sort
next_available = available.shift
s += next_available

while true
  available += dg.adjacent_vertices(s[-1])
  min = available.map{ |x| stb[x] }.min
  available = available.select{ |x| stb[x] == min }
  available = available.sort
  next_available = available.shift
  s += next_available

  if s.length == steps.flatten.uniq.length
    break
  end
end

puts s


# nice little visualization of what's happening
dg.write_to_graphic_file('jpg')
