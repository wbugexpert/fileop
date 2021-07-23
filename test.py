import os,shutil
from posix import listdir
from hashlib import sha1

rootPath='/home/cwj/Desktop/test'
keyPath ='/home/cwj/Desktop/keyword.txt'
keyword=[]
hashlist=[]
def f1(path):
    ls=os.listdir(path)
    #print(cnt)
    for i in ls:
        if os.path.isdir(path+"/"+i):
            f1(path+"/"+i)
    cnt=len(os.listdir(path))
    if cnt==1 and path!=rootPath:
        tmp=os.path.basename(path)
        tmp1=(os.listdir(path))[0]
        shutil.move(path+"/"+tmp1,path+"/../"+tmp+"_"+tmp1)
    ls=os.listdir(path)
    cnt=len(ls)
    if cnt==0 and path!=rootPath:
        os.rmdir(path)
        return


def read_key(keyPath):
    for line in open(keyPath):
        index=line.find('\n')
        line=line[0:index]
        keyword.append(line)
    #print(keyword)

def f2(path,key):
    #print(key)
    ls=os.listdir(path)
    for i in ls:
        if os.path.isdir(path+"/"+i):
            f2(path+"/"+i,key)
        pos=i.find(key)
        if(pos!=-1):
            #print(i,"-----",pos)
            #print(path+"/"+i+"----------["+path+"/"+i[0:pos]+i[pos+len(key):len(i)]+"]")
            shutil.move(path+"/"+i,path+"/"+i[0:pos]+i[pos+len(key):len(i)])


def getSha1(filename): #计算sha1
    sha1Obj = sha1()
    with open(filename, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()

def f3(path):
    ls=os.listdir(path)
    for i in ls:
        if os.path.isdir(path+"/"+i):
            f3(path+"/"+i)
        else:
            hashkey=getSha1(path+"/"+i)
            flag=0
            for j in range(0,len(hashlist)):
                if hashkey==hashlist[j]:
                    flag=1
                    break
            if flag:
                os.remove(path+"/"+i)
            else:
                hashlist.append(hashkey)





read_key(keyPath)
keysize=len(keyword)
for i in range(0,keysize):
    f2(rootPath,keyword[i])
f3(rootPath)
f1(rootPath)


