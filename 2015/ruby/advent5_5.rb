def pairs?(str)
  combos = []

  str.split("").each_with_index do |e, i|
    combos << [e, str[i + 1]]
  end

  doubles = combos.detect{ |c| combos.count(c) > 1 }

  doubles.nil? ? false : true
end

def between?(str)
  triples = []

  str.split("").each_with_index do |e, i|
    triples << [e, str[i + 1], str[i + 2]]
  end

  trues = []

  triples.each do |t|
    if t[0] == t[2]
      trues << true 
    else
      trues << false
    end
  end

  trues.include?(true) ? true : false
end

def overall?(str)
  if pairs?(str) && between?(str)
    true 
  else
    false 
  end
end

sum = 0

text = File.read('inputs/day5.txt')

text.split("\n").each do |t|
  if pairs?(t) == true
    sum += 1
  else
    sum += 0
  end
end

puts sum
