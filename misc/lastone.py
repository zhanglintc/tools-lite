#encode utf-8

def lastone(number, key):
    peoples = []
    counter = 1
    thisPeople = 0
    for i in range(number):
        peoples.append(i + 1)

    while(True):
        print("I'm No.%2d, %2d times" % (peoples[thisPeople], counter % key + ( key if counter % key == 0 else 0 )))
        if counter % key == 0:
            print("No.%2d has been excuted\n" % (peoples[thisPeople]))
            peoples.pop(thisPeople)
            thisPeople -= 1
        counter += 1
        thisPeople += 1
        if thisPeople >= len(peoples):
            thisPeople = 0        
        if len(peoples) == 1: 
            break
    print("Congratulations, No.%2d is survived" % (peoples[0]))

if __name__ == '__main__':
    lastone(13, 3)