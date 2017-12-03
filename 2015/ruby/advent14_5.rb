class Deer

  attr_accessor :name, :speed, :flight_time, :rest_time

  def initialize(name, speed, flight_time, rest_time)
    @name = name  
    @speed = speed
    @flight_time = flight_time
    @rest_time = rest_time
  end

  def distance_at(time)
    cyc, sec_passed = time.divmod(@flight_time + @rest_time)
    full_cyc = cyc * @flight_time * @speed
    flight_time_cyc = [sec_passed, @flight_time].min
    curr_cyc = flight_time_cyc * @speed
    full_cyc + curr_cyc
  end
end

input = File.read('inputs/day14.txt')

@deers = input.each_line.map do |line|
  line = line.scan(/(\w+).+ (\d+).+? (\d+).+? (\d+).+?\./)
  Deer.new(line[0][0], line[0][1].to_i, line[0][2].to_i, line[0][3].to_i
  )
end

def best_dist(time)
  distances = @deers.map do |d|   
    d.distance_at(time)
  end

  return distances.max
end

points = {}
(1..2503).each do |time|
  best_distance = best_dist(time)
  @deers.each do |d|
    if d.distance_at(time) == best_distance
      points[d.name] ||= 0
      points[d.name] += 1
    end
  end
end

puts points.values.max
