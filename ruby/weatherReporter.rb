#!/env/bin/ruby
# encoding: utf-8

require 'net/http'
require 'json'
require 'mail'

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

fr = open (File.dirname(__FILE__) + "/.pass"), "rb"
password = fr.read.chomp

city = "chongqing"
city_CN = "重庆"
base_url = "http://api.worldweatheronline.com/free/v2/weather.ashx"
params = "?key=55f1fdd05fba23be0a18043d0a017&num_of_days=3&format=json&lang=zh&q=#{city}"

resp = Net::HTTP.get_response URI(base_url + params)
dict = JSON.parse resp.body

date = dict['data']['weather'][0]['date']
morning =  dict['data']['weather'][0]['hourly'][2]
noon = dict['data']['weather'][0]['hourly'][4]
afternoon = dict['data']['weather'][0]['hourly'][6]

morning_tempC, morning_Desc = morning['tempC'], morning['lang_zh'][0]['value']
noon_tempC, noon_Desc = noon['tempC'], noon['lang_zh'][0]['value']
afternoon_tempC, afternoon_Desc = afternoon['tempC'], afternoon['lang_zh'][0]['value']

today = "\
#{city_CN} #{date} 天气状况:
早上 #{morning_tempC} 摄氏度, #{morning_Desc}.
中午 #{noon_tempC} 摄氏度, #{noon_Desc}.
晚上 #{afternoon_tempC} 摄氏度, #{afternoon_Desc}.\n
"

begin
  fr = open "yesterday.txt", "r"
  yesterday = fr.read
  fr.close
rescue
  yesterday = ""
end

fw = open "yesterday.txt", "w"
fw.write (today)
fw.close

smtp = {
  :address => 'smtp.163.com',
  :port => 25, :domain => '163.com',
  :user_name => 'zhanglintc',
  :password => password,
  :enable_starttls_auto => true,
  :openssl_verify_mode => 'none'
}

Mail.defaults { delivery_method :smtp, smtp }

mail = Mail.new do
  from 'zhanglintc@163.com'
  to 'contact@zhanglintc.co'
  subject "#{city_CN}天气状况"
  body (today + yesterday)
end

mail.deliver!

