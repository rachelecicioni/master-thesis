import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0
tmin=47.0
tmax=50.0

pulse = int(input("Inserisci il run: "))
user='JETPPF'
user_s='jnv7243'
times = np.loadtxt('times_{}.txt'.format(pulse))

user='JETPPF'

ppf.ppfgo()
fig, (ax1, ax2, ax3, ax4)=plt.subplots(nrows=4, ncols=1, sharex=True)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]

ax1.plot(wmhd_t,wmhd)
ax1.set_xlim(tmin,tmax)
ax1.set_ylabel("WMHD")
for i in times:
    ax1.axvline(i)

#dens
dens = getdat('xg/rtss/pdlmLid', pulse)[0]
dens_t = getdat('xg/rtss/pdlmLid', pulse)[1]

minor_radius=getdat('gs/bl-minrad<s', pulse)[0]
minor_radius_t=getdat('gs/bl-minrad<s', pulse)[1]
minor_radius_final=np.interp(dens_t, minor_radius_t, minor_radius)

elongation = getdat('gs/bl-elo<s', pulse)[0]
elongation_t = getdat('gs/bl-elo<s', pulse)[1]
elongation_final=np.interp(dens_t, elongation_t, elongation)

dens_final=0.1*dens/(2*minor_radius_final*elongation_final)

ax2.plot(dens_t,dens_final)
ax2.set_xlim(tmin,tmax)
ax2.set_ylabel("dens (e17 m-3)")
for i in times:
    ax2.axvline(i)

#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]

ax3.plot(elm_t,elm)
ax3.set_xlim(tmin,tmax)
ax3.set_ylabel("elm")
ax3.set_ylim(0,1e13)
for i in times:
    ax3.axvline(i)



nearest_values_t=[] #array con tutti i tempi di wmhd relativi ad un ELMs
index_wmhd=[]
for i in times:
    diff=np.abs(wmhd_t-i)
    index=np.argmin(diff)
    nearest_values_t.append(wmhd_t[index])
    index_wmhd.append(index)

drop=[]
for k_corr, k_succ in zip(index_wmhd, index_wmhd[1:]):
    min_wmhd=np.min(wmhd[k_corr:k_succ])
    drop.append(np.abs(wmhd[k_corr]-min_wmhd))
drop.append(0)




ax4.plot(nearest_values_t, drop)
ax4.set_ylabel("drop")

plt.show()

