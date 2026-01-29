#!/usr/bin/env ruby
# encoding: utf-8

require 'sinatra'

set :bind, '0.0.0.0'
set :port, '3322'

get '/' do
  content_type :json
  return request.env['HTTP_X_FORWARDED_FOR']&.split(',')&.first&.strip ||
    request.env['HTTP_X_REAL_IP'] ||
    request.env['REMOTE_ADDR']
end

