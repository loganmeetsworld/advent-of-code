def answer(players, points)
    current_pos, marble, player_scores, board, stop = 0, 0, Hash.new(0), [], false
    while true
        break if marble == points
        (0...players).each do |player|
            if marble % 23 == 0 && marble != 0
                board = board.rotate(current_pos - 7)
                player_scores[player] += marble + board.shift
                current_num = board[0]
                board = board.rotate(-1)
                current_pos = board.index(current_num)
            else
                board = board.rotate(current_pos + 2)
                board.push(marble)
                board = board.rotate(-1)
                current_pos = board.index(marble)
            end
            marble += 1
            break if marble == points
        end
    end
    return player_scores.values.max
end

puts "Part 1: "
puts answer(413, 71082)

puts "Part 2: "
puts answer(413, (71082 * 100))
