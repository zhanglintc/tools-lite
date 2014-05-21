import os
import sys
import subprocess

ftuple=os.walk(r"C:\\")

print("Searching...")
for root,dirs,files in ftuple:
    for tmp_file in files:
        if(tmp_file=="QQ.exe"):
            break
print("done")
p=subprocess.Popen(os.path.join(root,tmp_file))
