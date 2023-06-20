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
pulse_s = 96745

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
ax2.set_ylabel("dens ")

#elm
elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]

ax3.plot(elm_t,elm)
ax3.set_xlim(tmin,tmax)
ax3.set_ylabel("elm")
ax3.set_ylim(0,1e13)

num_seq=int(input("Quante sequenze vuoi plottare?(#):  "))

if num_seq ==1:

    sequenza=input("Inserisci la sequenza: ")

    wmhd = ppf.ppfdata(pulse_s, 'JST', 'WTH',seq=sequenza, uid=user_s)
    ax1.plot(wmhd[2], wmhd[0], label=sequenza)
    ax1.legend()
    
    dens = ppf.ppfdata(pulse_s, 'JST', 'NEAV',seq=sequenza, uid=user_s)
    ax2.plot(dens[2], dens[0]*1e-19)

    elm = ppf.ppfdata(pulse_s, 'JST', 'XIBA',seq=sequenza, uid=user_s)
    ax3.plot(elm[2], elm[0]*1e13)

    plt.show(block=False)

else:
    sequenze=[]
    for i in range(num_seq):
        elemento=input("Inserisci  la {}^ sequenza: ".format(i+1))
        sequenze.append(elemento)

    for i in range(num_seq):
        wmhd = ppf.ppfdata(pulse_s, 'JST', 'WTH',seq=sequenze[i], uid=user_s)
        ax1.plot(wmhd[2], wmhd[0], label=sequenze[i] )
        ax1.set_ylabel("wmhd")
        ax1.legend()

        dens = ppf.ppfdata(pulse_s, 'JST', 'NEAV',seq=sequenze[i], uid=user_s)

        ax2.plot(dens[2], dens[0]*1e-19, label=sequenze[i])
        ax2.set_ylabel("dens")

        elm = ppf.ppfdata(pulse_s, 'JST', 'XIBA',seq=sequenze[i], uid=user_s)
        ax3.plot(elm[2], elm[0]*1e12, label=sequenze[i])
        ax3.set_ylabel("ELMs")

    plt.show(block=False)

loop=input("Vuoi effettuare shift?(y/n): ")
while loop =='y':
    risp=[]
    shift_t=float(input("Inserisci lo shift nel tempo (s):  "))
    risp.append(shift_t)
    shift_wmhd=float(input("Inserisci lo shift verticale di wmhd (udm del grafico):  "))
    risp.append(shift_wmhd)
    shift_dens=float(input("Inserisci lo shift verticale di dens (udm del grafico):  "))
    risp.append(shift_wmhd)   
    shift_elm=float(input("Inserisci lo shift verticale di elm (udm del grafico):  "))
    risp.append(shift_elm)

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
    ax2.set_ylabel("dens ")

    #elm
    elm = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[0]
    elm_t = ppf.ppfdata(pulse, 'EDG7', 'BE2H', uid=user)[2]

    ax3.plot(elm_t,elm)
    ax3.set_xlim(tmin,tmax)
    ax3.set_ylabel("elm")
    ax3.set_ylim(0,1e13)

    
    if num_seq ==1:

        wmhd = ppf.ppfdata(pulse_s, 'JST', 'WTH',seq=sequenza, uid=user_s)
        ax1.plot(wmhd[2]+shift_t, wmhd[0]+shift_wmhd, label=sequenza)
        ax1.legend()
        
        dens = ppf.ppfdata(pulse_s, 'JST', 'NEAV',seq=sequenza, uid=user_s)
        ax2.plot(dens[2]+shift_t, dens[0]*1e-19+shift_dens)

        elm = ppf.ppfdata(pulse_s, 'JST', 'XIBA',seq=sequenza, uid=user_s)
        ax3.plot(elm[2]+shift_t, elm[0]*1e13+shift_elm)

        plt.show(block=False)

    else:

        for i in range(num_seq):
            wmhd = ppf.ppfdata(pulse_s, 'JST', 'WTH',seq=sequenze[i], uid=user_s)
            ax1.plot(wmhd[2]+shift_t, wmhd[0]+shift_wmhd, label=sequenze[i] )
            ax1.set_ylabel("wmhd")
            ax1.legend()

            dens = ppf.ppfdata(pulse_s, 'JST', 'NEAV',seq=sequenze[i], uid=user_s)

            ax2.plot(dens[2]+shift_t, dens[0]*1e-19+shift_dens, label=sequenze[i])
            ax2.set_ylabel("dens")

            elm = ppf.ppfdata(pulse_s, 'JST', 'XIBA',seq=sequenze[i], uid=user_s)
            ax3.plot(elm[2]+shift_t, elm[0]*1e12+shift_elm, label=sequenze[i])
            ax3.set_ylabel("ELMs")

        plt.show(block=False)
    loop=input("Vuoi shiftare nuovamente?(y/n): ")
else:
    print('fine')