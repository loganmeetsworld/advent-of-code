require 'digest'
md5 = Digest::MD5.new
passcode_part_1 = ''
passcode_part_2 = Array.new(8){ nil }
i = 0
door_id = 'ugkcyxxp'

8.times do
  until md5.hexdigest(door_id)[0..4] == '00000'
    i += 1
    door_id = 'ugkcyxxp' + i.to_s
  end
  passcode_part_1 << md5.hexdigest(door_id)[5]
  i += 1
  door_id = 'ugkcyxxp' + i.to_s
end

puts "Part 1: #{passcode_part_1}"

i = 0
door_id = 'ugkcyxxp'
while passcode_part_2.include? nil do
  until md5.hexdigest(door_id)[0..4] == '00000'
    i += 1
    door_id = 'ugkcyxxp' + i.to_s
  end
  position = md5.hexdigest(door_id)[5]
  if (position.to_i < 8) && (position.to_s == position.to_i.to_s)
    if passcode_part_2[position.to_i].nil?
      passcode_part_2[position.to_i] = md5.hexdigest(door_id)[6]
    end
    # puts "Passcode: #{passcode_part_2}"
    # puts "Position: #{position}"
  end
  i += 1
  door_id = 'ugkcyxxp' + i.to_s
end

puts "Part 2: #{passcode_part_2.join}"
