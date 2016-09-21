#!/env/bin/ruby
# encoding: utf-8

app_name = "bingAPI.rb"

puts "killing #{app_name}"
system "ps -ef | grep 5969 | grep -v grep | cut -c 9-15 | xargs kill -s 9"

puts "restarting #{app_name}"
system "nohup ruby #{app_name}&"
