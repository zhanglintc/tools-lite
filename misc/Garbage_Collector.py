'''
 Refer to:
 http://blog.jobbole.com/53376/
'''

class Obj():
    def __init__(self, vm):
        if vm.numObjects == vm.maxObjects:
            gc(vm)

        self.next = vm.firstObject
        vm.firstObject = self

        self.marked = 0

        vm.numObjects += 1

class VM():
    def __init__(self):
        self.firstObject = None
        self.stackSize = 0
        self.numObjects = 0
        self.maxObjects = 8
        self.stack = []

    def push(self, val):
        obj = Obj(self)
        obj.value = val
        self.stackSize += 1
        self.stack.append(obj)

    def pop(self):
        self.stackSize -= 1
        return self.stack.pop()

def gc(vm):
    numObjects = vm.numObjects

    for i in range(vm.stackSize):
        vm.stack[i].marked = 1

    pointer = vm.firstObject

    while pointer:
        if not pointer.marked:
            unreached = pointer
            pointer = unreached.next
            # free(unreached)

            vm.numObjects -= 1

        else:
            pointer.marked = 0
            pointer = pointer.next

    vm.maxObjects = vm.numObjects * 2

    print "Collected {} objects, {} remaining.\n".format(numObjects - vm.numObjects, vm.numObjects)

def test1():
    print "Test 1: Objects on stack are preserved."

    vm = VM()

    vm.push(1)
    vm.push(2)
    vm.push(3)
    vm.push(4)

    gc(vm)

def test2():
    print "Test 2: Unreached objects are collected."

    vm = VM()

    vm.push(1)
    vm.push(2)
    vm.push(3)
    vm.push(4)

    vm.pop()
    vm.pop()

    gc(vm)

def perfTest():
    print "Performance Test."

    vm = VM()

    for i in range(1000):
        for j in range(20):
            vm.push(i)

        for k in range(20):
            vm.pop()

if __name__ == '__main__':
    test1()
    test2()
    perfTest()










