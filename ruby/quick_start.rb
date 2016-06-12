require 'Find'

targetFolder = 'target_folder_path_here'

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
  if ["ini"].include? fileExt.downcase
    return true
  else
    return false
  end
end

def processFile path
  fr = open path, "rb"
  content = fr.read
  fr.close

  # fw = open path, "wb"
  # fw.write content
  # fw.close
end

each_file targetFolder do |path|
  if isTargetFile path
    processFile path
  end
end