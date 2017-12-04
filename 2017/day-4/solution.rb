require 'set'
require 'test/unit'
extend Test::Unit::Assertions

def count_valid(passwords)
    part_1_valid_count, part_2_valid_count = 0, 0
    
    passwords.each do |pass|
        words = pass.split(' ')
        if part_1_valid?(words) then part_1_valid_count += 1 end
        if part_2_valid?(words) then part_2_valid_count += 1 end
    end
    return [part_1_valid_count, part_2_valid_count]
end

def part_2_valid?(words)
    set = Set.new()
    words.each do |w|
        set << w.chars.sort.join
    end

    return words.length == set.length
end

def part_1_valid?(words)
    set = Set.new()
    words.each do |w|
        set << w
    end

    return words.length == set.length
end


passwords = File.open("./input.txt").read.split("\n")
valid = count_valid(passwords)

puts valid[0]
puts valid[1]

assert_equal part_1_valid?('aa bb cc dd aaa'), true
assert_equal part_1_valid?('aa bb cc dd ee'), true
assert_equal part_1_valid?('aa bb cc dd aa'), false

assert_equal part_2_valid?('abcde fghij'), true
assert_equal part_2_valid?('abcde xyz ecdab'), false
assert_equal part_2_valid?('a ab abc abd abf abj'), true
assert_equal part_2_valid?('iiii oiii ooii oooi oooo'), true
assert_equal part_2_valid?('oiii ioii iioi iiio'), false
