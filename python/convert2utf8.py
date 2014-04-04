'''
Convert encoding of files in given folder to uft-8.
'''

import os
import codecs
import chardet
import time

# set your python version True
Python2 = False
Python3 = True

# put your target folder address here:(if you are using drag function, this is useless)
target_folder=r"F:\Example\target_folders"
# set your target file type:
fExt = ["c","cpp","h","txt","rc","ini"]

################################################################
# functions:
################################################################
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

def GetEncodingInfo(datas):
    '''
    return datas' encoding info and relevant confidence
    '''
    result_dict = chardet.detect(datas)
    encoding_type = result_dict['encoding']#get encoding
    confidence = result_dict['confidence']#get confidence
    return encoding_type,confidence

def WriteAsUtf_8(target_file):
    ''' try to convert target_file encoding type to uft-8
        True for success
        False for error occured
    '''
    global log_for_write
    try:
        # read and detect file
        fr = codecs.open(target_file)#open target file
        datas = fr.read()#read content
        encoding_type,confidence = GetEncodingInfo(datas)
        fr.close()#close file
        log_for_print = 'tpye: ' + str(encoding_type) + ' with ' + str(confidence*100) + '% ' + str(target_file) + '\n'
        print(log_for_print)#print sth
        log_for_write += log_for_print

        # decode and encode
        datas = datas.decode(encoding_type)#decode cotent by useing detected encoding type
        datas = datas.encode('utf-8-sig')#encode in utf-8
        
        # rewirte file
        fw = open(target_file,'wb')#open target file using write mode
        fw.write(datas)#rewrite to original file
        fw.close()#close file
        return True

    except:
        log_for_print = 'Errored in tpye: ' + str(encoding_type) + ' with ' + str(confidence*100) + '% ' + str(target_file) + '\n'
        print(log_for_print)#print error infomation
        log_for_write += log_for_print
        return False

################################################################
# main:
################################################################
if __name__=="__main__":
    log_for_write = ''
    if Python2:
        target_folder = str(raw_input("Drag your folder here:\n"))
    elif Python3:
        target_folder = str(input("Drag your folder here:\n"))
    if target_folder[0] == '\"':# if target folder contain space, i will start with "
        target_folder = target_folder[1:-1]# so strip it
    start = time.time()
    FTuple = os.walk(target_folder)
    for root,dirs,files in FTuple:
        for tmp_file in files:        
            if IsTargetFile(tmp_file):
                target_file = os.path.join(root,tmp_file)
                WriteAsUtf_8(target_file)
    end = time.time()
    last = end -start
    print(str(last))
    f = open('log.dat','w')
    f.write(log_for_write)
    f.write(str(last))
    f.close()
    print('\n')
    if Python2:
        raw_input("Convert finished, press any key to close")
    elif Python3:
        input("Convert finished, press any key to close")

