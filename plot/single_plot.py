import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat8 

user='JETPPF'

shot_d=96482
shot_t=99282
shot_dt=99863

ppf.ppfgo()

dt=40


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

fig_ipla=plt.figure()

plt.xlabel("time (s)")
plt.ylabel(r'$I_p$ (MA)')
plt.title("Plasma current")
plt.xlim(0,35)
plt.plot(ip_time_d, ip_d_out, color ='blue', label='D 96482')
plt.plot(ip_time_t, ip_t_out, color ='magenta', label='T 99282')
plt.plot(ip_time_dt, ip_dt_out, color ='orange', label='DT 99863')
plt.legend()
fig_ipla.savefig('/home/jnv7243/PLOT/figure/i_p.pdf', format='pdf')
#-------------------------------------------------------------------------------------- total coupled power in fuzione del tempo
dda_2='ICRH'
dtype_2='PTOT'

icrh_ptot_d = ppf.ppfdata(shot_d, dda_2, dtype_2, uid=user)[0]
icrh_ptot_t = ppf.ppfdata(shot_t, dda_2, dtype_2, uid=user)[0]
icrh_ptot_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2, uid=user)[0]
icrh_ptot_time_d = ppf.ppfdata(shot_d, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_t = ppf.ppfdata(shot_t, dda_2, dtype_2 , uid=user)[2]-dt
icrh_ptot_time_dt = ppf.ppfdata(shot_dt, dda_2, dtype_2 , uid=user)[2]-dt

icrh_ptot_d_out=1e-6*icrh_ptot_d
icrh_ptot_t_out=1e-6*icrh_ptot_t
icrh_ptot_dt_out=1e-6*icrh_ptot_dt

fig_icrh_ptot=plt.figure()

plt.xlabel("time (s)")
plt.ylabel("Total Coupled Power ICRH (W)")
plt.title("Total Coupled Power ICRH")
plt.plot(icrh_ptot_time_d, icrh_ptot_d_out, color='blue', label='D 96482')
plt.plot(icrh_ptot_time_t, icrh_ptot_t_out, color='magenta', label='T 99282')
plt.plot(icrh_ptot_time_dt, icrh_ptot_dt_out, color='orange', label='DT 99863')
plt.legend()
fig_icrh_ptot.savefig('/home/jnv7243/PLOT/figure/tcp.pdf', format='pdf')
#------------------------------------------------------------------------------------- potenza NBI in funzione del tempo
dda_3='NBI'
dtype_3='PTOT'

nbi_ptot_d = ppf.ppfdata(shot_d, dda_3, dtype_3, uid=user)[0]
nbi_ptot_t = ppf.ppfdata(shot_t, dda_3, dtype_3, uid=user)[0]
nbi_ptot_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3, uid=user)[0]
nbi_ptot_time_d = ppf.ppfdata(shot_d, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_t = ppf.ppfdata(shot_t, dda_3, dtype_3 , uid=user)[2]-dt
nbi_ptot_time_dt = ppf.ppfdata(shot_dt, dda_3, dtype_3 , uid=user)[2]-dt

nbi_ptot_out_d=1e-6*nbi_ptot_d #mette in MW
nbi_ptot_out_t=1e-6*nbi_ptot_t
nbi_ptot_out_dt=1e-6*nbi_ptot_dt

fig_nbi_ptot=plt.figure()

plt.xlabel("time (s)")
plt.ylabel("Total NBI Power (MW)")
plt.title("Total NBI Power")
plt.plot(nbi_ptot_time_d, nbi_ptot_out_d, color='blue', label='D 96482')
plt.plot(nbi_ptot_time_t, nbi_ptot_out_t, color='magenta', label='T 99282')
plt.plot(nbi_ptot_time_dt, nbi_ptot_out_dt, color='orange', label='DT 99863')
plt.legend()
plt.show()
fig_nbi_ptot.savefig('/home/jnv7243/PLOT/figure/nbi_ptot.pdf', format='pdf')
#-------------------------------------------------------------------------------------NBI+ICRH
fig_nbi_icrh_ptot=plt.figure()

plt.xlabel("time (s)")
plt.ylabel("Total NBI and ICRH Power (MW)")
plt.title("Total NBI and ICRH Power")
plt.plot(nbi_ptot_time_d, nbi_ptot_out_d, color='blue', label='D 96482 - NBI')
plt.plot(nbi_ptot_time_t, nbi_ptot_out_t, color='magenta', label='T 99282 - NBI')
plt.plot(nbi_ptot_time_dt, nbi_ptot_out_dt, color='orange', label='DT 99863 - NBI')
plt.plot(icrh_ptot_time_d, icrh_ptot_d_out, color='cornflowerblue', label='D 96482 - ICRH')
plt.plot(icrh_ptot_time_t, icrh_ptot_t_out, color='violet', label='T 99282 - ICRH')
plt.plot(icrh_ptot_time_dt, icrh_ptot_dt_out, color='navajowhite', label='DT 99863 - ICRH')
plt.legend()
fig_nbi_icrh_ptot.savefig('/home/jnv7243/PLOT/figure/nbi_icrh_ptot.pdf', format='pdf')

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

fig_wmhd=plt.figure()
plt.xlabel("time (s)")
plt.ylabel(r'$E_p$ (MJ)')
plt.title("Plasma energy - MHD")
plt.plot(wmhd_time_d, wmhd_d_out, color='blue', label='D 96482')
plt.plot(wmhd_time_t, wmhd_t_out, color='magenta', label='T 99282')
plt.plot(wmhd_time_dt, wmhd_dt_out, color='orange', label='DT 99863')
plt.legend()
fig_wmhd.savefig('/home/jnv7243/PLOT/figure/wmhd.pdf', format='pdf')
#-------------------------------------------------------------------------------------neutron rate
dda_5='TIN'
dtype_5='RNT'

rnt_d = ppf.ppfdata(shot_d, dda_5, dtype_5, uid=user)[0]
rnt_t = ppf.ppfdata(shot_t, dda_5, dtype_5, uid=user)[0]
rnt_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5, uid=user)[0]
rnt_time_d = ppf.ppfdata(shot_d, dda_5, dtype_5 , uid=user)[2]-dt
rnt_time_t = ppf.ppfdata(shot_t, dda_5, dtype_5 , uid=user)[2]-dt
rnt_time_dt = ppf.ppfdata(shot_dt, dda_5, dtype_5 , uid=user)[2]-dt

rnt_out_d=1e-18*rnt_d
rnt_out_t=1e-18*rnt_t
rnt_out_dt=1e-18*rnt_dt

fig_rnt=plt.figure()

plt.xlabel("time (s)")
plt.ylabel(r'neutron rate $10^{-18}s^{-1}$') #nell'handbook non c'è UDM
plt.title("Total neutron rate")
plt.plot(rnt_time_d, rnt_out_d, color='blue', label='D 96482')
plt.plot(rnt_time_t, rnt_out_t, color='magenta', label='T 99282')
plt.plot(rnt_time_dt, rnt_out_dt, color='orange', label='DT 99863')
plt.legend()
fig_rnt.savefig('/home/jnv7243/PLOT/figure/rnt.pdf', format='pdf')

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

fig_tmax=plt.figure()

plt.xlabel("time (s)")
plt.ylabel(r'$T_e^{max}$ (keV)')
plt.title("Electron temperature max")
plt.plot(tmax_time_d, tmax_d_out, color='blue', label='D 96482')
plt.plot(tmax_time_t, tmax_t_out, color='magenta', label='T 99282')
plt.plot(tmax_time_dt, tmax_dt_out, color='orange', label='DT 99863')
plt.legend()
fig_tmax.savefig('/home/jnv7243/PLOT/figure/tmax.pdf', format='pdf')

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

fig_nela=plt.figure()

plt.xlabel("time (s)")
plt.ylabel(r'$n_e \cdot 10^{-19}(m^{-2})$')
plt.title("Linear density")
plt.plot(nela_time_d, nela_out_d, color='blue', label='D 96482')
plt.plot(nela_time_t, nela_out_t, color='magenta', label='T 99282')
plt.plot(nela_time_dt, nela_out_dt, color='orange', label='DT 99863')
plt.legend()
plt.show()
fig_nela.savefig('/home/jnv7243/PLOT/figure/nela.pdf', format='pdf')
