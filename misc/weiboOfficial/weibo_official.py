'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

from weibo import APIClient
# from snspy import SinaWeiboMixin

import time
import codecs

import webbrowser
APP_KEY = '2038131539' # app key
APP_SECRET = 'b4d84f59af3e5a52c8df1f0e7ccfa75d' # app secret
CALLBACK_URL = 'http://zhanglintc.blog.163.com' # callback url
# TOKEN = {u'access_token': u'2.00_ShHyB2HnvNCca83c087d04aFAkC', u'remind_in': u'157679999', u'uid': u'1804547715', u'expires_at': 1569833194}


if 0: # get token
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()    # redirect the user to 'url'
    # print url
    webbrowser.open(url, new=0, autoraise=True)

    ACCESS = raw_input("input your code here:\n")

    r = client.request_access_token(ACCESS)
    ACCESS_TOKEN = r.access_token
    EXPIRES_TIME = r.expires      # token expires time, UNIX timestamp, e.g., 1384826449.252 (10:01 am, 19 Nov 2013, UTC+8:00)

    print ACCESS_TOKEN
    print EXPIRES_TIME


else: # use token
    ACCESS_TOKEN='2.00_ShHyB2HnvNCca83c087d04aFAkC'
    EXPIRES_TIME=1569833194
    client2 = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL, access_token=ACCESS_TOKEN)

    fw = open('comments.txt', 'wb')
    for my_page in range(1, 5):
        print('Page {} is downloading'.format(my_page))
        received = client2.comments.to_me.get(uid = 1804547715, page = my_page, count = 20)

        fw.write('\n\nPage {}:\n'.format(my_page).encode('utf8'))
        for detail in received.comments:
            # print detail.text.encode('utf8')
            to_be_written = detail.created_at + ': ' + detail.text + ' by ' + detail.user.name + '\n'
            fw.write(to_be_written.encode('utf8'))

        fw.flush()

    fw.close()
    print('All the comments have downloaded')


# end of file








