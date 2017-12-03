input = File.open("./input.txt").read.split("\n")
part_1_count, part_2_count = 0, 0

def format_strings(code)
  regexp = /\[(.*?)\]/
  return code.gsub(regexp, ',').split(','), code.scan(regexp).flatten
end

def abba?(s)
  regexp = /(.)((?!\1).)\2\1/
  !regexp.match(s).nil?
end

def contains_abba?(str_array)
  str_array.select{ |s| abba?(s) }.length > 0
end

def supports_TLS(obj)
  contains_abba?(obj[0]) && !contains_abba?(obj[1])
end

def abas(str_arr)
  abas_hash = {}
  str_arr.each do |s|
    s.split('').each_with_index do |c, i|
      unless s[i + 2] == nil
        if s[i] == s[i + 2]
          abas_hash[s[i..i+2]] = s[i + 1] + s[i] + s[i + 1]
        end
      end
    end
  end
  return abas_hash
end

def supports_SSL(obj)
  out_abas = abas(obj[0])
  in_abas = abas(obj[1])

  out_abas.each do |k,v|
    if !in_abas[v].nil?
      return true
    end
  end
  return false
end

part_1_count = input.map{ |code| format_strings(code) }.select{ |str_obj| supports_TLS(str_obj) }.length
part_2_count = input.map{ |code| format_strings(code) }.select{ |str_obj| supports_SSL(str_obj) }.length

puts "Part 1: #{part_1_count}"
puts "Part 2: #{part_2_count}"
