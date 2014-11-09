import urllib, urllib2
import datetime

today = str(datetime.date.today())

web = urllib.urlopen("https://github.com/zhanglintc")

# fw = open("git.txt", 'w')

line = True
while line:
    line = web.readline()
    if today in line and ('data-count="0"') in line: # if today's data-count is 0, do remind
        # call a remind function here
        print line
    # fw.write(line)

# fw.close()