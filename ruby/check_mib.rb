#!/env/bin/ruby
# encoding: utf-8

require 'Find'
require 'pathname'

Encoding.default_external = Encoding::UTF_8
Encoding.default_internal = Encoding::UTF_8

VERSION = "v0.1"

targetFolder = './'

def each_file target
  Find.find(target) do |path|
    if not File.directory? path
      yield path
    end
  end
end

def isTargetFile path
  if not path.include? "/ja/"
    return false
  else
    return true
  end
end

def processFile path
  path = path.downcase
  return if not path.include? "d.kpd" and not path.include? "d.kp_"

  if path.include? "d.kp_"
    fileName = File.basename(path).gsub("kp_", "kpd")
    `expand #{path} #{fileName}`

    fr = open fileName, "rb"
    content = fr.read
    fr.close

    # delete tmep file in the end
    `del #{fileName}`
  else
    fr = open path, "rb"
    content = fr.read
    fr.close
  end

  content =~ /DeviceInfoCache\0+(\w+)\0+/
  cache_status = $1

  mib_status = "Unknown"
  mib_status = "Is MIB" if cache_status == "Disable"
  mib_status = "Not MIB" if cache_status == "Enable"

  puts mib_status + ": #{path}\n\n"
end

each_file targetFolder do |path|
  begin
    path = Pathname.new(path).realpath.to_s
    path = path.downcase
  rescue
    next
  end

  if isTargetFile path
    processFile path
  end
end

puts "Press any key to close..."
gets


