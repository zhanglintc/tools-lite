# encoding: utf-8

require 'net/http'

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

  
resp = Net::HTTP.get_response(URI "https://github.com/zhanglintc" )  
puts resp.body 

