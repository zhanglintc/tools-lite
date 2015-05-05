#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("date > tmp")

with open("tmp", "rb") as fr:
    if "Fri" not in fr.read():
        os.system('/home/lane/wb/src/wb.py -t "今天是星期五吗？不是…"')

    else:
        os.system('/home/lane/wb/src/wb.py -t "今天是星期五吗？是！"')

os.system("rm tmp")



