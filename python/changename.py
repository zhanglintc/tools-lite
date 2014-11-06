# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os

tup = os.walk(r'D:\KMWinDrv_VSS\000Common\04.Tools\AutoGenCodeReviewBook\html\Pki')

for root, dirs, files in tup:
    for f in files[:]:
        of = os.path.join(root,f)
        nf = of.replace('_P','')
        # nf = os.path.join(root,'own_xps_'+f)
        os.rename(of, nf)