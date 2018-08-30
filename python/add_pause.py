import os

fExt = ["bat"]
for i in range(len(fExt)):
    fExt[i] = fExt[i].strip().lower()

def IsTargetFile(FileName):
    sufix = os.path.splitext(FileName)[1][1:]

    if sufix.lower() in fExt:
        return True
    else:
        return False

FTuple = os.walk(r"E:\ZDS_Working_SVN\trunk\KMSrc_2.06.05\Driver\Driver\BUILD")
f_log = open('not_utf8.log', 'w')
for root,dirs,files in FTuple:
    for Tmpfile in files:
        if IsTargetFile(Tmpfile):
            print(Tmpfile) # print something makes user know program is running
            line_number = 1
            try:
                of = os.path.join(root,Tmpfile)
                fr = open(of, 'r')
                fw = open('temp.txt', 'w')
                line = True
                while line:
                    line = fr.readline()
                    if "call" in line and ':' not in line and 'rem' not in line and 'REM' not in line:
                        fw.write("echo {} at {}\n".format(line_number, of.split('\\')[-1]))
                        line_number += 1
                        fw.write("pause>nul\n")
                        line_number += 1
                    fw.write(line)
                    line_number += 1

                fr.close()
                fw.close()
                os.remove(of)
                os.rename('temp.txt', of)
            except:
                f_log.write(of)

f_log.close()
