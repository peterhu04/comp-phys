import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate
plt.ion()

def fun(x):
  return 1/np.log(x)

x=np.linspace(2,3,21) #21 points btwn 2,3
dx=x[1]-x[0]
y=fun(x)

