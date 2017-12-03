require 'pry'
require 'set'

molecule = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

input = File.readlines('inputs/day19.txt')

hash = {}

input.each do |line|
  if hash[line.split(' => ')[0]].nil?
    hash[line.split(' => ')[0]] = []
    hash[line.split(' => ')[0]] << line.split(' => ')[1].chomp
  else
    hash[line.split(' => ')[0]] << line.split(' => ')[1].chomp
  end
end

molecule_array = Array.new

hash.each do |k, v|
  count = molecule.scan(k).length
  segments = molecule.split(k)

  v.each do |replace|
    keys = Array.new(count){ k }
    count.times do |i|
      temp_place = keys.dup
      temp_place[i] = replace
      molecule_array << segments.zip(temp_place).flatten.join
      binding.pry
    end
  end
end

puts array.uniq.length
