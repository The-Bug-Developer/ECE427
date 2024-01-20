import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sig
from math import pi, exp, cos, sin, log, sqrt
from control import margin
from control import tf
from datetime import datetime

now = datetime.now()
step = 1e-4
First_time = now
t = np.arange(0,2*pi*0.01,step)
def phased(inp):
    return float(inp*pi/180)
I4,I5,I6,I1,I2,I3 = np.zeros(len(t)), np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t)),np.zeros(len(t))
I = 33.45


for i in range(len(t)):
    I1[i] = I*sin(60*2*pi*i*step+ phased(8.19))
    I2[i] = I*sin(60*2*pi*i*step+ phased(128))
    I3[i] = I*sin(60*2*pi*i*step+ phased(248))
    I4[i] = 19.3*sin(60*2*pi*i*step+ phased(-21.8))
    I5[i] = 19.3*sin(60*2*pi*i*step+ phased(98.2))
    I6[i] = 19.3*sin(60*2*pi*i*step+ phased(218))



    
plt.figure(figsize=(20,10))
plt.plot(t,I1,'r')
plt.plot(t,I2,'b')
plt.plot(t,I3,'g')

plt.ylabel('i(t) A',size = 12)
plt.legend(['$I_A$','$I_B$','$I_C$'],prop={'size': 25},loc = 2)
plt.xlabel('t (ms)',size = 12)
plt.title('Figure 4.1',size=18)
plt.grid(which='both')
plt.savefig('Figure_4.1.png',dpi=600)

plt.figure(figsize=(20,10))
plt.plot(t,I1,'r')
plt.plot(t,I2,'b')
plt.plot(t,I3,'g')

plt.ylabel('i(t) A',size = 12)
plt.legend(['$I_A$','$I_B$','$I_C$'],prop={'size': 25},loc = 2)
plt.xlabel('t (ms)',size = 12)
plt.title('Figure 4.2',size=18)
plt.grid(which='both')
plt.savefig('Figure_4.2.png',dpi=600)

now = datetime.now()
change = now-First_time

print(change)