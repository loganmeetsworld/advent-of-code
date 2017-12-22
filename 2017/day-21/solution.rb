def find_rule_in_light_rule_hash(light_rule_hash, light_data)
  return light_rule_hash[light_data] || 
  light_rule_hash[light_data.map(&:reverse)] || 
  light_rule_hash[light_data.reverse.map(&:reverse)] || 
  light_rule_hash[light_data.reverse.map(&:reverse)] || 
  light_rule_hash[light_data.map(&:chars).transpose.map(&:join)] || 
  light_rule_hash[light_data.map(&:chars).transpose.map(&:join).reverse] || 
  light_rule_hash[light_data.map(&:chars).transpose.map(&:join).map(&:reverse)] || 
  light_rule_hash[light_data.map(&:chars).transpose.map(&:join).map(&:reverse).reverse]
end

def enhance(data, light_rule_hash)
  size = data.length % 2 == 0 ? 2 : 3
  dimensions  = data.length / size
  enhanced_data = (0...dimensions).map do |i|
    next_data = (0...dimensions).map do |j|
      light_data = (0...size).map do |k|
        (0...size).map do |l|
          x = k + i * size
          y = l + j * size
          data[x][y]
        end.join
      end
      find_rule_in_light_rule_hash(light_rule_hash, light_data)
    end
    next_data = next_data.transpose.map(&:join)
  end

  return enhanced_data.flatten
end

def find_lights_turned_on(iterations, data, light_rule_hash)
  iterations.times { data = enhance(data, light_rule_hash) }

  return data.join.count('#')
end

light_rule_hash = {}; File.open('input.txt').read.split("\n").map{ |x| light_rule_hash[x.split(' => ')[0].split('/')] = x.split(' => ')[1].split('/') }
start_data = [".#.", "..#", "###"]
puts "Part 1: #{find_lights_turned_on(5, start_data, light_rule_hash)}"
puts "Part 2: #{find_lights_turned_on(18, start_data, light_rule_hash)}"
