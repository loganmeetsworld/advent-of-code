puts "Part 1:"
puts File.open("./input.txt").readlines.map(&:to_i).inject(&:+)

puts "Part 2:"
require 'set'
changes = File.open("./input.txt").readlines
current_freq = 0
freq_tracker = Set.new([current_freq])
found = nil

until found
    for c in changes
        current_freq += c.to_i
        if freq_tracker.include?(current_freq)
            found = current_freq
            break
        end
        freq_tracker.add(current_freq)
    end
end

puts found