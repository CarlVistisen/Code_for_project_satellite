
import numpy as np 
import matplotlib.pyplot as plt
#np.random.seed(4)


error=[]
L1error1=0
L1error2=0
L1error3=0
L1error4=0
L1error5=0

L2error1=0
L2error2=0
L2error3=0
L2error4=0
L2error5=0

Yrefsum=0
Y2sum=0
Y3sum=0
Y4sum=0
Y5sum=0


for j in range(1000):    
    i_sr=400
    i2=200
    i3=100
    i4=80
    i5=50

    t_list1=[0]
    t=0
    T=20
    i1=np.lcm(np.lcm(np.lcm(i_sr,i2),np.lcm(i3,i4)),i5)
    dt1=1/i1
    a=0.3
    b=0.6
    c=0.3
    Xn=0
    Yn=0.1
        
    steps1=int(np.round(T/dt1,0))
    dW1 = np.sqrt(dt1)*(np.random.normal(0,1,steps1))
    for i in range(steps1):
        
        Xnt=Xn+dt1*Yn
        Yn=Yn-dt1*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW1[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt
        
    Xref=Xn
    Yref=Yn




    t=0
    dt=1/i_sr
    Xn=0
    Yn=0.1

    steps=int(np.round(T/dt,0))
    dW = (np.zeros(steps))
    f=int(dt/dt1)
    g=f*steps
    for i in range(steps):
        for k in range(f):
            dW[i]+=dW1[i*f+k]
        

    for i in range(steps):
        
        Xnt=Xn+dt*Yn
        Yn=Yn-dt*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt

    Xn0=Xn
    Yn0=Yn

    X2=[0]
    Y2=[0.1]
    t_list2=[0]
    t=0
    dt2=1/i2

    Xn=0
    Yn=0.1

    steps=int(np.round(T/dt2,0))
    dW2 = np.zeros(steps)
    f2=int(dt2/dt1)
    g=f2*steps
    for i in range(steps):
        for k in range(f2):
            dW2[i]+=dW1[i*f2+k]
        
    for i in range(steps):
        
        Xnt=Xn+dt2*Yn
        Yn=Yn-dt2*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW2[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt

    Xn2=Xn
    Yn2=Yn

    t=0
    dt3=1/i3
    Xn=0
    Yn=0.1
    steps=int(np.round(T/dt3,0))
    dW3 = np.zeros(steps)
    f3=int(dt3/dt1)
    g=f3*steps
    for i in range(steps):
        for k in range(f3):
            dW3[i]+=dW1[i*f3+k]
        
    for i in range(steps):
        
        Xnt=Xn+dt3*Yn
        Yn=Yn-dt3*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW3[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt
        
    Xn3=Xn
    Yn3=Yn
   

   
    t=0
    dt4=1/i4
    Xn=0
    Yn=0.1
    steps=int(np.round(T/dt4,0))
    dW4 = np.zeros(steps)
    f4=int(dt4/dt1)
    g=f4*steps
    for i in range(steps):
        for k in range(f4):
            dW4[i]+=dW1[i*f4+k]

    for i in range(steps):
        
        Xnt=Xn+dt4*Yn
        Yn=Yn-dt4*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW4[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt

    Xn4=Xn
    Yn4=Yn
    
    t=0
    
    dt5=1/i5
    Xn=0
    Yn=0.1
    steps=int(np.round(T/dt5,0))
    dW5 = np.zeros(steps)
    f5=int(dt5/dt1)
    g=f5*steps
    for i in range(steps):
        for k in range(f5):
            dW5[i]+=dW1[i*f5+k]

    for i in range(steps):
        
        Xnt=Xn+dt5*Yn
        Yn=Yn-dt5*(b*Yn+np.sin(Xn)-c*np.sin(2*Xn))-dW5[i]*(np.sin(Xn)+Yn*b)*a
        Xn=Xnt

    Xn5=Xn
    Yn5=Yn
    
    Yrefsum+=Yref
    Y2sum+=Yn2
    Y3sum+=Yn3
    Y4sum+=Yn4
    Y5sum+=Yn5
        
    
    L2error1+=(Yref-Yn0)**2
    L2error2+=(Yref-Yn2)**2
    L2error3+=(Yref-Yn3)**2
    L2error4+=(Yref-Yn4)**2
    L2error5+=(Yref-Yn5)**2
    
    
    L1error1+=np.abs(Xref-Xn0)
    L1error2+=np.abs(Xref-Xn2)
    L1error3+=np.abs(Xref-Xn3)
    L1error4+=np.abs(Xref-Xn4)
    L1error5+=np.abs(Xref-Xn5)
    print(j)

    


dt_list=[dt,dt2,dt3,dt4,dt5]
L2error=[np.sqrt(L2error1/100),np.sqrt(L2error2/100),np.sqrt(L2error3/100),np.sqrt(L2error4/100),np.sqrt(L2error5/100)]
L1error=[np.abs(L1error1/100),np.abs(L1error2/100),np.abs(L1error3/100),np.abs(L1error4/100),np.abs(L1error5/100)]

Weakerror=[np.abs(Yrefsum/1000),np.abs(Y2sum/1000),np.abs(Y3sum/1000),np.abs(Y4sum/1000),np.abs(Y5sum/1000)]

print(i1)
print(dt_list)
print(L2error)


print(np.var(dW), dt)
print(np.var(dW2), dt2)
print(np.var(dW3), dt3)
print(np.var(dW4), dt4)
print(np.var(dW5), dt5)

plt.plot(dt_list,L2error, marker='o')

plt.xlabel("t")
plt.ylabel("X")
plt.title("t versus X")
plt.show()