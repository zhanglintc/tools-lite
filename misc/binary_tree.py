#encode utf-8

class Tree:
    def __init__(self, number):
        self.number = number
        self.LChild = None
        self.RChild = None

def tree_insert(tree_this, number):
    if tree_this == None:
        tree_new = Tree(number)
        tree_this = tree_new
    else:
        if number <= tree_this.number:
            tree_this.LChild = tree_insert(tree_this.LChild, number)
        else:
            tree_this.RChild = tree_insert(tree_this.RChild, number)
    return tree_this

def DLR(tree_this):
    if tree_this != None:
        print(tree_this.number)
        DLR(tree_this.LChild)
        DLR(tree_this.RChild)

def LDR(tree_this):
    if tree_this != None:
        LDR(tree_this.LChild)
        print(tree_this.number)
        LDR(tree_this.RChild)

def LRD(tree_this):
    if tree_this != None:
        LRD(tree_this.LChild)
        LRD(tree_this.RChild)
        print(tree_this.number)

if __name__ == '__main__':
    head = None
    head = tree_insert(head, 1)
    head = tree_insert(head, 2)
    head = tree_insert(head, 3)
    head = tree_insert(head, 4)
    head = tree_insert(head, 5)
    print('DLR:');DLR(head);
    print('LDR:');LDR(head);
    print('LRD:');LRD(head);