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
  attr_accessor :position, :attack_power, :hit_points, :type, :battle, :turn_position
  def initialize(type, position, turn_position, battle)
    @battle = battle
    @position = position
    @type = type
    @turn_position = turn_position
    @attack_power = 3
    @hit_points = 200
  end

  def move()
    targets = @battle.warriors.reject { |t| t.type == @type }
    in_range_targets = targets.map{ |t| find_surrounding(t.position).select{ |i| @battle.field[i] == "." } }.flatten.uniq
    possible_moves = in_range_targets.map{ |t| find_next_move(t) }.compact.sort
    return false if possible_moves.empty?
    next_position = possible_moves.first.last

    @battle.field[@position] = "."
    @battle.field[next_position] = @type
    @position = next_position
  end

  def find_surrounding(position)
    [position - (@battle.field.split.first.length + 1), position - 1, position + 1, position +  (@battle.field.split.first.length + 1)]
  end

  def find_next_move(target)
    possible_moves = find_surrounding(@position).select{ |i| @battle.field[i] == "." }.to_set
    options, next_options, seen = [target], [], Set.new

    distance, step = 1, nil
    loop do
      if options.empty?
        break if next_options.empty?

        options = next_options.sort.uniq.reverse
        next_options = []
        distance += 1
      end

      position = options.pop
      if possible_moves.include?(position)
        step = position
        break
      end

      seen.add(position)
      find_surrounding(position).each do |i|
        next_options.push(i) if @battle.field[i] == "." && !seen.include?(i)
      end
    end

    return [distance, target, step] if step
  end

  def attack()
    surrounding_squares = find_surrounding(@position)
    target = @battle.warriors.select{ |w| w.type != @type && surrounding_squares.include?(w.position) }.min_by { |w| [w.hit_points, w.position] }
    return false unless target
    target.hit_points -= @attack_power
    if target.hit_points <= 0
      puts "Target has fallen! Team #{target.type} is minus one member."
      @battle.field[target.position] = '.'
      @battle.warriors.delete(target)
    end
    return true
  end
end

# Initiate the battle with the puzzle input battlefield given
field = File.open('test-input.txt').read.chomp
battle = Battle.new(field)
puts "Initial battle state:"
battle.print_battle_state

# Initiate the given warriors on the field, add them to battle.warriors, and also give a warrior the battle
battle.initial_warrior_positions.each{ |w| battle.warriors.push(Warrior.new(w[:type], w[:position], w[:order], battle)) }

# Until all the warriors die on a give side, move the battle forward in rounds until a side wins.
until battle.warriors_on_one_side_all_dead?
  puts "Round ##{battle.rounds + 1}:"
  battle.warriors.sort_by(&:position).each do |w|
    w.move() && w.attack() unless w.attack()
  end

  battle.print_battle_state
  battle.rounds += 1
end

# The outcome of the round is determined by how many rounds were fought, and how many points remain on the winning side
winner = battle.warriors.first.type == 'E' ? "Elves" : "Goblins"
puts "Part 1: Over the course of #{battle.rounds} rounds, #{winner} won with #{battle.warriors.map{ |w| w.hit_points}.inject(&:+)} hit points. Official mathematical outcome: #{battle.rounds * battle.warriors.map{ |w| w.hit_points }.inject(&:+)}"