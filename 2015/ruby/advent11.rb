def pair_without_overlap?(input)
  input.scan(/(.)\1/).uniq.length >= 2
end

def no_look_alikes?(input)
  input.scan(/[iol]/).empty?
end

def triple_increment?(input)
  triples = []
  trues = []

  input.split("").each_with_index do |e, i|
    triples << [e, input[i + 1], input[i + 2]]
  end

  triples.each do |triple|
    triple.each do |l|
      unless l.nil?
        if !input.match(/#{l}#{l.next}#{l.next.next}/).nil?
          trues << true
        else
          trues << false
        end
      end
    end
  end

  trues.include?(true) ? true : false
end

def valid?(password)
  if triple_increment?(password) && no_look_alikes?(password) && pair_without_overlap?(password)
    return true
  else
    return false 
  end
end

def next_pass(password)
  loop do 
    password = password.succ
    return password if valid?(password)
  end
end

password = "vzbxkghb"
password = next_pass(password)
puts password
puts next_pass(password)