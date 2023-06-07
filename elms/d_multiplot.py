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

fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7)=plt.subplots(nrows=7, ncols=1, sharex=True)

#-----------------------------------------------------------------------------------------edg8/tbeo + bolo/topo
dda_p='EDG8'
dtype_p='TBEO'
dda_b='BOLO'
dtype_b='TOPO'

p = ppf.ppfdata(shot, dda_p, dtype_p, uid=user)[0]
p_time = ppf.ppfdata(shot, dda_p, dtype_p , uid=user)[2]-dt
p_out=p*1e-7
b = ppf.ppfdata(shot, dda_b, dtype_b, uid=user)[0]
b_time = ppf.ppfdata(shot, dda_b, dtype_b , uid=user)[2]-dt

ax1.set_title('ELMs behaviour (a.u.)')
ax1.set_xlim(tmin,tmax)
ax1.set_ylim(0,0.6*1e8)
ax1.axvline(t1-dt, linestyle='--', color='green')
ax1.axvline(t2-dt, linestyle='--', color='red')
ax1.plot(b_time, b, color ='black', label=r'bolo/topo $\cdot 10^{-7}$')
ax1.plot(p_time, p_out, color ='blue', label='edg8/tbeo')
ax1.legend()

#-------------------------------------------------------------------------------------andamento temporale delle frequenze per le due diagnostiche
dda_b2='ELML'
dtype_b2='FREQ'
dda_p2='ELML'
dtype_p2='FRKS'

p2 = ppf.ppfdata(shot, dda_p2, dtype_p2, uid=user)[0]
p2_time = ppf.ppfdata(shot, dda_p2, dtype_p2, uid=user)[2]-dt
b2 = ppf.ppfdata(shot, dda_b2, dtype_b2, uid=user)[0]
b2_time = ppf.ppfdata(shot, dda_b2, dtype_b2, uid=user)[2]-dt

ax2.set_title('ELMs frequency (Hz)')
ax2.set_xlim(tmin,tmax)
ax2.axvline(t1-dt, linestyle='--', color='green')
ax2.axvline(t2-dt, linestyle='--', color='red')
ax2.plot(b2_time, b2, color='black')
ax2.plot(p2_time, p2, color='blue')

#----------------------------------------------------------------------------------------andamento temporale della frequenza media (media fatta su intervalli di 50 ms)
arrb2_time=[]
arrb2_val=[]

dim=b2_time.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (b2_time[index_i+cont]-b2_time[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+b2[i]
        media=somma/(index_f-index_i)
        tempo=(b2_time[index_f-1]+b2_time[index_i])/2
        arrb2_val.append(media)
        arrb2_time.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp2_time=[]
arrp2_val=[]

dim=p2_time.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p2_time[index_i+cont]-p2_time[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p2[i]
        media=somma/(index_f-index_i)
        tempo=(p2_time[index_f-1]+p2_time[index_i])/2
        arrp2_val.append(media)
        arrp2_time.append(tempo)
        cont=1
        index_i=index_f
        somma=0

ax3.set_title('Average frequency')
ax3.axvline(t1-dt, linestyle='--', color='green')
ax3.axvline(t2-dt, linestyle='--', color='red')
ax3.plot(arrb2_time, arrb2_val, color='black')
ax3.plot(arrp2_time, arrp2_val, color='blue')
ax3.set_xlim(tmin,tmax)

vectb2_time=[]
vectb2_val=[]

for i in range(0, len(arrb2_time)-1):
    rapp=arrb2_val[i+1]/arrb2_val[i]
    time=(arrb2_time[i]+arrb2_time[i+1])/2
    vectb2_val.append(rapp)
    vectb2_time.append(time)

vectp2_time=[]
vectp2_val=[]

for i in range(0, len(arrp2_time)-1):
    rapp=arrp2_val[i+1]/arrp2_val[i]
    time=(arrp2_time[i]+arrp2_time[i+1])/2
    vectp2_val.append(rapp)
    vectp2_time.append(time)

ax4.set_title('Ratio frequency')
ax4.axvline(t1-dt, linestyle='--', color='green')
ax4.axvline(t2-dt, linestyle='--', color='red')
ax4.plot(vectb2_time, vectb2_val, color='black')
ax4.plot(vectp2_time, vectp2_val, color='blue')
ax4.set_xlim(tmin,tmax)
ax4.set_ylim(0,5)

#-----------------------------------------------------------------------------------------andamento temporale della dimensione
dda_b3='ELML'
dtype_b3='SIZE'
dda_p3='ELML'
dtype_p3='SIKS'

b3 = ppf.ppfdata(shot, dda_b3, dtype_b3, uid=user)[0]
b3_time = ppf.ppfdata(shot, dda_b3, dtype_b3, uid=user)[2]-dt
p3 = ppf.ppfdata(shot, dda_p3, dtype_p3, uid=user)[0]
p3_time = ppf.ppfdata(shot, dda_p3, dtype_p3, uid=user)[2]-dt

ax5.set_title('ELMs size')
ax5.set_xlim(tmin,tmax)
ax5.set_ylim(0,1e7)
ax5.axvline(t1-dt, linestyle='--', color='green')
ax5.axvline(t2-dt, linestyle='--', color='red')
ax5.plot(b3_time, b3, color='black')
ax5.plot(p3_time, p3, color='blue')

#-------------------------------------------------------------------------------------andamento temporale della size media (media fatta su intervalli di 50 ms)
arrb3_time=[]
arrb3_val=[]

dim=b3_time.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (b3_time[index_i+cont]-b3_time[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+b3[i]
        media=somma/(index_f-index_i)
        tempo=(b3_time[index_f-1]+b3_time[index_i])/2
        arrb3_val.append(media)
        arrb3_time.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp3_time=[]
arrp3_val=[]

dim=p3_time.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p3_time[index_i+cont]-p3_time[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p3[i]
        media=somma/(index_f-index_i)
        tempo=(p3_time[index_f-1]+p3_time[index_i])/2
        arrp3_val.append(media)
        arrp3_time.append(tempo)
        cont=1
        index_i=index_f
        somma=0


ax6.set_title('Average size')
ax6.axvline(t1-dt, linestyle='--', color='green')
ax6.axvline(t2-dt, linestyle='--', color='red')
ax6.plot(arrb3_time, arrb3_val, color='black')
ax6.plot(arrp3_time, arrp3_val, color='blue')
ax6.set_xlim(tmin,tmax)
ax6.set_ylim(0,1e7)

vectb3_time=[]
vectb3_val=[]

for i in range(0, len(arrb3_time)-1):
    rapp=arrb3_val[i+1]/arrb3_val[i]
    time=(arrb3_time[i]+arrb3_time[i+1])/2
    vectb3_val.append(rapp)
    vectb3_time.append(time)

vectp3_time=[]
vectp3_val=[]

for i in range(0, len(arrp3_time)-1):
    rapp=arrp3_val[i+1]/arrp3_val[i]
    time=(arrp3_time[i]+arrp3_time[i+1])/2
    vectp3_val.append(rapp)
    vectp3_time.append(time)

ax7.set_title('Ratio size')
ax7.axvline(t1-dt, linestyle='--', color='green')
ax7.axvline(t2-dt, linestyle='--', color='red')
ax7.plot(vectb3_time, vectb3_val, color='black')
ax7.plot(vectp3_time, vectp3_val, color='blue')
ax7.set_xlim(tmin,tmax)
ax7.set_ylim(0,7)

plt.show()

