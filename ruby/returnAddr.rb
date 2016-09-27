#!/env/bin/ruby
# encoding: utf-8

require 'sinatra'

set :bind, '0.0.0.0'
set :port, '3322'

get '/' do
  return env['REMOTE_ADDR']
end