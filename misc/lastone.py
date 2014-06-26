#encode utf-8

class Man:
    def __init__(self, number):
        self.number = number
        self.next = None

def lastone_new(number, key):
    man_head = None
    man_this = None
    man_cache = None
    counter = 1

    for i in range(number):
        man_new = Man(i + 1)

        if man_head == None:
            man_head = man_new
            man_this = man_head
        else:
            man_this.next = man_new
            man_this = man_new

    man_cache = man_this
    man_this.next = man_head
    man_this = man_head

    while True:
        print("I'm No.%2d, %2d times" % (man_this.number, counter % key + ( key if counter % key == 0 else 0 )))

        if counter % key == 0:
            print("No.%2d has been excuted\n" % (man_this.number))
            man_cache.next = man_this.next
            man_this = man_this.next
        else:
            man_cache = man_this
            man_this = man_this.next

        counter += 1

        if man_this.next == man_this:
            break

    print("Congratulations, No.%2d is survived" % (man_this.number))

def lastone(number, key):
    peoples = []
    counter = 1
    thisPeople = 0

    for i in range(number):
        peoples.append(i + 1)


    while True:
        print("I'm No.%2d, %2d times" % (peoples[thisPeople], counter % key + ( key if counter % key == 0 else 0 )))

        if counter % key == 0:
            print("No.%2d has been excuted" % (peoples[thisPeople]))
            peoples.pop(thisPeople)
            thisPeople -= 1
            print("Survivers:", peoples, "\n")

        counter += 1
        thisPeople += 1

        if thisPeople >= len(peoples):
            thisPeople = 0
        if len(peoples) == 1:
            break

    print("Congratulations, No.%2d is survived" % (peoples[0]))

if __name__ == '__main__':
    lastone_new(13, 3)