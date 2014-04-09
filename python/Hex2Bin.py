
target_file = r"C:\Users\Lane\Desktop\card.txt"

def Hex2Bin(Hex):
    
    convert_dict = {
    '0':'0000',    '1':'0001',    '2':'0010',    '3':'0011',
    '4':'0100',    '5':'0101',    '6':'0110',    '7':'0111',
    '8':'1000',    '9':'1001',    'a':'1010',    'b':'1011',
    'c':'1100',    'd':'1101',    'e':'1110',    'f':'1111',    }

    return convert_dict[Hex]

if __name__ == '__main__': 
    fr = open(target_file,"r")
    fw = open("rlt.log","w")
    data = fr.readline()
    while data:
        ret = ''
        for i in range(8 - (len(data)-1)):
            ret = ret + '0000,'
        for i in range(len(data)-1):
            ret = ret + Hex2Bin(data[i]) + ','
        print(ret[:-1])
        print('\n')
        fw.write(ret[:-1]+'\n')
        data = fr.readline()