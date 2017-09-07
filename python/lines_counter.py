"""
Description:
    Count lines in given folder

Author:
    Lane(zhanglintc)
"""

import os
import sys


# count blank lines or not
cnt_blank_lines = True
# judge your python version
version = sys.version[0]

ext_list = ['c','cpp','h','pl','pm', 't']
target_folder = r"Z:\golive"

def QuotationStrip(target_folder):
    """
    Strip quotation mark of given path
    """

    if target_folder[0] == '\"':
        target_folder = target_folder[1:-1]

    return target_folder

def line_count(target_file):
    """
    Count lines of given file
    """

    fr = open(target_file,"rb")
    data = fr.readline()
    lines = 0

    while data:
        data = fr.readline()
        if cnt_blank_lines == False:                # if not count blank lines, jump it
            if data == b'\r\n' or data == '\n':       # blank lines is b'\r\n' or b'\n'
                continue                              # so jump it

        lines += 1

    fr.close()
 
    return lines

def getExtension(target_file):
    """
    Get extension of target_file
    If not target extension, return None
    """

    extension = os.path.splitext(target_file)[1][1:].lower()

    if extension in ext_list:
        return extension

    else:
        return None

def traverse(target_folder):
    """
    Traverse given target and return lines of all the files
    """

    FTuple = os.walk(target_folder)
    result = {}

    for root,dirs,files in FTuple:
        for tmp_file in files:
            extension = getExtension(tmp_file)
            if extension:
                target_file = os.path.join(root,tmp_file)
                result[extension] = result.get(extension, 0) + line_count(target_file)

    # print result
    print("")
    print("all  -> {} lines\n".format(sum(result.values())))
    for key in result:
        print("{:<4} -> {} lines".format(key, result[key]))

if __name__ == '__main__':
    if version == '2':
        target_folder = raw_input("Drag target folder here to count:\n")
        target_folder = QuotationStrip(target_folder)
        traverse(target_folder)
        print("")
        raw_input("Press any key to close")

    elif version == '3':
        target_folder = input("Drag target folder here count:\n\n")
        target_folder = QuotationStrip(target_folder)
        traverse(target_folder)
        print("")
        input("Press any key to close")
