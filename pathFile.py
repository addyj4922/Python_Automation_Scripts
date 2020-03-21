import os
counter=1
dict={}
path1=[]
path1=os.environ.get('PATH').split(";")
for i in path1:
    dict.update(counter,path1[i])
for key, value in dict:
    print("{0}: {1}".format(key,value))