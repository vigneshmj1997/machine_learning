#done it
from sklearn import datasets
import numpy as np
import pandas as pd
file=pd.read_csv("train.csv")
target=np.array(file["label"])
data=np.array(file.drop(["label"],1))


import collections
from sklearn.cross_validation import train_test_split
from collections import Counter
X_train,X_test,Y_train,Y_test = train_test_split(data,target,test_size=0.1)
def distance(x,y):
    suma=0
    for i in range(0,len(x)):
        suma=(x[i]-y[i])**2+suma
    return (suma)    
def knear(sub,x,y):
    suma=[]
    count=[]
    for i in range(0,len(x)):
        num=distance(sub,x[i])
        suma.append(num)
        count.append(i)
        
    d=dict(zip(suma,count))
   # print(suma)
    suma.sort()
    check=[]
    for i in range(0,5):
        check.append(y[d[suma[i]]])
    maximum= max(k for k,v in Counter(check).items() if v>1)
    return maximum
        
        
        
        

suma=0
percent=0

for i in range(0,len(X_test)):
        #print(i)
    a=knear(X_test[i],X_train,Y_train)
        #print(a,Y_test[i])
    if(a==Y_test[i]):
            #print("same")
        suma = suma+1
            #print(suma)
percent=(suma/len(X_test)*100) +percent
print(percent)

    
                
        
    
    
