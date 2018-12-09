input = File.open('input.txt').read.split(' ').map(&:to_i).map(&:freeze)
# input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ').map(&:to_i).map(&:freeze)

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

puts sum_metadata(input)