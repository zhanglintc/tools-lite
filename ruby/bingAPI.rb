require 'net/http'
require 'json'
require 'sinatra'

set :bind, '0.0.0.0'
set :port, '5969'

def req_data
  uri = URI("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN")
  raw = Net::HTTP.get(uri)
  jsn = JSON.parse raw

  $enddate = jsn["images"][0]["enddate"]
  $url = jsn["images"][0]["url"]
  $copyright = jsn["images"][0]["copyright"]
end

get '/' do
  req_data()
  redirect $url
end

get '/url' do
  req_data()
  redirect $url
end

get '/date' do
  req_data()
  return $enddate
end

get '/description' do
  req_data()
  return $copyright
end