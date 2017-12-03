
sum = 1

text.gsub!("^>v<", "4")
text.gsub!("^v", "i")
text.gsub!("><", "i")
text.gsub!("<", "1")
text.gsub!(">", "1")
text.gsub!("v", "1")
text.gsub!("^", "1")



bleh = 0

text.split("").each do |t| 
  if t == "4"
    sum += 4
  elsif t == "1"
    sum += 1
  end
end


text.split("").each_with_index { |element, index| 
  if index == 0
    previous_element = nil
  else 
    previous_element = text[index-1]
  end
  if (element == "i") && (previous_element != "i")
    sum+= 1
  end
}




