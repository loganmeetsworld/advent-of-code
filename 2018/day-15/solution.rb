
# warrior class with attack methods, other classes inherit from it

class Battlefield
  attr_accessor :grid
  def initialize
    @grid = create_grid(input)
  end

  def create_grid(input)
  end
end

class Round
  def initialize(warriors, battlefield)
    @warriors = warriors
    @battlefield = battlefield
  end

  def print_battle_state
  end
end

class Warrior
  attr_accessor :position
  def initialize(position)
    @position = position
    @turn = false
    @attack_power = 3
    @hit_points = 200
  end

  def move()
    if identify_targets()
      targets = identify_targets()
    end
    if can_attack_closest_enemy?()
      attack()
    end

    square = find_nearest_adjacent_in_range_reachable_square()
    self.position = find_shortest_path_to_square()
  end

  def attack()
  end

  def find_adjacent_in_range_squares()
  end

  def find_reachable_squares()
  end

  def find_nearest_adjacent_in_range_reachable_square()
    # find the nearest square that is first in reading order
    if squares.length == 1
      square
    else
      break_reading_order_tie()
    end
  end

  def identify_targets()
    targets = []
    return targets
  end

  def can_attack_closest_enemy?()
  end
end


input = File.open('input.txt').readlines

battlefield = Battlefield.new(input)
battlefield.visualize