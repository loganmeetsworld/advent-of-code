input = File.open("./input.txt").read.split("\n")
weights, node_hash = {}, {}
BAD_NODE_WEIGHTS = []
require('./part_1.rb')

input.each do |l|
  id = l.split[0]
  w  = l.match(/\d+/)[0]
  weights[id] = w.to_i
  if l.include?('->')
    childrens = l.split('->')[1].split(',').map(&:strip)
    node_hash[id] = childrens
  end
end

def create_graph(node, node_hash, weights)
  childrens = node_hash[node]
  arr = []
  childrens.each do |c|
    if node_hash.keys.include?(c)
      w = create_graph(c, node_hash, weights)
      v = w.inject(&:+) + weights[c]
    else
      v = weights[c]
    end
    arr << v
  end

  if arr.uniq.length != 1
    index_of_bad_node = arr.each_with_index.max[1]
    index_of_good_node = arr.each_with_index.min[1]
    bad_node = node_hash[node][index_of_bad_node]
    bad_node_weight = weights[bad_node]
    BAD_NODE_WEIGHTS << bad_node_weight
  end

  return arr
end

g = create_graph(part_1, node_hash, weights)
puts BAD_NODE_WEIGHTS.min - (g.max - g.min)