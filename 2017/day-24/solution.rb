ports = File.open('test-input.txt').read.lines.map(&:strip).map{|l| l.split('/').map(&:to_i)}

