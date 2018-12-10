def sum_metadata(input)
    metadata = 0
    num_nodes = input.shift
    num_metadata = input.shift
    num_nodes.times do
        metadata += sum_metadata(input)
    end
    metadata += input.slice!(0, num_metadata).inject(&:+)
    return metadata
end

puts "Part 1:"
input = File.open('input.txt').read.split(' ').map(&:to_i).map(&:freeze)
puts sum_metadata(input)

def find_node_value(input)
    num_nodes = input.shift
    num_metadata = input.shift
    node_sums = (0...num_nodes).map{ find_node_value(input) }

    if num_nodes == 0
        (0...num_metadata).map{ input.shift }.inject(&:+)
    else
        node_value = 0
        num_metadata.times do
            metadata = input.shift - 1
            node_value += node_sums[metadata] if metadata < num_nodes
        end
        node_value
    end
end

puts "Part 2:"
input = File.open('input.txt').read.split(' ').map(&:to_i).map(&:freeze)
puts find_node_value(input)