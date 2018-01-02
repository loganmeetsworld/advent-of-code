class TapeArray
  STEPS = 12425180
  attr_accessor :state, :tape, :current_position
  def initialize
    @state = 'A'
    @tape = Array.new 10000000 {0}
    @current_position = @tape.length / 2
  end

  def toggle_value
    @tape[@current_position] = @tape[@current_position].zero? ? 1 : 0
  end

  def keep_value
    @tape[@current_position] = @tape[@current_position]
  end

  def execute_state
    cv = @tape[@current_position]
    case @state
    when 'A'
      if cv == 0
        toggle_value()
        @current_position += 1
        next_state = 'B'
      else
        toggle_value()
        @current_position += 1
        next_state = 'F'
      end
    when 'B'
      if cv == 0
        keep_value()
        @current_position -= 1
        next_state = 'B'
      else
        keep_value()
        @current_position -= 1
        next_state = 'C'
      end
    when 'C'
      if cv == 0
        toggle_value()
        @current_position -= 1
        next_state = 'D'
      else
        toggle_value()
        @current_position += 1
        next_state = 'C'
      end
    when 'D'
      if cv == 0
        toggle_value()
        @current_position -= 1
        next_state = 'E'
      else
        keep_value()
        @current_position += 1
        next_state = 'A'
      end
    when 'E'
      if cv == 0
        toggle_value()
        @current_position -= 1
        next_state = 'F'
      else
        toggle_value()
        @current_position -= 1
        next_state = 'D'
      end
    when 'F'
      if cv == 0
        toggle_value()
        @current_position += 1
        next_state = 'A'
      else
        toggle_value()
        @current_position -= 1
        next_state = 'E'
      end
    end
    return @tape, @current_position, next_state
  end

  def part_1_answer
    STEPS.times do
      @tape, @current_position, @state = execute_state()
    end
    @tape.count(1)
  end
end


t = TapeArray.new
puts t.part_1_answer