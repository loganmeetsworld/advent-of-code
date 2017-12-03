a = '11101000110010100'
desired_length = 272
desired_length_2 = 35651584

def fill_disk(a, length)
  until a.length >= length
    b = a
    b = b.reverse
    b = b.tr('10', '01')
    a = a + '0' + b
  end
  return a
end

def matching?(pair)
  pair[0] == pair[1]
end

def generate_checksum(data)
  if data.length % 2 != 0
    return data
  else
    generate_checksum(data.scan(/../).map{|d| matching?(d) ? '1' : '0' }.join(''))
  end
end

data = fill_disk(a,desired_length).slice(0,desired_length)
data_2 = fill_disk(a,desired_length_2).slice(0,desired_length_2)
puts "Part 1: #{generate_checksum(data)}"
puts "Part 2: #{generate_checksum(data_2)}"
