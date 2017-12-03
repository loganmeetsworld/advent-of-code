require 'pry'

class SueFinder
  attr_accessor :number, :children, :cats, :samoyeds, :pomeranians, :akitas, :vizslas, :goldfish, :trees, :cars, :perfumes

  def initialize(number, children = nil, cats = nil, samoyeds = nil, pomeranians = nil, akitas = nil, vizslas = nil, goldfish = nil, trees = nil, cars = nil, perfumes = nil)

    @number = number
    @children =  children
    @cats =  cats
    @samoyeds =  samoyeds
    @pomeranians =  pomeranians
    @akitas =  akitas
    @vizslas =  vizslas
    @goldfish =  goldfish
    @trees =  trees
    @cars =  cars
    @perfumes = perfumes
  end
end

input = File.read('inputs/day16.txt')

@sues = []

input.each_line.map do |line|
  sue_num = line.split(' ')[1].chomp(':').to_i
  s = SueFinder.new(sue_num)

  case line.split(' ')[2].chomp(':')
  when "children"
    s.children = line.split(' ')[3].to_i
  when "samoyeds"
    s.samoyeds = line.split(' ')[3].to_i
  when "pomeranians"
    s.pomeranians = line.split(' ')[3].to_i
  when "akitas"
    s.akitas = line.split(' ')[3].to_i
  when "vizslas"
    s.vizslas = line.split(' ')[3].to_i
  when "goldfish"
    s.goldfish = line.split(' ')[3].to_i
  when "trees"
    s.trees = line.split(' ')[3].to_i
  when "cars"
    s.cars = line.split(' ')[3].to_i
  when "perfumes"
    s.perfumes = line.split(' ')[3].to_i
  end

  case line.split(' ')[4].chomp(':')
  when "children"
    s.children = line.split(' ')[5].to_i
  when "samoyeds"
    s.samoyeds = line.split(' ')[5].to_i
  when "pomeranians"
    s.pomeranians = line.split(' ')[5].to_i
  when "akitas"
    s.akitas = line.split(' ')[5].to_i
  when "vizslas"
    s.vizslas = line.split(' ')[5].to_i
  when "goldfish"
    s.goldfish = line.split(' ')[5].to_i
  when "trees"
    s.trees = line.split(' ')[5].to_i
  when "cars"
    s.cars = line.split(' ')[5].to_i
  when "perfumes"
    s.perfumes = line.split(' ')[5].to_i
  end

  case line.split(' ')[6].chomp(':')
  when "children"
    s.children = line.split(' ')[7].to_i
  when "samoyeds"
    s.samoyeds = line.split(' ')[7].to_i
  when "pomeranians"
    s.pomeranians = line.split(' ')[7].to_i
  when "akitas"
    s.akitas = line.split(' ')[7].to_i
  when "vizslas"
    s.vizslas = line.split(' ')[7].to_i
  when "goldfish"
    s.goldfish = line.split(' ')[7].to_i
  when "trees"
    s.trees = line.split(' ')[7].to_i
  when "cars"
    s.cars = line.split(' ')[7].to_i
  when "perfumes"
    s.perfumes = line.split(' ')[7].to_i
  end

  @sues << s
end

real_sue = {
  children: 3,
  cats: 7,
  samoyeds: 2,
  pomeranians: 3,
  akitas: 0,
  vizslas: 0,
  goldfish: 5,
  trees: 3,
  cars: 2,
  perfumes: 1
}

find_sue = @sues.find do |sue|
  real_sue.all? do |attribute, value|
    # binding.pry
    sue.instance_variable_get("@#{attribute.to_s}".to_sym).nil? || sue.instance_variable_get("@#{attribute.to_s}".to_sym) == value 
  end
end

puts find_sue.instance_variable_get(:@number)
