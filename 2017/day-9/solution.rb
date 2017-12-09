require 'test/unit'
extend Test::Unit::Assertions

def calculate_scores(stream)
  total_score, level_score, gc, garbage, bang = 0, 0, 0, false, false

  stream.chars do |char|
    if bang then next bang = false end
    if garbage
      case char
      when '!'
        bang = true
      when '>'
        garbage = false
      else
        if garbage then gc += 1 end
      end
    else
      case char
      when '{'
        total_score += level_score += 1
      when '}'
        level_score -= 1
      when '<'
        garbage = true
      end
    end
  end
  return total_score, gc
end

assert_equal calculate_scores('{}').first, 1
assert_equal calculate_scores('{{{}}}').first, 6
assert_equal calculate_scores('{{},{}}').first, 5
assert_equal calculate_scores('{{{},{},{{}}}}').first, 16
assert_equal calculate_scores('{<a>,<a>,<a>,<a>}').first, 1
assert_equal calculate_scores('{{<ab>},{<ab>},{<ab>},{<ab>}}').first, 9
assert_equal calculate_scores('{{<!!>},{<!!>},{<!!>},{<!!>}}').first, 9
assert_equal calculate_scores('{{<a!>},{<a!>},{<a!>},{<ab>}}').first, 3
assert_equal calculate_scores('<>').last, 0
assert_equal calculate_scores('<random characters>').last, 17
assert_equal calculate_scores('<<<<>').last, 3
assert_equal calculate_scores('<{!>}>').last, 2
assert_equal calculate_scores('<!!>').last, 0
assert_equal calculate_scores('<!!!>>').last, 0
assert_equal calculate_scores('<{o"i!a,<{i<a>').last, 10

stream = File.open("./input.txt").read
puts calculate_scores(stream)
