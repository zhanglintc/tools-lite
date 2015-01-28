# coding=utf-8

import os
import urllib

# down load get-pip.py
def report_hook(count, block_size, total_size):
    print '%02d%%'%(100.0 * count * block_size/ total_size)

url = 'https://raw.github.com/pypa/pip/master/contrib/get-pip.py'
print 'download begin, please waite...'

file_path, headers = urllib.urlretrieve(url, reporthook = report_hook)

with open(file_path, "rb") as fr:
    data = fr.read()

with open('./download.py','w') as fw:
    fw.write(data)

print 'download success, installing...'

# install pip by calling get-pip.py
import download
download.main()

print 'clearing up...'
filepath=['./download.py','./download.pyc']

try:
    for path in filepath:
        os.remove(path)
except :
    pass

print "insall pip success, please ADD '\Python27\Scripts' to your enveronment path"