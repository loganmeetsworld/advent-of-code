require 'pry'

def swap_letter(password, letter_x, letter_y)
  position_x = password.index(letter_x)
  position_y = password.index(letter_y)

  password[position_x] = letter_y
  password[position_y] = letter_x
  return password
end

def swap_position(password, position_x, position_y)
  letter_x = password[position_x.to_i]
  letter_y = password[position_y.to_i]

  password[position_y.to_i] = letter_x
  password[position_x.to_i] = letter_y
  return password
end

def rotate(password, dir, num_steps)
  dir_num = dir == 'right' ? -1 : 1
  return password.split('').rotate!(dir_num * num_steps.to_i).join('')
end

def rotate_based(password, letter)
  password = password.split('')
  letter_index = password.index(letter)
  puts 'i: ' + letter_index.to_s
  letter_index += 1 if letter_index >= 4
  letter_index += 1
  puts 'steps: ' + letter_index.to_s
  return password.rotate!(-1 * letter_index).join('')
end

def reverse(password, position_x, position_y)
  password[position_x.to_i..position_y.to_i] = password[position_x.to_i..position_y.to_i].reverse
  return password
end

def move(password, position_x, position_y)
  password = password.split('')
  return password.insert(position_y.to_i, password.delete_at(position_x.to_i)).join('')
end

def scramble_pass(input, password)
  input.each do |i|
    i = i.split(' ')
    keyword = i[0]
    sub_keyword = i[1]

    case keyword
    when 'swap'
      case sub_keyword
      when 'letter'
        password = swap_letter(password, i[2], i[5])
      else
        password = swap_position(password, i[2], i[5])
      end
    when 'reverse'
      password = reverse(password, i[2], i[4])
    when 'move'
      password = move(password, i[2], i[5])
    when 'rotate'
      case sub_keyword
      when 'based'
        password = rotate_based(password, i[-1])
      else
        password = rotate(password, i[1], i[2])
      end
    end
  end
  return password
end

input = File.open("./input.txt").readlines
password = 'abcdefgh'
puts 'Part 1: ' + scramble_pass(input, password)
