def calculate_sleep(watch_events)
    asleep_time, asleep_minutes = 0, []
    times = watch_events.join("\n").scan(/\d{2}:(\d{2})/).flatten.map(&:to_i).each_slice(2).to_a
    times.each do |time|
        if time.length == 2
            asleep_time += (time[1] - time[0])
            asleep_minutes += (time[0]...time[1]).to_a
        end
    end
    return asleep_time, asleep_minutes
end

def parse_watch(watch)
    id = watch.scan(/#(\d+)/).flatten.first
    asleep_time, asleep_minutes = calculate_sleep(watch.split("\n")[1..-1])
    return {:id => id, :asleep_time => asleep_time, :asleep_minutes => asleep_minutes}
end

def parse_sleep_info(id, group)
    total_sleep = group.map{ |h| h[:asleep_time] }.inject(:+)
    total_minutes = group.map{ |h| h[:asleep_minutes] }.flatten
    most_repeated_minute = total_minutes.max_by { |i| total_minutes.count(i) }
    repeated_count = total_minutes.count(most_repeated_minute)
    return {:id => id, :total_sleep => total_sleep, :repeated_count => repeated_count, :most_repeated_minute => most_repeated_minute}
end

sleep_info = File.open("./input.txt")
    .readlines
    .map(&:chomp)
    .sort
    .join("\n")
    .split(/(?=\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\] Guard)/)
    .map{ |w| parse_watch(w) }
    .group_by{ |w| w[:id] }
    .map{ |id, group| parse_sleep_info(id, group) }

puts "Part 1:"
biggest_sleeper_by_total_sleep = sleep_info.max_by{ |x| x[:total_sleep] }
puts  biggest_sleeper_by_total_sleep[:id].to_i * biggest_sleeper_by_total_sleep[:most_repeated_minute]

puts "Part 2:"
biggest_sleeper_by_minute = sleep_info.max_by{ |x| x[:repeated_count] }
puts biggest_sleeper_by_minute[:id].to_i * biggest_sleeper_by_minute[:most_repeated_minute]