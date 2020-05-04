#!/usr/bin/env ruby

require 'net/http'
require 'json'
require 'sinatra'
require 'sinatra/jsonp'
require 'hashie'

set :bind, '0.0.0.0'
set :port, '5969'

def parse_data daysAgo
  uri = URI("http://www.bing.com/HPImageArchive.aspx?format=js&idx=#{daysAgo}&n=1&mkt=zh-CN")
  raw = Net::HTTP.get(uri)
  jsn = JSON.parse raw
  jsn = Hashie::Mash.new jsn

  this = jsn.images[0]
  $fullstartdate = this.fullstartdate
  $startdate = this.startdate
  $enddate = this.enddate
  $url = "http://www.bing.com#{this.url}"
  $urlbase = this.urlbase
  $name = $urlbase.gsub "/th?id=", ""
  $copyright = this.copyright
  $title = this.copyright
  $hash = this.hsh
  p $name
end

get '/' do
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  redirect $url
end

get '/url' do
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  redirect $url
end

get '/date' do
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  return $enddate
end

get '/description' do
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  return $copyright
end

# get '/description_with_callback' do
#   callback = (params['callback'] or 'default_callback')
#   daysAgo = (params['daysAgo'] or 0)
#   parse_data(daysAgo)
#   jsn = {"description": $copyright}
#   jsonp $copyright, callback
# end

get '/description_with_callback' do
  callback = (params['callback'] or 'default_callback')
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  response.headers['content-type'] = 'application/javascript; charset=utf-8'
  ret = "#{callback}(#{daysAgo}, \"#{$copyright}\")"
end

get '/check_fav_callback' do
  callback = (params['callback'] or 'default_callback')
  daysAgo = (params['daysAgo'] or 0)
  parse_data(daysAgo)
  in_db = 1
  response.headers['content-type'] = 'application/javascript; charset=utf-8'
  ret = "#{callback}(#{daysAgo}, #{in_db})"
end


