# input = 'dabAcCaCBAcCcaDA'
input = File.open("./input.txt").read.chomp

def polymer?(s1, s2)
    return false if /[[:upper:]]/.match(s1) and /[[:upper:]]/.match(s2)
    return if s1 == nil or s2 == nil
    s1 == s2.upcase || s2 == s1.upcase
end

puts "Part 1:"
while true
    length = input.length
    for i in (0...input.length).to_a
        if polymer?(input[i], input[i + 1])
            input.slice!(input[i] + input[i + 1])
            break
        end
    end
    if input.length == length
        break
    end
end

puts input.length

puts "Part 2:"