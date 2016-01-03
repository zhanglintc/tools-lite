#!/env/bin/ruby
# encoding: utf-8

def cdRepo path
  tempFile = "what_ever_things_here"
  tempFilePath = "#{path}/#{tempFile}"
  system "cd #{path} && git status > #{tempFile}"

  fr = open tempFilePath
  content = fr.read
  fr.close

  File.delete tempFilePath

  if not content.include? "up-to-date"
    puts path
  else
    puts "OK"
  end
end

def checkRepo
  Dir.entries("./").each do |path|
    if File.directory? path and not /^\.+$/ =~ path
      cdRepo path
    end
  end

  puts "Check completed..."
end

if __FILE__ == $0
  checkRepo()
end


