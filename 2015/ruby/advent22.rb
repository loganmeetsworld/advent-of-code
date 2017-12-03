require 'pry'

spells = {
  "missile" => 53, 
  "drain" => 73, 
  "shield" => 113, 
  "poison" => 173, 
  "recharge" => 229
}

class Character
  attr_accessor :boss_hp, :boss_damage, :hero_hp, :money, :armor, :shield_turns, :poison_turns, :recharge_turns, :money_spent

  def initialize
    @boss_hp = 58
    @boss_damage = 9
    @hero_hp = 50
    @money = 500
    @armor = 0
    @shield_turns = 0
    @poison_turns = 0
    @recharge_turns = 0
    @money_spent = 0
  end

  def hurt(character, damage)
    character == "boss" ? @boss_hp -= damage : @hero_hp -= (damage - @armor)
  end

  def fatal_for?(character)
    character == "boss" ? @boss_hp <= 0 : @hero_hp <= 0 || @money < 53
  end

  def time_up_on?(spell)
    if spell.values[0] > @money then return false; end

    if spell.keys[0] == "shield"
      shield_turns == 0
    elsif spell.keys[0] == "poison"
      poison_turns == 0
    elsif spell.keys[0] == "recharge"
      recharge_turns == 0
    else
      true
    end
  end

  def cast!(spell, boss)
    @money_spent += spell.values[0]
    @money -= spell.values[0]
    @hero_hp -= 1 # comment out for part 1

    case spell.keys[0]
    when "missile"
      boss.hurt("boss", 4)
    when "drain"
      boss.hurt("boss", 2)
      @hero_hp += 2
    when "shield"
      @armor = 7
      @shield_turns = 6
    when "poison"
      @poison_turns = 6
    when "recharge"
      @recharge_turns = 5
    end
  end

  def count_turns(boss)
    @shield_turns > 0 ? @shield_turns -= 1 : @armor = 0

    if @poison_turns > 0 then boss.hurt("boss", 3); @poison_turns -= 1; end

    if @recharge_turns > 0 then @money += 101; @recharge_turns -= 1; end
  end
end

min = 5000
mins = []

100_000.times do 
  boss, hero = Character.new, Character.new

  while !hero.fatal_for?("hero")
    hero.count_turns(boss)
    sample = spells.keys.sample
    spell = spells.select { |k,v| k == sample }

    while !hero.time_up_on?(spell)
      sample = spells.keys.sample
      spell = spells.select { |k,v| k == sample }
    end

    hero.cast!(spell, boss)
    hero.count_turns(boss)

    if boss.fatal_for?("boss")
      if hero.money_spent <= min
        min = hero.money_spent
        mins << min
      end
      break
    end
    # binding.pry
    hero.hurt("hero", boss.boss_damage)
  end
end

puts mins.min