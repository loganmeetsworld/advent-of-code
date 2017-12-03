require 'digest'
require 'pry'

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
  md5 = Digest::MD5.new
  key = thousand_ahead.keys.min_by{|x| x.match(/\d+/)[0].to_i }
  thousand_ahead.delete(key)
  last = key.gsub(/\d+/, '') + (key.match(/\d+/)[0].to_i + 1000).to_s
  thousand_ahead[last] = md5.hexdigest(last)
  thousand_ahead
end

def create_thousand_ahead(input)
  md5 = Digest::MD5.new
  thousand_ahead = Hash.new
  key = input + '2'

  1000.times do |i|
    thousand_ahead[key] = md5.hexdigest(key)
    key = inc(key)
  end
  thousand_ahead
end

md5 = Digest::MD5.new
input = 'ngcjuoqr'
thousand_ahead = create_thousand_ahead(input)
count = 0
key = input + '1'

until count == 64
  if three_in_a_row(md5.hexdigest(key)).any?
    if thousand_ahead.select{|k,v| five_in_a_row?(three_in_a_row(md5.hexdigest(key))[0], v)}.any?
      count += 1
      key = inc(key)
      thousand_ahead = shift_thousand(thousand_ahead)
    else
      key = inc(key)
      thousand_ahead = shift_thousand(thousand_ahead)
    end
  else
    key = inc(key)
    thousand_ahead = shift_thousand(thousand_ahead)
  end
end

puts "Part 1: #{(key.scan(/\d+/)[0].to_i - 1).to_s}"
