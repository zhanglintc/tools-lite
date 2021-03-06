require 'Find'
require 'nkf'

VERSION = "v0.11"

targetFolder = ''

def each_file target
  Find.find(target) do |path|
    if not File.directory? path
      yield path
    end
  end
end

def isTargetFile path
  fileName = File.basename(path) || ""
  fileExt  = File.extname(path)[1..-1] || ""
  if ["csv"].include? fileExt.downcase
    return true
  else
    return false
  end
end

def processFile path
  fr = open path, "rb"
  content = fr.read
  fr.close

  content = NKF.nkf "-w", content
  content =~ /Duplicate : (\d+),/
  if $1.to_i > 0
    puts "Duplicated => #{$1}: " + path
  end
end

each_file targetFolder do |path|
  if isTargetFile path
    processFile path
  end
end

puts "done"
gets

