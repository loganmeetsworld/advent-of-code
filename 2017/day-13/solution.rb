input = File.open('input.txt').read.split("\n")
# input = "0: 3
# 1: 2
# 4: 4
# 6: 4".split("\n")

def create_firewall(input)
  firewall = Hash.new
  input.each{ |l| firewall[l.split(': ')[0].to_i] = [Array.new(l.split(': ')[1].to_i), true] }
  firewall.values.each {|v| v[0][0] = 'S' }
  return firewall
end

packet_position = 0
hit_count = 0
firewall = create_firewall(input)

def update_scanner_positions(firewall)
  firewall.values.each do |v|
    column = v[0]
    scanner_direction_down = v[1]
    current_scanner_position = column.index('S')
    last_item_index = column.length - 1
    if scanner_direction_down
      v[0][current_scanner_position + 1] = 'S'
      if current_scanner_position + 1 == last_item_index
        v[1] = false
      end
    else
      v[0][current_scanner_position - 1] = 'S'
      if current_scanner_position - 1 == 0
        v[1] = true
      end
    end

    v[0][current_scanner_position] = nil
  end
  return firewall
end

(0..firewall.keys.max).each do |pico|
  v = firewall[pico]
  if !v.nil? && !v[0][packet_position].nil?
    hit_count += (pico * firewall[pico][0].length)
    puts "Caught at column #{pico} with severity #{firewall[pico][0].length}"
  end
  update_scanner_positions(firewall)
end

puts "Hit severity: #{hit_count}"