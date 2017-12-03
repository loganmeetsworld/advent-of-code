def decompress_1(str)
  decompressed_length = 0
  until str == ''
    if detect_marker(str)
      decompressed_length += calculate_marker(str).inject(:*)
      update_str(str)
    else
      decompressed_length += 1
      str.slice!(0)
    end
  end
  return decompressed_length
end

def decompress_2(str)
  decompressed_length = 0
  until str == ''
    if detect_marker(str)
      marker = detect_marker(str)[1]
      substring = str[(marker.length + 2)...((marker.length + 2) + calculate_marker(str)[0])]
      decompressed_length += decompress_2(substring) * calculate_marker(str)[1]
      str = str[(calculate_marker(str)[0] + marker.length + 2)..-1]
    else
      decompressed_length += 1
      str.slice!(0)
    end
  end
  decompressed_length 
end

def update_str(str)
  instruction = detect_marker(str)[1]
  repeat_str_length = instruction.split('x')[0].to_i
  idx = repeat_str_length + instruction.length + 2
  str.slice!(0, idx)
end

def detect_marker(str)
  regex = /^\((.*?)\)/
  str.match(regex)
end

def calculate_marker(str)
  instruction = detect_marker(str)[1]
  repeat_times = instruction.split('x')[1].to_i
  repeat_str_length = instruction.split('x')[0].to_i
  [repeat_str_length, repeat_times]
end

input = File.open("./input.txt").read.strip
puts "Part 1: " + decompress_1(input).to_s

input = File.open("./input.txt").read.strip
puts "Part 2: " + decompress_2(input).to_s
