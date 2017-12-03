sum = 0 

def not_letters?(str)
  (str.include?("ab") || str.include?("cd") || str.include?("pq") || str.include?("xy")) ? false : true
end


def vowel?(str)
  (str.scan(/[aeiou]/).count >= 3) ? true : false
end

def double_letter?(str)
  trues = []

  str.split("").each_with_index do |e, i| 
    if e == str[i+1]
      trues << true
    end
  end

  trues.include?(true) ? true : false
end

def overall?(str)
  if not_letters?(str) && vowel?(str) && double_letter?(str)
    true 
  else
    false 
  end
end

# overall?("ugknbfddgicrmopn")
# overall?("aaa")
# overall?("jchzalrnumimnmhp")
# overall?("haegwjzuvuyypxyu")
# overall?("dvszwmarrgswjxmb")

text.split("\n").each do |t|
  overall?(t) ? sum+= 1 : sum+= 0
end

puts sum
