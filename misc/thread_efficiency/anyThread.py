# -*- coding: utf-8 -*-

from makeData import MULTIPLE
from makeData import dataFileName
import threading
import time

thread_quantity = 1
threadList = []
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

    base = MULTIPLE * 10 / thread_quantity
    for i in range(thread_quantity):
        if i == 0:
            threadList.append(myTread(dataList[: base * (i + 1)]))

        elif i == thread_quantity - 1:
            threadList.append(myTread(dataList[base * i :]))

        else:
            threadList.append(myTread(dataList[base * i : base * (i + 1)]))

    # Start !!!
    print("Counting...")

    start = time.clock()

    for thread in threadList:
        thread.start()

    while(len(globalList) < thread_quantity):
        pass

    end = time.clock()
    print("The function has run: %.03f seconds" %(end - start))

    print("maximal is: {}".format(max(globalList)))
    print("thread_quantity is: {}".format(thread_quantity))
    # End !!!

    try:
        input()
    except:
        pass


