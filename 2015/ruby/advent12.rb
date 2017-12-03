#part one

input = File.read('inputs/day12')

strings = input.scan(/-?\d+/)
nums = []

strings.each do |s|
  nums << s.to_i
end

nums.inject(:+)
puts nums

# part 2

require 'json'

def add_all(nums)
  case nums 
  when Numeric
    nums
  when Array
    nums = nums.map { |num| add_all(num) }
    nums.inject(:+)
  when Hash
    if nums.values.include?('red')
      0
    else
      add_all(nums.values)   
    end
  else
    0
  end
end

puts add_all(JSON.load(File.read("inputs/day12")))