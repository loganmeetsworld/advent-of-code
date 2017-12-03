require 'pry'
weapons = Hash.new
armor = Hash.new
ring = Hash.new

weapons["dagger"] = [8, 4, 0]
weapons["shortsword"] = [10, 5, 0]
weapons["warhammer"] = [25, 6, 0]
weapons["longsword"] = [40, 7, 0]
weapons["greataxe"] = [74, 8, 0]

armor["leather"] = [13, 0, 1]
armor["chainmail"] = [31, 0, 2]
armor["splintmail"] = [53, 0, 3]
armor["bandedmail"] = [75, 0, 4]
armor["platemail"] = [102, 0, 5]
armor["none"] = [0, 0, 0]

ring[:damage_1] = [25, 1, 0]
ring[:damage_2] = [50, 2, 0]
ring[:damage_3] = [100, 3, 0]
ring[:defence_1] = [20, 0, 1]
ring[:defence_2] = [40, 0, 2]
ring[:defence_3] = [80, 0, 3]
ring[:mix_1] = [105, 1, 2]
ring[:mix_2] = [125, 1, 3]
ring[:mix_3] = [70, 2, 1]
ring[:mix_4] = [130, 2, 3]
ring[:mix_5] = [120, 3, 1]
ring[:mix_6] = [140, 3, 2]
ring[:none] = [0, 0, 0]

class Player
  attr_accessor :damage, :armor, :my_points, :boss_damage, :boss_armor, :boss_points, :cost, :ring, :ring_damage, :ring_defense

  def initialize(damage, armor, ring)
    @damage = damage[1]
    @armor = armor[2]
    @ring_damage = ring[1]
    @ring_defense = ring[2]
    @my_points = 100
    @boss_points = 104
    @boss_damage = 8
    @boss_armor = 1
    @cost = damage[0] + armor[0] + ring[0]
  end

  def attack!
    puts "Boss points at:"
    puts @boss_points -= ((@damage + @ring_damage) - @boss_armor)
  end

  def defend!
    puts "My points at:"
    puts @my_points -= (@boss_damage - (@armor + @ring_defense))
  end
end

players = []

equip = weapons.values.product(armor.values).product(ring.values).map(&:flatten)

equip_array = []

equip.each do |e|
  equip_array << e.each_slice(3).to_a
end

equip_array.each do |v|
  players << Player.new(v[0], v[1], v[2])
  # binding.pry
end

winners = []
losers = []

players.each do |p|
  until (p.my_points <= 0) || (p.boss_points <= 0)
    p.attack!
    if p.boss_points <= 0 
      break
    end
    p.defend!
  end
  if p.my_points > p.boss_points
    winners << p
  elsif p.my_points < p.boss_points
    losers << p
  end
end

costs = []
costs_2 = []

winners.each do |w|
  costs << w.cost
end

losers.each do |w|
  costs_2 << w.cost
end

puts "The minimum cost to win is #{costs.min}."
puts "The maximum cost to lose is #{costs_2.max}."