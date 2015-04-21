#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, re, os

def need_add(f_path):
    with open(f_path, "rb") as fr:
        content = fr.read()
        if "Problem Link:" in content:
            # print f_path
            return False

    return True

def add_link(f_path, url_link = None):
    with open(f_path, "rb") as fr:
        content = ""
        flag = False
        line = True
        while line:
            line = fr.readline()
            if flag:
                content += "\n# Problem Link:\n# {0}\n".format(url_link)
                flag = False

            if "zhanglin" in line:
                flag = True

            content += line

    # print content

    with open(f_path, "wb") as fw:
        print "writing: {0}".format(f_path)
        fw.write(content)

def main():
    url = "https://leetcode.com/problemset/algorithms"
    site = urllib.urlopen(url)
    content = site.read()

    pattern = '<a href="(.*?)">(.*?)</a>' # <a href="/problems/reverse-words-in-a-string-ii/">Reverse Words in a String II</a>
    web_info = re.findall(pattern, content)   # tup[0]: link   tup[1]: title

    # get web information
    target = "https://leetcode.com"
    web_dikt = {} # key: title    value: link
    for tup in web_info:
        web_dikt[tup[1]] = target + tup[0]

    # get local information
    local_path = r"E:\SVN-Space\leetcode\trunk\Python"
    local_files = {} # key: name   value: path
    tup = os.walk(local_path)
    for root, dirs, files in tup:
        for f in files:
            name = f[:-3] # python: f[:-3]   java: f[-5]   c++: f[-4]
            path = os.path.join(root, f)
            local_files[name] = path
            need_add(path)

    # add link
    for title in web_dikt:
        if "Pascal" in title:
            print title

        if title in local_files:
            if need_add(local_files[title]):
                add_link(local_files[title], web_dikt[title])
                pass

if __name__ == '__main__':
    main()


