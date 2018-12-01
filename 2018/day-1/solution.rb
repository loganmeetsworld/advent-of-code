puts "Part 1:"
puts File.open("./input.txt").readlines.map(&:to_i).inject(&:+)

puts "Part 2:"
require 'set'
changes, current_freq, freq_tracker, found = File.open("./input.txt").readlines, 0, Set.new([current_freq]), nil

until found
    for c in changes
        current_freq += c.to_i
        if freq_tracker[current_freq]
            found = current_freq
            break
        end
        freq_tracker.add(current_freq)
    end
end

puts found