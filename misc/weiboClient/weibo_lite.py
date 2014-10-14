#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lane's Weibo Client Application Beta, Nothing Reserved
"""

from weibo import Client
import webbrowser
import json
import pickle

# ACCESS_TOKEN = {u'access_token': u'2.00_ShHyB2HnvNCca83c087d04aFAkC', u'remind_in': u'157679999', u'uid': u'1804547715', u'expires_at': 1569833194}

API_KEY = '2038131539' # app key
API_SECRET = 'b4d84f59af3e5a52c8df1f0e7ccfa75d' # app secret
REDIRECT_URI = 'http://zhanglintc.blog.163.com' # callback url

def get_token_manually():
    """
    Call this function if your 'ACCESS_TOKEN' is out of data,
    replace the 'ACCESS_TOKEN' above after the 'c.token' is printed.

    Out of dated, plan to remove -> zhanglin 2014.10.14
    """

    c = Client(API_KEY, API_SECRET, REDIRECT_URI)
    webbrowser.open(c.authorize_url)

    code = input('paste code here:\n')
    c.set_code(code)
    print(c.token)

def update_access_token():
    """
    Get ACCESS_TOKEN form file 'token'. It will direct you to weibo.com to get
    a new ACCESS_TOKEN if failed to find the file 'token'.

    Try to delete file 'token' so that you can get a new one if this application
    not running correctly.
    """

    try:
        fr = open('token', 'rb')
        ACCESS_TOKEN = pickle.load(fr)
        fr.close()

    except FileNotFoundError:
        c = Client(API_KEY, API_SECRET, REDIRECT_URI)
        webbrowser.open(c.authorize_url)

        code = input('Paste code here:\n')
        c.set_code(code)

        fw = open('token', 'wb')
        pickle.dump(c.token, fw)
        fw.close()

        ACCESS_TOKEN = c.token

    return ACCESS_TOKEN

def get_comments_to_me(clinet, start_page, end_page):
    """Download comments from 'start_page' to 'end_page'"""

    my_page = start_page

    fw = open('comments.txt', 'wb')

    while my_page <= end_page:
        try:
            print('Page {} is downloading'.format(my_page))
            received = client.get('comments/to_me', count = 20, uid = 1804547715, page = my_page)

        except:
            print('Page {} is downloading has failed'.format(my_page))
            continue

        fw.write('\n\nPage {}:\n'.format(my_page).encode('utf8'))
        for item in received['comments']:
            to_be_written = item['created_at'] + ': ' + item['text'] + ' by ' + item['user']['name'] + '\n'
            fw.write(to_be_written.encode('utf8'))

        fw.flush()
        my_page += 1
        
    fw.close()
    print('All the comments have downloaded')


def get_friends_timeline(client):
    """Show 20 friends_timeline in the screen"""

    received = client.get('statuses/friends_timeline')
    i = 1
    for item in received['statuses']:
        print(('No.' + str(i) + ': ' + item['text'] + ' by @' + item['user']['name'] + '\n').encode('utf8'))
        i += 1

if __name__=="__main__":
    ACCESS_TOKEN = update_access_token()

    client = Client(API_KEY, API_SECRET, REDIRECT_URI, ACCESS_TOKEN)
    get_friends_timeline(client)
    # get_comments_to_me(client, 1, 5)




