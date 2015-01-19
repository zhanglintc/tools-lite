import codecs
# import chardet

# written by zhanglin
def GetEncodingInfo(data):
    '''
    return data' encoding info and relevant confidence
    '''
    # result_dict = chardet.detect(data)
    encoding_type = result_dict['encoding'] # get encoding
    confidence = result_dict['confidence'] # get confidence
    return encoding_type, confidence

def ReadTxtFile(filePathName):
    encodingList = ["utf8", "utf_8_sig", "utf16", "cp932", "mbcs", "ascii", "cp936", "cp1252"]
    
    f = open(filePathName, "rb")
    data = f.read()
    
    for encoding in encodingList: # encoding_type, encodingList:
        try:
            strs = codecs.decode(data, encoding)

        except ValueError:
            continue

        f.close()
        return strs, encoding

    return "",""

class TxtFileHandle:
    def __init__(self):
        self._encoding = "utf8"
        self._encodingList = ["utf8", "utf_8_sig", "utf16", "cp932", "ascii", "cp936", "cp1252"]
        self._filePathName = ""

    def ReadTxtFile(self, filePathName):
        """
        A generator which return one decoded line each time.
        """

        fr = codecs.open(filePathName, "rb")

        line = True
        while line:
            line = fr.readline()
            
            for encoding in self._encodingList:
                try:
                    line = codecs.decode(line, encoding)
                    break

                except ValueError:
                    continue

            self._filePathName = filePathName
            self._encoding = encoding

            yield line

        fr.close()

    def WriteTxtFile(self, strs):
        if "" == self._filePathName:
            return False
        
        try:
            data = codecs.encode(strs, self._encoding)
            
            f = open(self._filePathName, "wb")
            f.write(data)
            f.close()
            return True

        except:
            return False
