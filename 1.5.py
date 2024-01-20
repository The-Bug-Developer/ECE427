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
t = np.arange(0,2*pi*0.005,step)
Vin = np.zeros(len(t))
Vout = np.zeros(len(t))
for i in range(len(t)):
    Vin[i] = 12*sqrt(2)*sin(60*2*pi*i*step)
    Vout[i] = abs(12*sqrt(2)*sin(60*2*pi*i*step))

plt.figure(figsize=(20,10))

plt.plot(t,Vout,'b')
plt.plot(t,Vin,'r.')
plt.ylabel('v(t) V',size = 12)
plt.legend(['$Vout$','$Vin$'],prop={'size': 25},loc = 2)
plt.xlabel('t (ms)',size = 12)
plt.title('Figure 5.1',size=18)
plt.grid(which='both')
plt.savefig('Figure_5.1.png',dpi=600)

for i in range(len(t)):
    Vin[i] = 12*sqrt(2)*sin(60*2*pi*i*step)
    Vout[i] = abs((12*sqrt(2)-1.2)*sin(60*2*pi*i*step))
    if(abs(Vin[i])<1.2):
        Vout[i] = 0
        
plt.figure(figsize=(20,10))

plt.plot(t,Vout,'b')
plt.plot(t,Vin,'r.')
plt.ylabel('v(t) V',size = 12)
plt.legend(['$Vout$','$Vin$'],prop={'size': 25},loc = 2)
plt.xlabel('t (ms)',size = 12)
plt.title('Figure 5.2',size=18)
plt.grid(which='both')
plt.savefig('Figure_5.2.png',dpi=600)

now = datetime.now()
change = now-First_time

print(change)