class Room
  @@rooms = []
  attr_reader :encrypt_name, :sector_id, :checksum

  def initialize(encrypt_name, sector_id, checksum)
    @encrypt_name = encrypt_name
    @sector_id = sector_id.to_i
    @checksum = checksum
    @@rooms << self
  end

  def valid_room?
    decrypt_name = 
      @encrypt_name.join('')
        .each_char
        .group_by{ |w| w }
        .map{ |k, v| [k, v.size ] }
        .sort_by { |x, y| [ -Integer(y), x ] }
        .map(&:first)
        .join('')[0..4]
    @checksum == decrypt_name
  end

  def decrypt_name
    string = ''
    letters = ('a'..'z').to_a
    rotated_letters = letters.rotate(@sector_id)

    @encrypt_name.each do |word|
      decrypt_word = 
        word.chars
          .map { |x| rotated_letters[letters.find_index(x)] }
          .join('')
      string << decrypt_word
      string << ' '
    end

    return string[0..-2]
  end

  def self.sum_sector_ids
    @@rooms
      .select{ |room| room.valid_room? }
      .map(&:sector_id)
      .inject(:+)
  end

  def self.find_north_pole
    @@rooms
      .detect{ |x| x.decrypt_name == 'northpole object storage' }
      .sector_id
  end
end

input = File.open("./input.txt").read.split("\n")

input.each do |code|
  regexp = /([0-9]+)\[(.*?)\]/
  matches = regexp.match(code)
  encrypt_name = code.gsub(regexp, '').split('-')
  Room.new(encrypt_name, matches[1], matches[2])
end

valid_room_id_sum = Room.sum_sector_ids
north_pole_sector_id = Room.find_north_pole
puts "Part 1 answer: #{valid_room_id_sum}"
puts "Part 2 answer: #{north_pole_sector_id}"