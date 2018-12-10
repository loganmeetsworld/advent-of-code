def answer(players, points)
    current_pos, marble, count, player_scores, board, stop = 0, 0, 0, Hash.new(0), [], false
    while !stop
        (0...players).each do |player|
            if marble % 23 == 0 && marble != 0
                player_scores[player] += marble
                board = board.rotate(current_pos - 7)
                player_scores[player] += board.shift
                current_num = board[0]
                board = board.rotate(board.index(0))
                current_pos = board.index(current_num)
                count += 1
            else
                board = board.rotate(current_pos + 2)
                board.push(marble)
                board = board.rotate(board.index(0))
                current_pos = board.index(marble)
            end
            marble += 1
            stop = true if marble >= points
        end
    end
    return player_scores.values.max
end

input = File.open('input.txt').read
players, points = input.scan(/(\d+)/).map(&:first).map(&:to_i)

puts "Part 1: "
puts Time.now
puts answer(players, points)
puts Time.now

puts "Part 2: "
puts answer(players, points * 100)
