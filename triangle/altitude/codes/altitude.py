import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

omat = np.array([[0, 1], [-1, 0]])
def dir_vec(A, B):
    return B - A

def norm_vec(A, B):
    return omat @ dir_vec(A, B) 
    
#random vertices generated
A=np.array([0,-3])
B=np.array([4,1])
C=np.array([-2,0])

def alt_foot(A,B,C):
  m = B-C
  n = omat@m 
  N=np.block([[m],[n]])
  p = np.zeros(2)
  p[0] = m@A 
  p[1] = n@B
  #Intersection
  P=np.linalg.inv(N.T)@p
  return P

D1 =  alt_foot(A,B,C)
E1 =  alt_foot(B,C,A)
F1 =  alt_foot(C,A,B)
print(f"D1:{D1},E1:{E1},F1:{F1}")
#parameters of altitudes
m_AD1=dir_vec(A,D1)
n_AD1=norm_vec(A,D1)
c_AD1=norm_vec(A,D1)@A
print(f"AD1-m:{m_AD1},n:{n_AD1},c:{c_AD1}")
m_BE1=dir_vec(B,E1)
n_BE1=norm_vec(B,E1)
c_BE1=norm_vec(B,E1)@B
print(f"BE1-m:{m_BE1},n:{n_BE1},c:{c_BE1}")
m_CF1=dir_vec(C,F1)
n_CF1=norm_vec(C,F1)
c_CF1=norm_vec(C,F1)@C
print(f"CF1-m:{m_CF1},n:{n_CF1},c:{c_CF1}")

def line_intersect(n1,A1,n2,A2):
  N=np.block([[n1],[n2]])
  p = np.zeros(2)
  p[0] = n1@A1
  p[1] = n2@A2
  #Intersection
  P=np.linalg.solve(N,p)
  return P

#point H  
H=line_intersect(n_BE1,B,n_CF1,C)
print(f"H:{H}")

#plot
def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AD1 = line_gen(D1,A)
x_BE1 = line_gen(B,E1)
x_CF1 = line_gen(C,F1)
x_CE1 = line_gen(C,E1)
x_CD1 = line_gen(C,D1)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AD1[0,:],x_AD1[1,:],label='$AD_1$')
plt.plot(x_BE1[0,:],x_BE1[1,:],label='$BE_1$')
plt.plot(x_CF1[0,:],x_CF1[1,:],label='$CF_1$')
plt.plot(x_CE1[0,:],x_CE1[1,:],linestyle='dotted')
plt.plot(x_CD1[0,:],x_CD1[1,:],linestyle='dotted')

A = A.reshape(-1,1)
B = B.reshape(-1,1)
C = C.reshape(-1,1)
D1 = D1.reshape(-1,1)
E1 = E1.reshape(-1,1)
F1 = F1.reshape(-1,1)
H = H.reshape(-1,1)
tri_coords = np.block([[A,B,C,D1,E1,F1,H]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','$D_1$','$E_1$','$F_1$','H']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.savefig("altitude.png",bbox_inches='tight')
