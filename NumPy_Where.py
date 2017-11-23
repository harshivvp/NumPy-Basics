import numpy as np

A = np.array([0,1,2,2])
B = np.array([100,200,300,400])

condition = np.array([True,True,True,False])

answer = ([(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)])

print(answer)

#Using WHERE :

ans_with_where = np.where(condition,A,B)

print(','.join(tuple(map(str,ans_with_where))))

#################################################################################################

from numpy.random import randn

arr = randn(5,5)
print(arr)
print(np.where(arr<0,0,arr))
