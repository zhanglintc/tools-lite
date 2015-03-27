# -*- coding: utf-8 -*-

MULTIPLE = 10000000
dataFileName = "big_data.txt"

if __name__ == '__main__':
    with open(dataFileName, "wb") as fw:
        for i in range(10):
            for loop in range(1 * MULTIPLE):
                fw.write(str(i) + ",")

