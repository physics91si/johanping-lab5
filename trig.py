#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.

import numpy as np
import matplotlib.pyplot as plt


# TODO fill in this function
def integrate(y,dx):
   return np.sum(y*dx)

# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y

x = np.arange(0,np.pi,0.01)
y = np.sin(x)
z = np.cos(x)

print("The integral of sin(x) over x with dx = 0.01  is ")
print(integrate(y,0.01))

print("The integral of cos(x) over x with dx = 0.01  is ")
print(integrate(z,0.01))

#plot cos curve
plt.figure()
plt.plot(x,z)
plt.show()

#plot sin curve
plt.figure
plt.plot(x,y)
plt.show()



