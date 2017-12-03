require 'digest'

day_1_zeros = 5
day_2_zeros = 6
input = "iwrupvqb"

0.step do |number|
  if Digest::MD5.new.hexdigest("#{input}#{number.to_s}")[0, day_2_zeros] == '0' * day_2_zeros
    puts number
    break
  end
end