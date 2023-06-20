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

ppf.ppfgo()
fig, (ax1, ax2, ax3)=plt.subplots(nrows=3, ncols=1, sharex=True)

#wmhd
wmhd = getdat('xg/rtss/wmhd', pulse)[0]
wmhd_t = getdat('xg/rtss/wmhd', pulse)[1]

ax1.plot(wmhd_t,wmhd)
ax1.set_xlim(tmin,tmax)
ax1.set_ylabel("WMHD")

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

#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]

ax3.plot(elm_t,elm)
ax3.set_xlim(tmin,tmax)
ax3.set_ylabel("elm")
ax3.set_ylim(0,1e13)

plt.show()
