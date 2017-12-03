require 'pry'
input = File.read('inputs/day14.txt')

@hash = Hash.new { |k, v| k[v] = {} }

input.each_line.map do |line|
  line = line.scan(/(\w+).+ (\d+).+? (\d+).+? (\d+).+?\./)
  deer, speed, flight_time, rest_time = line[0][0], line[0][1], line[0][2], line[0][3]

  @hash[deer] = speed, flight_time, rest_time
end

def calc_finish(hash)
  distances_at_end = []
  hash.each do |k, v|
    seconds = 2503
    distance = 0
    while seconds >= 0
      seconds -= v[1].to_i
      if seconds < 0
        flight_remaining = seconds + v[1].to_i
        distance += (v[0].to_i * flight_remaining)
        # binding.pry
        break
      end
      distance += v[0].to_i * v[1].to_i
      seconds -= v[2].to_i
    end

    distances_at_end << [k, distance.to_i]
  end

  puts distances_at_end

end

calc_finish(@hash)