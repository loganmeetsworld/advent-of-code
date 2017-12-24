# This helped me immensely, thank you @mjgpy3!:
# https://www.youtube.com/watch?v=AqXTZo6o34s

a, b, c, d, e, f, g, h = 1, 107900, 124900, 0, 0, 0, 0, 0

while true
  f, d = true, 2
  while d < b
    if b % d == 0 then f = false; break end; d += 1
  end

  h += 1 if !f; break if b == c; b += 17
end

puts "Part 2: #{h}"