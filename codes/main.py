import numpy as np
from numpy import linalg as LA
A=np.array([1,-1])
B=np.array([-4,6])
C=np.array([-3,-5])
#finding the side lengths
a=np.linalg.norm(C-B)
b=np.linalg.norm(C-A)
c=np.linalg.norm(A-B)
#Incentre
I=np.array([(a*A[0]+b*B[0]+c*C[0])/(a+b+c),(a*A[1]+b*B[1]+c*C[1])/(a+b+c)])
print("I = ",I)
#finding k for E_3 and F_3
k1=((I-A)@(A-B))/((A-B)@(A-B))
k2=((I-A)@(A-C))/((A-C)@(A-C))
#finding E_3 and F_3
E3=A+(k1*(A-B))
F3=A+(k2*(A-C))
print("k1 = ",k1)
print("k2 = ",k2)
print("E3 = ",E3)
print("F3 = ",F3)

