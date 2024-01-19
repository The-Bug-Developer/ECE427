import matplotlib.pyplot as plt
import numpy as np
from scipy import signal as sig
from math import pi, exp, cos, sin, log, sqrt
from control import margin
from control import tf
t = np.arange(0,5*1.5e-6,1e-8)
x = np.zeros(len(t))
Tau = 1.5e-6
for i in range(len(t)):
    x[i] = 3-2.8*exp(-t[i]/(Tau))

plt.figure(figsize=(20,10))
plt.plot(t,x,'k')
# plt.axis([ .1, Range, -60, 20])
for i in range(1,6):
    plt.axvline(i*Tau,color='PURPLE',linestyle='dotted')

plt.ylabel('v(t) V',size = 12)
plt.xlabel('t ($\mu$s)',size = 12)
plt.title('Figure 2.1',size=18)
plt.grid(which='both')
plt.savefig('Figure_2.1.png',dpi=600)


t = np.arange(0,1e-6,1e-8)
x = np.zeros(len(t))
Tau = 1.5e-6
for i in range(len(t)):
    x[i] = 3-2.8*exp(-t[i]/(Tau))
for i in range(int(len(t)*0.4),len(t)):
    x[i] = 0.855*exp((-t[i]+0.4e-6)/(Tau))
    
plt.figure(figsize=(20,10))
plt.plot(t,x,'k')
# plt.axis([ .1, Range, -60, 20])

plt.ylabel('v(t) V',size = 12)
plt.xlabel('t ($\mu$s)',size = 12)
plt.title('Figure 2.2',size=18)
plt.grid(which='both')
plt.savefig('Figure_2.2.png',dpi=600)