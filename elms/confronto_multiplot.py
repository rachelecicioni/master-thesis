import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat8 

user='JETPPF'

shot_d=96482 #shot D
shot_t=99282 #shot T
shot_dt=99863 #shot DT

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

fig, (ax1, ax2, ax3, ax4, ax5)=plt.subplots(nrows=5, ncols=1, sharex=True)

#scelgo come diagnostica KS3

#-----------------------------------------------------------------------------------------edg8/tbeo per trizio e deuterio
dda_p='EDG8'
dtype_p='TBEO'

p_d = ppf.ppfdata(shot_d, dda_p, dtype_p, uid=user)[0]
p_time_d = ppf.ppfdata(shot_d, dda_p, dtype_p , uid=user)[2]-dt
p_t = ppf.ppfdata(shot_t, dda_p, dtype_p, uid=user)[0]
p_time_t = ppf.ppfdata(shot_t, dda_p, dtype_p , uid=user)[2]-dt
p_dt = ppf.ppfdata(shot_dt, dda_p, dtype_p, uid=user)[0]
p_time_dt = ppf.ppfdata(shot_dt, dda_p, dtype_p , uid=user)[2]-dt

ax1.set_title('ELMs behaviour (a.u.)')
ax1.set_xlim(tmin,tmax)
ax1.set_ylim(0,3*1e14)
ax1.axvline(t1-dt, linestyle='--', color='green')
ax1.axvline(t2-dt, linestyle='--', color='red')
ax1.plot(p_time_d, p_d, color ='blue', label='D 96482')
ax1.plot(p_time_t, p_t, color ='magenta', label='T 99282')
ax1.plot(p_time_dt, p_dt, color ='orange', label='DT 99863')
ax1.legend()

#----------------------------------------------------------------------------------------andamento temporale della frequenza media (media fatta su intervalli di 50 ms)
dda_p2='ELML'
dtype_p2='FRKS'

p2_d = ppf.ppfdata(shot_d, dda_p2, dtype_p2, uid=user)[0]
p2_time_d = ppf.ppfdata(shot_d, dda_p2, dtype_p2, uid=user)[2]-dt
p2_t = ppf.ppfdata(shot_t, dda_p2, dtype_p2, uid=user)[0]
p2_time_t = ppf.ppfdata(shot_t, dda_p2, dtype_p2, uid=user)[2]-dt
p2_dt = ppf.ppfdata(shot_dt, dda_p2, dtype_p2, uid=user)[0]
p2_time_dt = ppf.ppfdata(shot_dt, dda_p2, dtype_p2, uid=user)[2]-dt

arrp2_time_d=[]
arrp2_val_d=[]

dim=p2_time_d.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p2_time_d[index_i+cont]-p2_time_d[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p2_d[i]
        media=somma/(index_f-index_i)
        tempo=(p2_time_d[index_f-1]+p2_time_d[index_i])/2
        arrp2_val_d.append(media)
        arrp2_time_d.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp2_time_t=[]
arrp2_val_t=[]

dim=p2_time_t.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p2_time_t[index_i+cont]-p2_time_t[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p2_t[i]
        media=somma/(index_f-index_i)
        tempo=(p2_time_t[index_f-1]+p2_time_t[index_i])/2
        arrp2_val_t.append(media)
        arrp2_time_t.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp2_time_dt=[]
arrp2_val_dt=[]

dim=p2_time_dt.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p2_time_dt[index_i+cont]-p2_time_dt[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p2_dt[i]
        media=somma/(index_f-index_i)
        tempo=(p2_time_dt[index_f-1]+p2_time_dt[index_i])/2
        arrp2_val_dt.append(media)
        arrp2_time_dt.append(tempo)
        cont=1
        index_i=index_f
        somma=0


ax2.set_title('Average frequency')
ax2.axvline(t1-dt, linestyle='--', color='green')
ax2.axvline(t2-dt, linestyle='--', color='red')
ax2.plot(arrp2_time_d, arrp2_val_d, color='blue')
ax2.plot(arrp2_time_t, arrp2_val_t, color='magenta')
ax2.plot(arrp2_time_dt, arrp2_val_dt, color='orange')
ax2.set_xlim(tmin,tmax)

vectp2_time_d=[]
vectp2_val_d=[]

for i in range(0, len(arrp2_time_d)-1):
    rapp=arrp2_val_d[i+1]/arrp2_val_d[i]
    time=(arrp2_time_d[i]+arrp2_time_d[i+1])/2
    vectp2_val_d.append(rapp)
    vectp2_time_d.append(time)

vectp2_time_t=[]
vectp2_val_t=[]

for i in range(0, len(arrp2_time_t)-5):
    rapp=arrp2_val_t[i+1]/arrp2_val_t[i]
    time=(arrp2_time_t[i]+arrp2_time_t[i+1])/2
    vectp2_val_t.append(rapp)
    vectp2_time_t.append(time)
    
vectp2_time_dt=[]
vectp2_val_dt=[]

for i in range(0, len(arrp2_time_dt)-5):
    rapp=arrp2_val_dt[i+1]/arrp2_val_dt[i]
    time=(arrp2_time_dt[i]+arrp2_time_dt[i+1])/2
    vectp2_val_dt.append(rapp)
    vectp2_time_dt.append(time)

ax3.set_title('Ratio frequency')
ax3.axvline(t1-dt, linestyle='--', color='green')
ax3.axvline(t2-dt, linestyle='--', color='red')
ax3.plot(vectp2_time_d, vectp2_val_d, color='blue')
ax3.plot(vectp2_time_t, vectp2_val_t, color='magenta')
ax3.plot(vectp2_time_dt, vectp2_val_dt, color='orange')
ax3.set_xlim(tmin,tmax)
#ax3.set_ylim(0,5)

#----------------------------------------------------------------------------------------andamento temporale della frequenza media (media fatta su intervalli di 50 ms)
dda_p3='ELML'
dtype_p3='SIKS'

p3_d = ppf.ppfdata(shot_d, dda_p3, dtype_p3, uid=user)[0]
p3_time_d = ppf.ppfdata(shot_d, dda_p3, dtype_p3, uid=user)[2]-dt
p3_t = ppf.ppfdata(shot_t, dda_p3, dtype_p3, uid=user)[0]
p3_time_t = ppf.ppfdata(shot_t, dda_p3, dtype_p3, uid=user)[2]-dt
p3_dt = ppf.ppfdata(shot_dt, dda_p3, dtype_p3, uid=user)[0]
p3_time_dt = ppf.ppfdata(shot_dt, dda_p3, dtype_p3, uid=user)[2]-dt

arrp3_time_d=[]
arrp3_val_d=[]

dim=p3_time_d.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p3_time_d[index_i+cont]-p3_time_d[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p3_d[i]
        media=somma/(index_f-index_i)
        tempo=(p3_time_d[index_f-1]+p3_time_d[index_i])/2
        arrp3_val_d.append(media)
        arrp3_time_d.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp3_time_t=[]
arrp3_val_t=[]

dim=p3_time_t.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p3_time_t[index_i+cont]-p3_time_t[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p3_t[i]
        media=somma/(index_f-index_i)
        tempo=(p3_time_t[index_f-1]+p3_time_t[index_i])/2
        arrp3_val_t.append(media)
        arrp3_time_t.append(tempo)
        cont=1
        index_i=index_f
        somma=0

arrp3_time_dt=[]
arrp3_val_dt=[]

dim=p3_time_dt.size
index_i=0
index_f=0
cont=1
somma=0
while (index_i+cont)<dim:
    if (p3_time_dt[index_i+cont]-p3_time_dt[index_i])<0.05:
        cont=cont+1
    else:
        index_f=index_i+cont
        for i in range(index_i, index_f):
            somma=somma+p3_dt[i]
        media=somma/(index_f-index_i)
        tempo=(p3_time_dt[index_f-1]+p3_time_dt[index_i])/2
        arrp3_val_dt.append(media)
        arrp3_time_dt.append(tempo)
        cont=1
        index_i=index_f
        somma=0

ax4.set_title('Average size')
ax4.axvline(t1-dt, linestyle='--', color='green')
ax4.axvline(t2-dt, linestyle='--', color='red')
ax4.plot(arrp3_time_d, arrp3_val_d, color='blue')
ax4.plot(arrp3_time_t, arrp3_val_t, color='magenta')
ax4.plot(arrp3_time_dt, arrp3_val_dt, color='orange')
ax4.set_xlim(tmin,tmax)

vectp3_time_d=[]
vectp3_val_d=[]

for i in range(0, len(arrp3_time_d)-1):
    rapp=arrp3_val_d[i+1]/arrp3_val_d[i]
    time=(arrp3_time_d[i]+arrp3_time_d[i+1])/2
    vectp3_val_d.append(rapp)
    vectp3_time_d.append(time)

vectp3_time_t=[]
vectp3_val_t=[]

for i in range(0, len(arrp3_time_t)-1):
    rapp=arrp3_val_t[i+1]/arrp3_val_t[i]
    time=(arrp3_time_t[i]+arrp3_time_t[i+1])/2
    vectp3_val_t.append(rapp)
    vectp3_time_t.append(time)

vectp3_time_dt=[]
vectp3_val_dt=[]

for i in range(0, len(arrp3_time_dt)-1):
    rapp=arrp3_val_dt[i+1]/arrp3_val_dt[i]
    time=(arrp3_time_dt[i]+arrp3_time_dt[i+1])/2
    vectp3_val_dt.append(rapp)
    vectp3_time_dt.append(time)

ax5.set_title('Ratio size')
ax5.axvline(t1-dt, linestyle='--', color='green')
ax5.axvline(t2-dt, linestyle='--', color='red')
ax5.plot(vectp3_time_d, vectp3_val_d, color='blue')
ax5.plot(vectp3_time_t, vectp3_val_t, color='magenta')
ax5.plot(vectp3_time_dt, vectp3_val_dt, color='orange')
ax5.set_xlim(tmin,tmax)
#ax5.set_ylim(0,5)

plt.show()
