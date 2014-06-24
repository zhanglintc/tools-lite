#encode utf-8

def lastone(number, key):
    peoples = []
    for i in range(number):
        peoples.append(i)

    i = 0
    while(True):
        i += 1
        print("I'm No.%2d, %2d times" % (peoples[i], ( i % key )+( key if i % key == 0 else 0 )))
        if( i == 11): break

    # print (len(peoples))

if __name__ == '__main__':
    lastone(13, 3)