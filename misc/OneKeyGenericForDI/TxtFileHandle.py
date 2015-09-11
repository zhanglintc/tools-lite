import codecs
import os

class TxtFileHandle:
    def __init__(self):
        self._encoding = "utf8"
        self._encodingList = ["utf8", "utf_8_sig", "utf16", "cp932", "mbcs", "ascii", "cp936", "cp1252"]
        self._filePathName = ""

    def ReadTxtFile(self, filePathName):
        """
        A generator which return one decoded line each time.
        """

        fr = codecs.open(filePathName, "rb")

        data = fr.read()
        for EncodingName in self._encodingList:
            try:
                data = codecs.decode(data, EncodingName)
                break

            except ValueError:
                continue

        self._filePathName = filePathName
        self._encoding = EncodingName

        fr.seek(0, os.SEEK_SET)

        data = data.split("\n")

        # remove last NULL string
        if not data[-1]:
            data.pop(-1)

        for line in data:
            yield line + "\n"

        fr.close()

    def WriteTxtFile(self, data):
        if "" == self._filePathName:
            return False
        
        try:
            data = codecs.encode(data, self._encoding)
            
            f = open(self._filePathName, "wb")
            f.write(data)
            f.close()
            return True

        except:
            return False
