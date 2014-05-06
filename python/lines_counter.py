'''
count lines in given folder
'''

import os
import sys


# count blank lines or not
cnt_blank_lines = True
# judge your python version
version = sys.version[0]

fExt = ["c",'cpp','h','py']
target_folder = r"F:\SVN-Workspace\sanguosha\trunk\src"

def QuotationStrip(target_folder):
    if target_folder[0] == '\"':
        target_folder = target_folder[1:-1]
    return target_folder

def line_count(target_file):
    '''
    count and return given files
    '''
    f = open(target_file,"rb")
    datas = f.readline()
    cnt = 0
    while datas:
        datas = f.readline()
        if cnt_blank_lines == False: # if not count blank lines, jump it
            if datas == b'\r\n':     # data in blank lines is b'\r\n'
                continue             # so jump it
        #print(datas)
        cnt += 1
    #print(cnt)
    return cnt

def IsTargetFile(target_file):
    ''' to judge input file is target file type or not.
        True for is target_file
        False for not target_file
    '''
    sufix = os.path.splitext(target_file)[1][1:]    
    if sufix.lower() in fExt:
        return True
    else:
        return False

def traverse(target_folder):
    '''
    traverse given target and return lines of all the files
    '''
    FTuple = os.walk(target_folder)
    result = 0
    for root,dirs,files in FTuple:
        for tmp_file in files:
            if IsTargetFile(tmp_file):
                target_file = os.path.join(root,tmp_file)
                result += line_count(target_file)
    return str(result)


if __name__ == '__main__':
    if version == '2':
        target_folder = raw_input("Drag target folder here to count:\n")
        target_folder = QuotationStrip(target_folder)
        print(traverse(target_folder) + ' lines')
        raw_input("Press any key to close")
    elif version == '3':
        target_folder = input("Drag target folder here count:\n")
        target_folder = QuotationStrip(target_folder)
        print(traverse(target_folder) + ' lines')
        input("Press any key to close")
