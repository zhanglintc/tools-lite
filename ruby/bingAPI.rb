require 'net/http'
require 'json'
require 'sinatra'

set :bind, '0.0.0.0'
set :port, '5969'

uri = URI("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
raw = Net::HTTP.get(uri)
jsn = JSON.parse raw

enddate = jsn["images"][0]["enddate"]
url = jsn["images"][0]["url"]
copyright = jsn["images"][0]["copyright"]

get '/' do
  return url
end

get '/url' do
  return url
end

get '/date' do
  return enddate
end

get '/description' do
  return copyright
end