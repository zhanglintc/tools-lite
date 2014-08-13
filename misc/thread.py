#encode utf-8

import threading

def pr():
    print('thr')

if __name__ == '__main__':
    t1 = threading.Thread(target = pr)
    t1.start()