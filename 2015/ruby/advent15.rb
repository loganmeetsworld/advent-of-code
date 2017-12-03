require 'pry'
class Ingredient
  attr_accessor :name, :capacity, :durability, :flavor, :texture, :calories

  def initialize(name, capacity, durability, flavor, texture, calories)
    @name = name
    @capacity = capacity
    @durability = durability
    @flavor = flavor
    @texture = texture
    @calories = calories
  end
end

input = File.read('inputs/day15.txt')

@ingredients = input.each_line.map do |line|
  nums = line.scan(/-?\d+/)
  name = line.split(' ')[0].chomp(":")
  Ingredient.new(name, nums[0].to_i, nums[1].to_i, nums[2].to_i, nums[3].to_i, nums[4].to_i
  )
end

def contains_quad_for_sum(arr, n)
  arr.permutation(4).find_all { |a, b, c, d| a + b + c + d == n }

end

possible_combos = contains_quad_for_sum((0..100).to_a, 100)

sums_part_1 = []
sums_part_2 = []

  possible_combos.each do |c|
    capacity = 
    (c[0] * @ingredients[0].capacity) + 
    (c[1] * @ingredients[1].capacity) + 
    (c[2] * @ingredients[2].capacity) + 
    (c[3] * @ingredients[3].capacity)

    if capacity < 0 
      capacity = 0 
    end

    durability = 
    (c[0] * @ingredients[0].durability) + 
    (c[1] * @ingredients[1].durability) + 
    (c[2] * @ingredients[2].durability) + 
    (c[3] * @ingredients[3].durability)

    if durability < 0
      # binding.pry
      durability = 0 
    end

    flavor = 
    (c[0] * @ingredients[0].flavor) + 
    (c[1] * @ingredients[1].flavor) + 
    (c[2] * @ingredients[2].flavor) + 
    (c[3] * @ingredients[3].flavor)

    if flavor < 0 
      flavor = 0
    end

    texture = 
    (c[0] * @ingredients[0].texture) + 
    (c[1] * @ingredients[1].texture) + 
    (c[2] * @ingredients[2].texture) + 
    (c[3] * @ingredients[3].texture)

    if texture < 0 
      texture = 0 
    end

    calories = 
    (c[0] * @ingredients[0].calories) + 
    (c[1] * @ingredients[1].calories) + 
    (c[2] * @ingredients[2].calories) + 
    (c[3] * @ingredients[3].calories)

    if calories < 0 
      calories = 0 
    end

    sum_part_1 = capacity * durability * flavor * texture

    if calories <= 500
      sum_part_2 = capacity * durability * flavor * texture
    else
      sum_part_2 = 0
    end

    sums_part_1 << sum_part_1
    sums_part_2 << sum_part_2
    # binding.pry
  end

puts sums_part_1.max
puts sums_part_2.max