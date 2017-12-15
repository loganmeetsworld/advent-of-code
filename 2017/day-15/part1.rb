a, b, a_fac, b_fac, DIV, PAIRS, count = 634, 301, 6807, 48271, 2147483647, 5000000, 0

PAIRS.times do
  a, b = (a * a_fac) % DIV, (b * b_fac) % DIV
  if a.to_s(2)[a.to_s(2).length-16..-1].to_i & b.to_s(2)[a.to_s(2).length-16..-1].to_i then count += 1 end
end

puts count