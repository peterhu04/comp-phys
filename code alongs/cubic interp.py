import numpy as np
from matplotlib import pyplot as plt
plt.ion()

def fun(x):
  return 1/np.log(x)

x=np.linspace(2,3,21) #21 points btwn 2,3
y=fun(x)
print(x)
plt.clf()
plt.plot(x,y)
plt.plot(x,y,'*')
plt.show

xx=np.linspace(x[1],x[-2],1001)
yy=0*xx
tmp = 0*xx

for i in range(len(xx)):
  for j in range(len(x)):
    if x[j]<i:
      
  ind=np.argmax(xx[i]>x) #found index of left hand neighbor
  tmp[i]=ind
  fitp=np.polyfit(xx[ind-1:i]+3,y[ind-1:ind+3],3) #fit polynomial to lh neighbor-1 to right +1
  print(fitp)


#not exactly working...
