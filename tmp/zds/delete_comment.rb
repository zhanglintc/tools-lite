require 'Find'

Author  = "zhanglintc"
Version = "v0.4" 

targetFolder = './' # 在这里写你的鸡台球目标地址

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

  return ["basic.ini", "uisetup.ini"].include? fileName.downcase
end

# 逐行处理
def eachline fr
  to_reserver_list = [] # 保留flag
  to_retrun = ""

  fr.each do |line|
    line =~ /(2017.\d{1,2}.\d{1,2})/ # 找到所有包含日期的行

    # 如果找到了就处理
    if $1
      date_str = $1
      date_str.gsub! /\.|\//, "" # 删除其中所有的.和/, 这样2017.03.24或者2017/03/24全部变成20170324
      date_int = date_str.to_i # str => int

      next if date_int < 20170324 # 小于3月24号的一律忽略

      if to_reserver_list.include? date_int
        to_reserver_list.delete date_int # 如果该日期被保存过, 保留flag中删掉它(意味着-E到来)
        to_retrun << line if to_reserver_list == [] # 意味着某一个注释块的最后一行, 特殊处理一下
      else
        to_reserver_list << date_int # 如果该日期 未 被保存过, 保留flag中保存它(意味着-S到来)
      end
    end

    # 如果是注释行  and  如果to_reserver_list为空,   毫不犹豫忽略
    next if line =~ /^\s*;.*/ and to_reserver_list == [] and line.include? "//"
    to_retrun << line # 未被忽略的最后要返回
  end

  return to_retrun
end

def processFile path
  # 读文件并处理
  fr = open path, "rb"
  to_retrun = eachline fr
  fr.close

  # 按老板的要求:
  to_retrun.gsub! /^\s+\r\n/, "\r\n" # 先删除只有空格的行里的空格
  to_retrun.gsub! /(?:^\r\n)+/, "\r\n" #　然后多行变一行

  # 写回去
  # fw = open path, "wb"
  # fw.write to_retrun
  # fw.close
end

each_file targetFolder do |path|
  if isTargetFile path
    puts path
    processFile path
  end
end

