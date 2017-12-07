input = File.open("./test-input.txt").read.split("\n")
input = File.open("./input.txt").read.split("\n")

tree = {}
parents = {}
hash = {}

input.each do |x|
  tree[x.split[0]] = { 
    'weight' => x.split[1].gsub(/\D/, "").to_i,
    'children' => x.include?(' -> ') ? x.split(' -> ')[1].split(',').strip : []
  }
end

tree.each do |key, values|
  children = values['children']
  children.each do |child|
    parents[child] = key
  end
  hash[key] = 1  
end

hash.keys.select{ |x| !parents[x] }