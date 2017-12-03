require 'pry'

molecule = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

input = File.readlines('inputs/day19.txt')
hash = {}

input.each do |line|
  hash[line.split(' => ')[1].chomp] = line.split(' => ')[0].chomp
end

molecule_dup = molecule.dup

while molecule_dup != "e"
  steps = 0
  no_more_placements = false
  molecule_dup = molecule.dup

  until no_more_placements
    no_more_placements = true

    hash.keys.shuffle.each do |e|
      if !molecule_dup.scan(e).empty?
        molecule_dup.sub!(e, hash[e])
        steps += 1 
        no_more_placements = false 
      end
    end
  end
end

puts "#{steps} steps to finish."