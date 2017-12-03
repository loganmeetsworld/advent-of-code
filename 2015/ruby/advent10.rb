require 'pry'
input = "1113222113"

# Next = 3113322113, to 40
# Next = 132123222113

def look_and_say(input, times)
  overall = 0

  while overall < times
    array = []

    input.split('').each_with_index do |s, i|
      count = 1
      index = 1
      if s != input[i - 1] || i == 0
        while s == input[i + index]
          count += 1
          index += 1
        end
        array << count.to_s + s
      end
    end
    overall += 1
    input = array.join("")
  end
  puts input.length

end

look_and_say(input, 40)
look_and_say(input, 50)