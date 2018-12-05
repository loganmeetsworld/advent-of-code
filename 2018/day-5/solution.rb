def remove_reactions(input)
    stack = [input.shift]
    input.each do |char|
        next if char == nil || stack.empty?
        # check if the difference in character code indicates capitalization
        (stack.last.ord - char.ord).abs == 32 ? stack.pop : stack.push(char)
    end
    return stack
end

def remove_units(l, polymer)
    return polymer.gsub(l, '').gsub(l.upcase, '')
end

input = File.open("./input.txt").read.chomp

puts "Part 1:"
puts remove_reactions(input.dup.chars).length

puts "Part 2:"
lengths = []
('a'..'z').each do |l|
    polymer = remove_units(l, input.dup)
    polymer = remove_reactions(polymer.chars)
    lengths.push(polymer.length) unless polymer.length == 0
end
puts lengths.min
