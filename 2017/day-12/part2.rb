require 'rgl/adjacency'
require 'rgl/connected_components'

input = File.open('input.txt').read.split("\n")
dg=RGL::DirectedAdjacencyGraph[]

input.each do |l|
  node, neighbors = l.split(' <-> ')
  for n in neighbors.split(', ')
    dg.add_edge node.to_i, n.to_i
  end
end

connected_components = []
dg.to_undirected.each_connected_component { |c| connected_components <<  c }
puts "Part 2: #{connected_components.length}"