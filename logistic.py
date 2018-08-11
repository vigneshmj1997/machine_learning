from sklearn import datasets
iris=datasets.load_iris()
data=iris.data
data=data[:99]
target=iris.target
target=target[:99]
import math

def fun(a):

    return(1/(1+((math.e)**(-a))))


def sigma(coff,var):
    total=0
    for i in range(0,len(var)):
        total+=coff[i]*var[i]
    return(total)
import random 
coff=[]

for i in range(len(data[1])):
    coff.append(random.randint(1,20))

def gradient(coff,tar,data):
    for i in range(0,1000):
        
         for i in range(0,len(data)):
                 coff[i]+=0.1*(tar-fun(sigma(coff,data)))*data[i]
            
    ##print(fun(sigma(coff,data)),"   ",tar)       
print(coff)
count=0
for i in range(0,len(data)):
    tem=fun(sigma(coff,data[i]))
    if(tem!=target[i]):
        gradient(coff,target[i],data[i])
        count+=1 
#finding bias term       
print(count)
print(coff)
to=0
tem1=0
for i in range(0,int(len(data)/2)):
    a=1

    r=random.randint(0,len(data)-1)
    if(fun(sigma(coff,data[r]))<0.5):
        a=0
        
    print(target[r]," - ",a)
    if(target[r]==a):
        to+=1
print(to," ",len(data)/2)        
        

    

    


    
    
        
