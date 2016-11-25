require 'net/http'
require 'json'
require 'sinatra'

set :bind, '0.0.0.0'
set :port, '5969'

def req_data daysAgo
  uri = URI("http://www.bing.com/HPImageArchive.aspx?format=js&idx=#{daysAgo}&n=1&mkt=zh-CN")
  raw = Net::HTTP.get(uri)
  jsn = JSON.parse raw

  $enddate = jsn["images"][0]["enddate"]
  $url = jsn["images"][0]["url"]
  $copyright = jsn["images"][0]["copyright"]
end

get '/' do
  daysAgo = (params['daysAgo'] or 0)
  req_data(daysAgo)
  redirect $url
end

get '/url' do
  daysAgo = (params['daysAgo'] or 0)
  req_data(daysAgo)
  redirect $url
end

get '/date' do
  daysAgo = (params['daysAgo'] or 0)
  req_data(daysAgo)
  return $enddate
end

get '/description' do
  daysAgo = (params['daysAgo'] or 0)
  req_data(daysAgo)
  return $copyright
end