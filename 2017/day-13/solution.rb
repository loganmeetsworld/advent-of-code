require 'test/unit'
require 'pry'
extend Test::Unit::Assertions

class Firewall
  attr_accessor :fh, :severity, :delay

  def initialize(instr)
    @instr = instr
    @fh = create_firewall_hash()
    @severity = 0
    @packet_position = 0
    @delay = 0
    @never_caught = false
  end

  def create_firewall_hash
    h, dir = Hash.new, true
    @instr.split("\n").each{ |l| values = l.split(': '); h[values.first.to_i] = [Array.new(values.last.to_i), dir] }
    h.values.each{ |v| v.first[0] = 'S' }
    return h
  end

  def reset_scanner_positions
    @fh = create_firewall_hash()
  end

  def update_scanner_positions
    fh.values.each do |v|
      column, scanner_direction_down = v[0], v[1]
      current_scanner_position, last_item_index = column.index('S'), column.length - 1
      if scanner_direction_down
        column[current_scanner_position + 1] = 'S'
        v[1] = false if current_scanner_position + 1 == last_item_index
      else
        column[current_scanner_position - 1] = 'S'
        v[1] = true if current_scanner_position - 1 == 0
      end
      column[current_scanner_position] = nil
    end
  end

  def find_shortest_safe_delay
    reset_scanner_positions()
    until @never_caught
      @never_caught = true
      update_scanner_positions()
      @delay += 1 
      temp = Marshal.load(Marshal.dump(@fh))

      (0..fh.keys.max).each do |p|
        v = fh[p]
        if !v.nil? && !v[0][@packet_position].nil? then @never_caught = false; break end
        update_scanner_positions()
      end

      if @never_caught == false then @fh = temp end
    end
  end

  def find_severity_traversing_firewall_with_no_delay
    (0..fh.keys.max).each do |p|
      v = fh[p]
      if !v.nil? && !v[0][@packet_position].nil? then @severity += (p * fh[p][0].length) end
      update_scanner_positions()
    end
  end
end

# tests
test_input = "0: 3\n1: 2\n4: 4\n6: 4"
test_firewall = Firewall.new(test_input)
test_firewall.find_severity_traversing_firewall_with_no_delay
test_firewall.find_shortest_safe_delay
assert_equal test_firewall.severity, 24
assert_equal test_firewall.delay, 10

# answers
input = File.open('input.txt').read
firewall = Firewall.new(input)
firewall.find_severity_traversing_firewall_with_no_delay
puts "Part 1 answer: #{firewall.severity}"
# this will definitely take like 10 minutes to run
firewall.find_shortest_safe_delay
puts "Part 2 answer: #{firewall.delay}"