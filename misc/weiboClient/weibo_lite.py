from weibo import Client
import json
import time

DELAY_TIME = 0

API_KEY = '2038131539'            # app key
API_SECRET = 'b4d84f59af3e5a52c8df1f0e7ccfa75d'      # app secret
REDIRECT_URI = 'http://zhanglintc.blog.163.com'  # callback ur

#c = Client(API_KEY, API_SECRET, REDIRECT_URI)
#print c.authorize_url

#code = raw_input()

#c.set_code(code)

token = {u'access_token': u'2.00_ShHyB2HnvNCca83c087d04aFAkC', u'remind_in': u'157679999', u'uid': u'1804547715', u'expires_at': 1569833194}

fw = open('comments.txt', 'ab')

c2 = Client(API_KEY, API_SECRET, REDIRECT_URI, token)

my_page = 1
while my_page <= 25:
    try:
        print('page', my_page, 'downloading')
        received = c2.get('comments/to_me', uid = 1804547715, page = my_page)        

    except:
        print('page', my_page, 'has failed\n')
        time.sleep(DELAY_TIME)
        continue

    fw.write(b'\n\npage' + str(my_page).encode('utf8') + b':\n')
    for item in received['comments']:
        to_be_written = item['created_at'] + ': ' + item['text'] + ' by ' + item['user']['name'] + '\n'
        fw.write(to_be_written.encode('utf8'))

    time.sleep(DELAY_TIME)
    fw.flush()
    print('page', my_page, 'downloaded\n')
    my_page += 1
    
fw.close()

print('All the comments have downloaded')



