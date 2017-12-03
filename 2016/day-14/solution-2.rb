require 'digest'

def three_in_a_row(hex)
  hex.scan(/(.)\1\1/).flatten
end

def five_in_a_row?(letter, hex)
  !hex.match(/(#{letter.to_s})\1\1\1\1/).nil?
end

def inc(key)
  key.gsub(/\d+/, '') + (key.match(/\d+/)[0].to_i + 1).to_s
end

def shift_thousand(thousand_ahead)
  key = thousand_ahead.keys.min_by{|x| x.match(/\d+/)[0].to_i }
  thousand_ahead.delete(key)
  last = key.gsub(/\d+/, '') + (key.match(/\d+/)[0].to_i + 1000).to_s
  thousand_ahead[last] = strech_hash(last)
  thousand_ahead
end

def create_thousand_ahead(input)
  thousand_ahead = Hash.new
  key = input + '1'

  1000.times do |i|
    thousand_ahead[key] = strech_hash(key)
    key = inc(key)
  end
  thousand_ahead
end

def create_reference(input)
  thousand_ahead = Hash.new
  key = input + '0'

  1001.times do |i|
    thousand_ahead[key] = strech_hash(key)
    key = inc(key)
  end
  thousand_ahead
end

def strech_hash(key)
  md5 = Digest::MD5.new
  
  2017.times do |i|
    key = md5.hexdigest(key)
  end
  key
end

input = 'ngcjuoqr'
thousand_ahead = create_thousand_ahead(input)
reference = create_reference(input)
count = 0
key = 'ngcjuoqr0'

until count == 64
  if three_in_a_row(reference[key]).any?
    if thousand_ahead.select{|k,v| five_in_a_row?(three_in_a_row(reference[key])[0], v)}.any?
      count += 1
      key = inc(key)
      thousand_ahead = shift_thousand(thousand_ahead)
      reference[key] = strech_hash(key)
    else
      key = inc(key)
      thousand_ahead = shift_thousand(thousand_ahead)
      reference[key] = strech_hash(key)
    end
  else
    key = inc(key)
    thousand_ahead = shift_thousand(thousand_ahead)
    reference[key] = strech_hash(key)
  end
end

puts "Part 2: #{(key.scan(/\d+/)[0].to_i - 1).to_s}"
