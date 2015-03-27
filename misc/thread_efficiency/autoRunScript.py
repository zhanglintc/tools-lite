# -*- coding: utf-8 -*-

import anyThread

def autoRunScript():
    fw = open("timeCost.txt", "wb")

    for i in range(1, 11):
        timeCost = anyThread.anyThread(i)
        fw.write("Quantity: {} --- Time: {}\n".format(i, timeCost))

        reload(anyThread)

    fw.close()


if __name__ == '__main__':
    autoRunScript()

    try:
        input()
    except:
        pass


