input = File.open('input.txt').read.split(',')
programs = ['abcdefghijklmnop']

def dance(programs, steps)
  steps.each_with_object(programs.dup) do |step, programs|
    case step[0]
    when 's'
      programs.replace(programs.chars.rotate(-step[1..-1].to_i).join)
    when 'x'
      scan_a, scan_b = step[1..-1].scan(/\d+/).map(&:to_i)
      a, b = programs[scan_a], programs[scan_b]
      programs.tr!(a + b, b + a)
    when 'p'
      a, b = step[1..-1].split('/')
      programs.tr!(a + b, b + a)
    end
  end
end

loop {
  programs.push dance(programs[-1], input).freeze
  break if programs[-1] == programs[0]
}

programs.pop

puts programs[1]
puts programs[1000000000 % programs.length]