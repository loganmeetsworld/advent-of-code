input = File.open("./input.txt").read.split("\n")

def parse_input(line)
  line = line.split(' ')
  case line[0]
  when 'bot'
    if Bot.all.find{|x| x.id == line[1] }.nil?
      b = Bot.new(line[1], [line[5], line[6]], [line[10], line[11]])
    else
      bot = Bot.all.find{|x| x.id == line[1] }
      bot.low = [line[5], line[6]]
      bot.high = [line[10], line[11]]
    end
  when 'value'
    v = Value.new(line[1])

    if Bot.all.find{|x| x.id == line[-1] }.nil?
      b = Bot.new(line[-1])
      b.values << v
    else
      b = Bot.all.find{|x| x.id == line[-1] }
      b.values << v
    end
  end
end

class Bot
  @@bots = []
  attr_accessor :values, :id, :low, :high, :processed_instruction
  def initialize(id, low=nil, high=nil)
    @id = id
    @low = low
    @high = high
    @values = []
    @processed_instruction = false
    @@bots << self
  end

  def self.all
    @@bots
  end

  def self.not_processed
    @@bots.find_all{ |x| x.processed_instruction }
  end

  def self.find_magic_bot
    @@bots.find{ |x| x.values(&:id) }
  end

  def give_values
    min = @values.min_by{|x| x.id.to_i }
    max = @values.max_by{|x| x.id.to_i }
    if @low[0] == 'bot'
      low_bot = @@bots.find{|x| x.id == @low[1]}
      low_bot.values << min
    end

    if @high[0] == 'bot'
      high_bot = @@bots.find{|x| x.id == @high[1]}
      high_bot.values << max
    end

    @processed_instruction = true
  end
end

class Value
  @@values = []
  attr_accessor :id
  def initialize(id)
    @id = id
    @@values << self
  end

  def self.all
    return @@values
  end
end

input.each do |line|
  parse_input(line)
end

while Bot.all.map(&:processed_instruction).include?(false)
  Bot.all.find_all{|x| x.values.length > 1 && x.processed_instruction == false}.each do |b|
    b.give_values
  end
end

magic_bot = Bot.all.find{|b| b.values.map(&:id).sort == ['17', '61']}.id

puts "Part 1: #{magic_bot}"

puts 'Part2: ' + [Bot.all.find{|x| x.id == '188'}.values.min_by{|x| x.id.to_i }.id.to_i,
Bot.all.find{|x| x.id == '58'}.values.min_by{|x| x.id.to_i }.id.to_i,
Bot.all.find{|x| x.id == '203'}.values.max_by{|x| x.id.to_i }.id.to_i].inject(:*).to_s

# bot 188 gives low to output 0 and high to bot 72
# bot 58 gives low to output 2 and high to bot 51
# bot 203 gives low to output 16 and high to output 1

