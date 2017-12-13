require 'test/unit'
extend Test::Unit::Assertions

class Firewall
  attr_accessor :fh

  def initialize(instr)
    @fh = create_firewall_hash(instr)
    @severity = 0
    @packet_position = 0
  end

  def create_firewall_hash(instr)
    h, dir = Hash.new, true
    instr.split("\n").each{ |l| values = l.split(': '); h[values.first.to_i] = [Array.new(values.last.to_i), dir] }
    h.values.each{ |v| v.first[0] = 'S' }
    return h
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

  def print_helpful_info(p, fh)
    puts "Caught at column #{p} with severity #{fh[p][0].length}"
  end

  def calculate_severity_traversing_firewall
    (0..fh.keys.max).each do |p|
      v = fh[p]
      if !v.nil? && !v[0][@packet_position].nil?
        @severity += (p * fh[p][0].length)
        # print_helpful_info(p, fh)
      end
      update_scanner_positions()
    end
    return @severity
  end
end

test_input = "0: 3\n1: 2\n4: 4\n6: 4"
test_firewall = Firewall.new(test_input)
assert_equal test_firewall.calculate_severity_traversing_firewall, 24

input = File.open('input.txt').read
firewall = Firewall.new(input)
part1_answer = firewall.calculate_severity_traversing_firewall
puts part1_answer