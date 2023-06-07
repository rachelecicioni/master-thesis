import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat8 

user='JETPPF'

shot=96482 #shot D

ppf.ppfgo()

#Setting shift temporale(dt) e tempo massimo e minimo per la visualizzazione del plot
dt=40
dt_bis=0.3
t1=48
t2=49.986
tmin=t1-dt-dt_bis
tmax=t2-dt+dt_bis
#Indico con p=pmt (quindi i segnale di KS3)
#Indico con b=bolometer (quindi i segnali di KB5)

fig, (ax1, ax2)=plt.subplots(1, 2)

dda_b2='ELML'
dtype_b2='FREQ'
dda_p2='ELML'
dtype_p2='FRKS'

p2 = ppf.ppfdata(shot, dda_p2, dtype_p2, uid=user)[0]
p2_time = ppf.ppfdata(shot, dda_p2, dtype_p2, uid=user)[2]-dt
b2 = ppf.ppfdata(shot, dda_b2, dtype_b2, uid=user)[0]
b2_time = ppf.ppfdata(shot, dda_b2, dtype_b2, uid=user)[2]-dt

dda_b3='ELML'
dtype_b3='SIZE'
dda_p3='ELML'
dtype_p3='SIKS'

b3 = ppf.ppfdata(shot, dda_b3, dtype_b3, uid=user)[0]
b3_time = ppf.ppfdata(shot, dda_b3, dtype_b3, uid=user)[2]-dt
p3 = ppf.ppfdata(shot, dda_p3, dtype_p3, uid=user)[0]
p3_time = ppf.ppfdata(shot, dda_p3, dtype_p3, uid=user)[2]-dt

ax1.hist2d(p2, p3, bins=10, cmap='Blues')
ax1.set_title('KS3 D')
ax1.set_xlabel('frequency')
ax1.set_ylabel('size')

ax2.hist2d(b2, b3, bins=11, cmap='Blues')
ax2.set_title('bolometer D')
ax2.set_xlabel('frequency')
ax2.set_ylabel('size')

plt.show()
