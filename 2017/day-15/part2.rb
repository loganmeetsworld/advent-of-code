a, b, a_fac, b_fac, DIV, mult_a, mult_b, PAIRS, count = 634, 301, 16807, 48271, 2147483647, 4, 8, 5000000, 0

def generator(num, fact, div, mult)
  matches = []
  until matches.length == PAIRS
    num = (num * fact) % div
    matches << num if num % mult == 0
  end
  return matches
end

a = generator(a, a_fac, DIV, mult_a)
b = generator(b, b_fac, DIV, mult_b)

a.zip(b).map { |x, y| if x.to_s(2).split('').last(16).join == y.to_s(2).split('').last(16).join then count += 1 end }

puts count