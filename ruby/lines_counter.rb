require 'Find'

ext = ['c','cpp','h','java','py']
target_folder = "/Users/lane/Github"

def count_line(target_file)
  counter = 0

  fr = File.open(target_file)
  fr.each_line do |line|
    counter += 1
  end

  return counter
end

counter = {}

Find.find('/Users/lane/Github') do |path|
  if not File.directory? path
    file_name = path.split('/')[-1]
    extension = file_name.split('.')[-1]
    if ext.include? extension
      if not counter[extension]
        counter[extension] = count_line path
      else
        counter[extension] += count_line path
      end
    end
  end
end

puts 'all -> ' + eval(counter.values.join('+')).to_s
puts
counter.each do |key, val|
  puts key.to_s + ' -> ' + val.to_s
end

