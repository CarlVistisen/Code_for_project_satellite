
import numpy as np 
import matplotlib.pyplot as plt
#np.random.seed(4)



    
X1=[0]
Y1=[1.5]
t_list1=[0]
t=0
T=10
dt1=1/20000
a=0.3
b=0.6
c=0.3
Xn=0
Yn=0.1
    
steps1=int(np.round(T/dt1,0))
dW1 = np.sqrt(dt1)*(np.random.normal(0,1,steps1))
for i in range(steps1):
    
    Xnt=Xn+dt1*Yn
    Yn=Yn-dt1*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn)+0.5*(a**2)*((np.sin(Xn)+Yn*b)*(np.cos(Xn)*Yn+b)))-dW1[i]*(np.sin(Xn)+Yn*b)*a
    Xn=Xnt
    X1.append(Xn)
    Y1.append(Yn)
    t+=dt1
    t_list1.append(t)
        
X_array1=np.array(X1)
Y_array1=np.array(Y1)
t_array1=np.array(t_list1)
    





X=[0]
Y=[1.5]
t_list=[0]
t=0

dt=1/100
Xn=0
Yn=100

steps=int(np.round(T/dt,0))
dW = (np.zeros(steps))
f=int(dt/dt1)
g=f*steps
for i in range(steps):
    for k in range(f):
         dW[i]+=dW1[i*f+k]
        

for i in range(steps):   
    Xnt=Xn+dt*Yn
    Yn=Yn-dt*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn)+0.5*(a**2)*((np.sin(Xn)+Yn*b)*(np.cos(Xn)*Yn+b)))-dW[i]*(np.sin(Xn)+Yn*b)*a
    Xn=Xnt
    X.append(Xn)
    Y.append(Yn)
    t+=dt
    t_list.append(t)
    
X_array=np.array(X)
Y_array=np.array(Y)
t_array=np.array(t_list)



X2=[0]
Y2=[1.5]
t_list2=[0]
t=0
dt2=1/80

Xn=0
Yn=100

steps=int(np.round(T/dt2,0))
s = (np.random.normal(0,0,steps))
dW = (np.zeros(steps))
f=int(dt/dt1)
g=f*steps
for i in range(steps):
    for k in range(f):
        dW[i]+=dW1[i*f+k]
        


for i in range(steps):
    
    Xnt=Xn+dt*Yn
    Yn=Yn-dt*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn)+0.5*(a**2)*((np.sin(Xn)+Yn*b)*(np.cos(Xn)*Yn+b)))-dW[i]*(np.sin(Xn)+Yn*b)*a
    Xn=Xnt
    X2.append(Xn)
    Y2.append(Yn)
    t+=dt2
    t_list2.append(t)
    
X_array2=np.array(X2)
Y_array2=np.array(Y2)
t_array2=np.array(t_list2)




X3=[0]
Y3=[1.5]
t_list3=[0]
t=0
dt3=1/40
Xn=0
Yn=100

steps=int(np.round(T/dt3,0))
dW2 = np.zeros(steps)
f2=int(dt2/dt1)
g=f2*steps
for i in range(steps):
    for k in range(f2):
        dW2[i]+=dW1[i*f2+k]
        
for i in range(steps):
        
    Xnt=Xn+dt2*Yn
    Yn=Yn-dt2*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn)+0.5*(a**2)*((np.sin(Xn)+Yn*b)*(np.cos(Xn)*Yn+b)))-dW2[i]*(np.sin(Xn)+Yn*b)*a
    Xn=Xnt
    X3.append(Xn)
    Y3.append(Yn)
    t+=dt3
    t_list3.append(t)
    
X_array3=np.array(X3)
Y_array3=np.array(Y3)
t_array3=np.array(t_list3)

    


plt.plot(t_array,X_array, marker='o')
plt.plot(t_array1,X_array1, marker='.')
plt.plot(t_array2,X_array2, marker='.')
plt.plot(t_array3,X_array3, marker='.')
plt.xlabel("t")
plt.ylabel("X")
plt.title("t versus X")
plt.show()


dt_list=[dt,dt2,dt3]

error=[np.abs(X_array1[-1]-X_array[-1]),np.abs(X_array1[-1]-X_array2[-1]),np.abs(X_array1[-1]-X_array3[-1])]

plt.plot(dt_list,error, marker='o')

plt.xlabel("t")
plt.ylabel("X")
plt.title("t versus X")
plt.show()