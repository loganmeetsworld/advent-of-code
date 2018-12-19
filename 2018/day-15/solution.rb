require "set"

# Two main classes: a battle and warriors. A Battle has many warriors, elves and goblins. They fight over rounds.
class Battle
  attr_accessor :field, :rounds, :initial_warrior_positions, :walls, :warriors
  def initialize(input)
    @field = input
    @rounds = 0
    @initial_warrior_positions = build_warriors(@field)
    @warriors = []
  end

  def print_battle_state()
    puts @field
    puts
  end

  def warriors_on_one_side_all_dead?()
    goblins = @warriors.select{ |w| w.type == 'G' }
    elves = @warriors.select{ |w| w.type == 'E' }
    return true if elves.empty?
    return true if goblins.empty?
  end

  # We start with the warriors in their positions from our input, but these positions will change.
  def build_warriors(field)
    warriors = []
    field.chars.each_with_index do |c, i|
      if c.match(/[A-Z]/)
        warriors.push({:type => c, :position => i})
      end
    end
    return warriors
  end
end

class Warrior
  attr_accessor :position, :attack_power, :hit_points, :type, :battle
  def initialize(type, position, battle)
    @battle = battle
    @position = position
    @type = type
    @attack_power = 3
    @hit_points = 200
  end

  def move()
    squares_surrounding_current_warrior = find_surrounding(@position)
    in_range_targets = @battle.warriors.select{ |t| t.type != @type }.map{ |t| find_surrounding(t.position).select{ |i| @battle.field[i] == "." } }.flatten.uniq
    target_to_attack = @battle.warriors.select{ |t| t.type != @type && squares_surrounding_current_warrior.include?(t.position) }.min_by{ |t| [t.hit_points, t.position] }
    return attack(target_to_attack) if target_to_attack

    possible_moves = in_range_targets.map{ |t| find_next_move(t, squares_surrounding_current_warrior) }.compact.sort
    unless possible_moves.empty?
      next_position = possible_moves.first.last
      @battle.field[@position] = "."
      @battle.field[next_position] = @type
      @position = next_position
    end
  end

  private def attack(target)
    target.hit_points -= @attack_power
    if target.hit_points <= 0
      puts "Target has fallen! Team #{target.type} is minus one member."
      @battle.field[target.position] = '.'
      @battle.warriors.delete(target)
    end
  end

  private def find_surrounding(position)
    [position - (@battle.field.split.first.length + 1), position - 1, position + 1, position +  (@battle.field.split.first.length + 1)]
  end

  private def find_next_move(target, squares_surrounding_current_warrior)
    possible_moves, next_possible_options, seen = [target], [], Set.new

    distance, step = 1, nil
    loop do
      if possible_moves.empty?
        break if next_possible_options.empty?

        possible_moves = next_possible_options.sort.uniq.reverse
        next_possible_options = []
        distance += 1
      end

      position = possible_moves.pop
      if squares_surrounding_current_warrior.include?(position)
        step = position
        break
      end

      seen.add(position)
      find_surrounding(position).each do |i|
        next_possible_options.push(i) if @battle.field[i] == "." && !seen.include?(i)
      end
    end

    return [distance, target, step] if step
  end
end

# Initiate the battle with the puzzle input battlefield given
field = File.open('test-5.txt').read.chomp
battle = Battle.new(field)
puts "Initial battle state:"
battle.print_battle_state

# Initiate the given warriors on the field, add them to battle.warriors, and also give a warrior the battle
battle.initial_warrior_positions.each{ |w| battle.warriors.push(Warrior.new(w[:type], w[:position], battle)) }

# Until all the warriors die on a give side, move the battle forward in rounds until a side wins.
until battle.warriors_on_one_side_all_dead?
  puts "Round ##{battle.rounds + 1}:"
  battle.warriors.sort_by(&:position).each{ |w| w.move() }
  battle.rounds += 1
  battle.print_battle_state
end

# The outcome of the round is determined by how many rounds were fought, and how many points remain on the winning side
winner = battle.warriors.first.type == 'E' ? "Elves" : "Goblins"
puts "Part 1: Over the course of #{battle.rounds} rounds, #{winner} won with #{battle.warriors.map{ |w| w.hit_points}.inject(&:+)} hit points. Official mathematical outcome: #{battle.rounds * battle.warriors.map{ |w| w.hit_points }.inject(&:+)}"