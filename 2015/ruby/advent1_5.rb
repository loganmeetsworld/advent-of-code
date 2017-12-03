count = 0
File.read('inputs/day1').chars.reduce(0) do |curr, char|
  if curr == -1
    break 
  end

  count = count + 1
  curr + (char == '(' ? 1 : -1)
end

puts count