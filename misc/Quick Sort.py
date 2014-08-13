lst = [13, 5, 111, 2.5, 10, 12]

def sort(data):
    if len(data) == 1:
        return data

    lst1 = []
    lst2 = []

    for i in range(len(data)):
        if i == 0:
            continue

        if data[i] <= data[0]:
            lst1.append(data[i])
        else:
            lst2.append(data[i])

    lst2.append(data[0])

    lst1 = sort(lst1)
    lst2 = sort(lst2)
    return lst1 + lst2

print(sort(lst))
