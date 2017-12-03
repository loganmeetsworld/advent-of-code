# josephus problem 
input = 3014387

binary = '0b' + input.to_s(2)[1..-1] + '1'

binary.to_i(2)
