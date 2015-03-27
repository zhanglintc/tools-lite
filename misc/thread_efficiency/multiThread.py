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

    t0 = myTread(dataList[MULTIPLE * 0 : MULTIPLE * 1])
    t1 = myTread(dataList[MULTIPLE * 1 : MULTIPLE * 2])
    t2 = myTread(dataList[MULTIPLE * 2 : MULTIPLE * 3])
    t3 = myTread(dataList[MULTIPLE * 3 : MULTIPLE * 4])
    t4 = myTread(dataList[MULTIPLE * 4 : MULTIPLE * 5])
    t5 = myTread(dataList[MULTIPLE * 5 : MULTIPLE * 6])
    t6 = myTread(dataList[MULTIPLE * 6 : MULTIPLE * 7])
    t7 = myTread(dataList[MULTIPLE * 7 : MULTIPLE * 8])
    t8 = myTread(dataList[MULTIPLE * 8 : MULTIPLE * 9])
    t9 = myTread(dataList[MULTIPLE * 9 : MULTIPLE * 10])


    start = time.clock()

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

    while(len(globalList) < 10):
        pass

    end = time.clock()
    print("The function has run: %.03f seconds" %(end - start))

    print("maximal is: {}".format(max(globalList)))

    try:
        input()
    except:
        pass


