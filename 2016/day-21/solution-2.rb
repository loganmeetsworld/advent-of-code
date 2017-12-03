require 'pry'

def un_swap_letter(password, letter_y, letter_x)
  position_x = password.index(letter_x)
  position_y = password.index(letter_y)

  password[position_x] = letter_y
  password[position_y] = letter_x
  return password
end

def un_swap_position(password, position_y, position_x)
  letter_x = password[position_x.to_i]
  letter_y = password[position_y.to_i]

  password[position_y.to_i] = letter_x
  password[position_x.to_i] = letter_y
  return password
end

def un_rotate(password, dir, num_steps)
  dir_num = dir == 'left' ? -1 : 1
  return password.split('').rotate!(dir_num * num_steps.to_i).join('')
end

def un_rotate_based(password, letter)
  password = password.split('')
  letter_index = password.index(letter)

  steps = letter_index / 2
    if letter_index % 2 == 1 || letter_index == 0
      steps += 1
    else
      steps += 5
    end

  return password.rotate(steps).join
end

def un_reverse(password, position_x, position_y)
  password[position_x.to_i..position_y.to_i] = password[position_x.to_i..position_y.to_i].reverse
  return password
end

def un_move(password, position_y, position_x)
  password = password.split('')
  return password.insert(position_y.to_i, password.delete_at(position_x.to_i)).join('')
end

def un_scramble_pass(input, password)
  input.each do |i|
    i = i.split(' ')
    keyword = i[0]
    sub_keyword = i[1]

    case keyword
    when 'swap'
      case sub_keyword
      when 'letter'
        password = un_swap_letter(password, i[2], i[5])
      else
        password = un_swap_position(password, i[2], i[5])
      end
    when 'reverse'
      password = un_reverse(password, i[2], i[4])
    when 'move'
      password = un_move(password, i[2], i[5])
    when 'rotate'
      case sub_keyword
      when 'based'
        password = un_rotate_based(password, i[-1])
      else
        password = un_rotate(password, i[1], i[2])
      end
    end
  end
  return password
end

input = File.open("./input.txt").readlines.reverse!
password = 'fbgdceah'
puts 'Part 2: ' + un_scramble_pass(input, password)
