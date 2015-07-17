#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd, xlwt, re, xlutils.copy

target = r"C:\Users\zhanglin\Desktop\test.xls"

print "openning"
xlsfile = xlrd.open_workbook(target, formatting_info = True)

idx = 0
table = True
while (table):
    try:
        table = xlsfile.sheets()[idx]
        print idx, table.name.encode("utf-8")
        for i in range(3 - 1, table.nrows):
            line = table.cell(i, 4 - 1).value.encode("utf-8")
            if re.search('(KOAY..)A(.)', line):
                table.put_cell(i, 7 - 1, 1, u"●", 0)

            if re.search('36C\-9', line):
                table.put_cell(i, 7 - 1, 1, u"●", 0)

    except Exception, e:
        print Exception, e
        break

    idx += 1

print "coping"
wb = xlutils.copy.copy(xlsfile)
print "saving"
wb.save("aaaa.xls")