import codecs
import chardet

def GetEncodingInfo(datas):
    '''
    return datas' encoding info and relevant confidence
    '''
    result_dict = chardet.detect(datas)
    encoding_type = result_dict['encoding']#get encoding
    confidence = result_dict['confidence']#get confidence
    return encoding_type,confidence

def ReadTxtFile(FilePathName):
    encodinglist = ["utf8","utf_8_sig","utf16","cp932","mbcs","ascii","cp936","cp1252"]
    
    f = open(FilePathName, "rb")
    datas = f.read()

    #encoding_type,confidence = GetEncodingInfo(datas)
    
    for EncodingName in encodinglist:#encoding_type,encodinglist:
        try:
            strs = codecs.decode(datas, EncodingName)
        except ValueError:
            continue

        f.close()
        return strs,EncodingName

    return "",""

class TxtFileHandle:
    def __init__( self ):
        self._EncodingName = "utf8"
        self._encodinglist = ["utf8","utf_8_sig","utf16","cp932","mbcs","ascii","cp936","cp1252"]
        self._FilePathName = ""

    def ReadTxtFile( self, FilePathName ):
        f = codecs.open(FilePathName, "rb")
        datas = f.read()

        #encoding_type,confidence = GetEncodingInfo(datas)
        
        for EncodingName in self._encodinglist:
            try:
                strs = codecs.decode(datas, EncodingName)
            except ValueError:
                continue

            f.close()
            self._FilePathName = FilePathName
            self._EncodingName = EncodingName
            return strs

        return ""

    def WriteTxtFile( self, strs):
        if "" == self._FilePathName:
            return False
        
        try:
            datas = codecs.encode( strs, self._EncodingName)
            
            f = open( self._FilePathName, "wb")
            f.write( datas )
            f.close()
            return True
        except:
            return False
