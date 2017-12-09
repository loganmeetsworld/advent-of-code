require 'test/unit'
extend Test::Unit::Assertions

def calculate_score(chars)
  total_score = 0
  group_score = 1
  i = 0

  chars.length.times do
    case chars[i]
    when '!'
      i += 2
    when '{'
      total_score += group_score
      group_score += 1
      i += 1
    when '}'
      group_score -= 1
      i += 1
    else
      i += 1
    end
  end
  return total_score
end

assert_equal calculate_score('{}'), 1
assert_equal calculate_score('{{{}}}'), 6
assert_equal calculate_score('{{},{}}'), 5
assert_equal calculate_score('{{{},{},{{}}}}'), 16
assert_equal calculate_score('{<a>,<a>,<a>,<a>}'), 1
assert_equal calculate_score('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9
assert_equal calculate_score('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9
assert_equal calculate_score('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3

chars = File.open("./input.txt").read.split('')
calculate_score(chars)
