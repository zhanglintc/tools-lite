# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os

TITLE    = "Blat Hello Mail"
CONTENT  = "This is a test mail send by blat"
MAILTO   = "mailto@domain.com"
USERNAME = "yourname@domain.com"
PASSWORD = "yourpassword"
SMTP     = "smtp.domain.com"
TIMES    = 1

def blat_send():
    # blat -install [SMTP server] [username] [try times] [port]
    os.system("blat -install {0} {1} 3 25".format(SMTP, USERNAME))

    for i in range(TIMES):
        # blat -body CONTENT -to MAILTO -s TITLE -u USERNAME -pw PASSWORD
        os.system(
            'blat -body "{0}" -to "{1}" -s "{2}" -u "{3}" -pw "{4}"'.format(
                CONTENT,
                MAILTO,
                TITLE,
                USERNAME,
                PASSWORD,
                )
            )


if __name__ == '__main__':
    blat_send()


