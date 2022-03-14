'''import json
import sys
import os

if len(sys.argv)>1:
    if os.path.exists(sys.argv[1]):
       with open(sys.argv[1],"r") as f:
           res=json.load(f)
           print("yes it is valid json file")
       
    else:
        print("it is invalid one please enter valid file name")
else:
    print("please enter file name")'''

'''import yaml
with open("practise.yaml","w+") as f:
    dct={'name':'srinitha','eid':'21241'}
    yaml.dump(dct,f)
    f.seek(0,0)
    res=yaml.full_load(f)
    print(res)'''

'''import json
with open("practise.yaml","w+") as f:
    dct={'name':'srinitha','eid':'21241'}
    json.dump(dct,f)
    f.seek(0,0)
    res=json.load(f)
    print(res)'''

'''import os
import sys
import platform
import subprocess

# Seeing if the file exists
if os.path.exists(sys.argv[1]):
    f = open(sys.argv[1], "r")
    f_contents = f.read()
    f.close()
else:
    print("Usage: copy2clip <file_name>")
    exit(1)

whatos = platform.system()
print(whatos)

if whatos == "Darwin":
    subprocess.run("pbcopy", universal_newlines=True, input=f_contents)
    print("success: copied to clipboard")
elif whatos == "Windows":
    subprocess.run("clip",universal_newlines=True ,input=f_contents)
    print("success: copied to clipboard")
else:
    print("failed: clipboard not supported")'''
'''import re
with open("first.txt","r") as f:
    dta="Hello jhjkhmn your mail is srinitha.chinthala@ojas-it.com"
    res=f.read()
    res1=re.split(r"[@-(\.)]",res)
    print(res1)'''

from itertools import combinations
inp=int(input("enter how many values you want to enter"))
lst=[1,2,3,4,5,6,7]
lst1=[]
lst2=[]
for i in combinations(lst,2):
 res1=i[0]*i[1]
 res2=i[0]+i[1]
 lst1.append(res1)
 lst2.append(res2)
res3=max(lst1)
res4=lst1.index(res3)
res5=lst2[res4]
print(res5)
'''lst=[1,2,9,4,5,6,7,8,9]
lst.sort()
res1=lst[len(lst)-2:]
res2=res[0]*res[1]'''























































    
