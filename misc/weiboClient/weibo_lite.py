from weibo import Client
import webbrowser
import json
import time

DELAY_TIME = 0

API_KEY = '2038131539' # app key
API_SECRET = 'b4d84f59af3e5a52c8df1f0e7ccfa75d' # app secret
REDIRECT_URI = 'http://zhanglintc.blog.163.com' # callback url
ACCESS_TOKEN = {u'access_token': u'2.00_ShHyB2HnvNCca83c087d04aFAkC', u'remind_in': u'157679999', u'uid': u'1804547715', u'expires_at': 1569833194}

def get_token_manually():
    '''
    Call this function if your 'ACCESS_TOKEN' is out of data,
    replace the 'ACCESS_TOKEN' above after the 'c.token' is printed.
    '''

    c = Client(API_KEY, API_SECRET, REDIRECT_URI)
    webbrowser.open(c.authorize_url)

    code = input('paste code here:\n')
    c.set_code(code)
    print(c.token)

def get_comments_to_me(start_page, end_page):
    '''
    Download comments from 'start_page' to 'end_page'
    '''
    my_client = Client(API_KEY, API_SECRET, REDIRECT_URI, ACCESS_TOKEN)
    my_page = start_page

    fw = open('comments.txt', 'ab')

    while my_page <= end_page:
        try:
            print('page', my_page, 'downloading')
            received = my_client.get('comments/to_me', uid = 1804547715, page = my_page)

        except:
            print('page', my_page, 'has failed\n')
            time.sleep(DELAY_TIME)
            continue

        fw.write(b'\n\npage' + str(my_page).encode('utf8') + b':\n')
        for item in received['comments']:
            to_be_written = item['created_at'] + ': ' + item['text'] + ' by ' + item['user']['name'] + '\n'
            fw.write(to_be_written.encode('utf8'))

        fw.flush()
        time.sleep(DELAY_TIME)
        print('page', my_page, 'downloaded\n')

        my_page += 1
        
    fw.close()
    print('All the comments have downloaded')

if __name__=="__main__":
    get_comments_to_me(1, 1)




