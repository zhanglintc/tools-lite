import os

# count blank lines or not
cnt_blank_lines = True

fExt = ["c",'cpp','h','py']
target_folder = r"E:\SVN-Space\tools-lite"

def line_count(target_file):
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
    FTuple = os.walk(target_folder)
    result = 0
    for root,dirs,files in FTuple:
        for tmp_file in files:
            if IsTargetFile(tmp_file):
                target_file = os.path.join(root,tmp_file)
                result += line_count(target_file)
    return result

print(traverse(target_folder))
