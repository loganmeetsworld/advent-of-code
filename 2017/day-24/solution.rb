require 'set'

def possible_bridges(start, components)
  components_set = Set.new()
  return components_set if components.empty?
  possible_starting_components = components.select{|c| c[0] == start || c[1] == start }
  possible_starting_components.each do |comp|
    components_set.add(comp)
    next_comp = comp.first == start ? comp.last : comp.first
    following = possible_bridges(next_comp, components.select{|c| c != comp})
    following.each do |remaining|
      components_set.add([comp] + remaining)
    end
  end
  components_set
end

def calculate_strength(bridge)
  bridge.flatten.inject(&:+)
end

def strongest_bridge(possible_bridges)
  possible_bridges.map{ |bridge| calculate_strength(bridge) }.max
end

def longest_bridge(possible_bridges)
  max_length = possible_bridges.max_by(&:length).length
  all_with_max_length = possible_bridges.find_all{|x| x.length == max_length}
  strongest_bridge(all_with_max_length)
end

components = File.open('input.txt').read.lines.map(&:strip).map{|l| l.split('/').map(&:to_i)}
possible_bridges = possible_bridges(0, components)
puts "Part 1: #{strongest_bridge(possible_bridges)}"
puts "Part 2: #{longest_bridge(possible_bridges)}"