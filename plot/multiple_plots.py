import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat8 
plt.rcParams['font.family']='monospace'

user='JETPPF'

shot_d=96482
shot_t=99282
shot_dt=99863

ppf.ppfgo()

dt=40
tmin=0
tmax=13

fig, (ax1, ax2, ax3, ax4, ax5, ax6)=plt.subplots(nrows=6, ncols=1, sharex=True)
fig.suptitle(r'$I_p$=3.5 MA')

#------------------------------------------------------------------------------------- corrente di plasma in funzione del tempo
dda_1='MAGN'
dtype_1='IPLA'

ip_d = ppf.ppfdata(shot_d, dda_1, dtype_1, uid=user)[0]
ip_t = ppf.ppfdata(shot_t, dda_1, dtype_1, uid=user)[0]
ip_dt = ppf.ppfdata(shot_dt, dda_1, dtype_1, uid=user)[0]
ip_time_d = ppf.ppfdata(shot_d, dda_1, dtype_1 , uid=user)[2]-dt
ip_time_t = ppf.ppfdata(shot_t, dda_1, dtype_1 , uid=user)[2]-dt
ip_time_dt = ppf.ppfdata(shot_dt, dda_1, dtype_1 , uid=user)[2]-dt

ip_d_out=-1*1e-6*ip_d #così lo mette in MA e lo rigira
ip_t_out=-1*1e-6*ip_t
ip_dt_out=-1*1e-6*ip_dt

ax1.set_ylabel(r'$I_p$ (MA)')
ax1.set_title('(a)', loc='left', pad=-14)
ax1.set_xlim(tmin, tmax)
ax1.plot(ip_time_d, ip_d_out, color ='blue')
ax1.plot(ip_time_t, ip_t_out, color ='magenta')
ax1.plot(ip_time_dt, ip_dt_out, color ='orange')
ax1.legend(['D 96482', 'T 99282', 'DT 99863'])

#-------------------------------------------------------------------------------------- total coupled power in fuzione del tempo
dda_2='ICRH'
dtype_2='PTOT'
dda_3='NBI'
dtype_3='PTOT'

icrh_ptot_d = ppf.ppfdata(shot_d, dda_2, dtype_2, uid=user)[0]
icrh_ptot_t = ppf.ppfdata(shot_t, dda_2, dtype_2, uid=user)[0]
icrh_ptot_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2, uid=user)[0]
icrh_ptot_time_d = ppf.ppfdata(shot_d, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_t = ppf.ppfdata(shot_t, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2 , uid=user)[2]-dt

nbi_ptot_d = ppf.ppfdata(shot_d, dda_3, dtype_3, uid=user)[0]
nbi_ptot_t = ppf.ppfdata(shot_t, dda_3, dtype_3, uid=user)[0]
nbi_ptot_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3, uid=user)[0]
nbi_ptot_time_d = ppf.ppfdata(shot_d, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_t = ppf.ppfdata(shot_t, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_out_d=1e-6*nbi_ptot_d #mette in MW
nbi_ptot_out_t=1e-6*nbi_ptot_t
nbi_ptot_out_dt=1e-6*nbi_ptot_dt

icrh_ptot_d_out=1e-6*icrh_ptot_d
icrh_ptot_t_out=1e-6*icrh_ptot_t
icrh_ptot_dt_out=1e-6*icrh_ptot_dt

ax2.set_ylabel(r'$P_{NBI}, P_{ICRH}$ (MW)')
ax2.set_title('(b)', loc='left', pad=-14)
ax2.plot(nbi_ptot_time_d, nbi_ptot_out_d, color='blue')
ax2.plot(nbi_ptot_time_t, nbi_ptot_out_t, color='magenta')
ax2.plot(nbi_ptot_time_dt, nbi_ptot_out_dt, color='orange')
ax2.plot(icrh_ptot_time_d, icrh_ptot_d_out, color='blue')
ax2.plot(icrh_ptot_time_t, icrh_ptot_t_out, color='magenta')
ax2.plot(icrh_ptot_time_dt, icrh_ptot_dt_out, color='orange')

#-------------------------------------------------------------------------------------energia MHD in funzione del tempo
dda_4='EFIT'
dtype_4='WP'

wmhd_d = ppf.ppfdata(shot_d, dda_4, dtype_4, uid=user)[0]
wmhd_t = ppf.ppfdata(shot_t, dda_4, dtype_4, uid=user)[0]
wmhd_dt = ppf.ppfdata(shot_dt, dda_4, dtype_4, uid=user)[0]
wmhd_time_d = ppf.ppfdata(shot_d, dda_4, dtype_4 , uid=user)[2]-dt
wmhd_time_t = ppf.ppfdata(shot_t, dda_4, dtype_4 , uid=user)[2]-dt
wmhd_time_dt = ppf.ppfdata(shot_dt, dda_4, dtype_4 , uid=user)[2]-dt

wmhd_d_out=1e-6*wmhd_d
wmhd_t_out=1e-6*wmhd_t
wmhd_dt_out=1e-6*wmhd_dt

ax3.set_ylabel(r'$E_p$ (MJ)')
ax3.set_title('(c)', loc='left', pad=-14)
ax3.plot(wmhd_time_d, wmhd_d_out, color='blue')
ax3.plot(wmhd_time_t, wmhd_t_out, color='magenta')
ax3.plot(wmhd_time_dt, wmhd_dt_out, color='orange')

#-------------------------------------------------------------------------------------neutron rate
dda_5='TIN'
dtype_5='RNT'

rnt_d = ppf.ppfdata(shot_d, dda_5, dtype_5, uid=user)[0]*100
#rnt_t = ppf.ppfdata(shot_t, dda_5, dtype_5, uid=user)[0]
rnt_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5, uid=user)[0]
rnt_time_d = ppf.ppfdata(shot_d, dda_5, dtype_5 , uid=user)[2]-dt
#rnt_time_t = ppf.ppfdata(shot_t, dda_5, dtype_5 , uid=user)[2]-dt
rnt_time_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5 , uid=user)[2]-dt

rnt_out_d=1e-18*rnt_d
#rnt_out_t=1e-18*rnt_t
rnt_out_dt=1e-18*rnt_dt

ax4.set_ylabel(r'rnt $10^{-18}s^{-1}$') #nell'handbook non c'è UDM
ax4.set_title('(d)', loc='left', pad=-14)
ax4.plot(rnt_time_d, rnt_out_d, color='blue')
#ax4.plot(rnt_time_t, rnt_out_t, color='magenta')
ax4.plot(rnt_time_dt, rnt_out_dt, color='orange')

#------------------------------------------------------------------------------------------- temperatura elettronica

dda_6='ECM1'
dtype_6='TMAX'

tmax_d = ppf.ppfdata(shot_d, dda_6, dtype_6, uid=user)[0]
tmax_t = ppf.ppfdata(shot_t, dda_6, dtype_6, uid=user)[0]
tmax_dt = ppf.ppfdata(shot_dt, dda_6, dtype_6, uid=user)[0]
tmax_time_d = ppf.ppfdata(shot_d, dda_6, dtype_6 , uid=user)[2]-dt
tmax_time_t = ppf.ppfdata(shot_t, dda_6, dtype_6 , uid=user)[2]-dt
tmax_time_dt = ppf.ppfdata(shot_dt, dda_6, dtype_6 , uid=user)[2]-dt

tmax_d_out=1e-2*tmax_d
tmax_t_out=1e-2*tmax_t
tmax_dt_out=1e-2*tmax_dt

ax5.set_ylabel(r'$T_e^{max}$ (keV)')
ax5.set_title('(e)', loc='left', pad=-14)
ax5.plot(tmax_time_d, tmax_d_out, color='blue')
ax5.plot(tmax_time_t, tmax_t_out, color='magenta')
ax5.plot(tmax_time_dt, tmax_dt_out, color='orange')

#----------------------------------------------------------------------------------------------densità
dda_7='LIDX'
dtype_7='NELA'

nela_d = ppf.ppfdata(shot_d, dda_7, dtype_7, uid=user)[0]
nela_t = ppf.ppfdata(shot_t, dda_7, dtype_7, uid=user)[0]
nela_dt = ppf.ppfdata(shot_dt, dda_7, dtype_7, uid=user)[0]
nela_time_d = ppf.ppfdata(shot_d, dda_7, dtype_7 , uid=user)[2]-dt
nela_time_t = ppf.ppfdata(shot_t, dda_7, dtype_7 , uid=user)[2]-dt
nela_time_dt = ppf.ppfdata(shot_dt, dda_7, dtype_7 , uid=user)[2]-dt

nela_out_d=1e-19*nela_d
nela_out_t=1e-19*nela_t
nela_out_dt=1e-19*nela_dt

ax6.set_xlabel("time (s)")
ax6.set_ylabel(r'$n_e \cdot 10^{-19}(m^{-2})$')
ax6.set_title('(f)', loc='left', pad=-14)
ax6.plot(nela_time_d, nela_out_d, color='blue')
ax6.plot(nela_time_t, nela_out_t, color='magenta')
ax6.plot(nela_time_dt, nela_out_dt, color='orange')

plt.show()

fig.savefig('/home/jnv7243/PLOT/figure/finale.pdf', format='pdf')
