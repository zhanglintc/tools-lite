lst = [13, 5, 111, 2.5, 10, 12]

def merge(lst1, lst2):
    lst = []
    while(len(lst1) > 0 and len(lst2) > 0):
        if lst1[0] < lst2[0]:
            lst.append(lst1[0])
            lst1.pop(0)
        else:
            lst.append(lst2[0])
            lst2.pop(0)
    
    if len(lst1) != 0:
        lst = lst + lst1
    else:
        lst = lst + lst2

    return lst

def sort(data):
    if len(data) < 2:
        return data
    half = len(data) // 2
    lst1 = data[0:half]
    lst2 = data[half:]
    lst1 = sort(lst1)
    lst2 = sort(lst2)
    ret = merge(lst1, lst2)
    return ret

print(sort(lst))
