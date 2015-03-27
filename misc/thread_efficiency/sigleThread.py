# -*- coding: utf-8 -*-

from makeData import MULTIPLE
from makeData import dataFileName
import threading
import time

globalList = []

class myTread(threading.Thread):
    def __init__(self, dataList):
        threading.Thread.__init__(self)
        self.dataList = dataList

    def run(self):
        maximal = 0
        global globalList

        for i in self.dataList:
            maximal = max(maximal, i)

        globalList.append(maximal)

if __name__ == '__main__':
    with open(dataFileName, "rb") as fr:
        dataList = fr.read().split(",")

    t0 = myTread(dataList[MULTIPLE * 0 : MULTIPLE * 10])

    start = time.clock()

    t0.start()

    while(len(globalList) < 1):
        pass

    end = time.clock()
    print("The function has run: %.03f seconds" %(end - start))

    print("maximal is: {}".format(max(globalList)))

    try:
        input()
    except:
        pass


