import ppf
import numpy as np 
import time  
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt  
from getdat import getdat 
plt.rcParams['lines.linewidth'] = 1.0

pulse = 96745
user='jnv7243'

ppf.ppfgo()
fig, (ax1, ax2, ax3, ax4)=plt.subplots(nrows=4, ncols=1, sharex=True)

num_seq=int(input("Quante sequenze vuoi plottare?(#):  "))

if num_seq ==1:

    sequenza=input("Inserisci la sequenza: ")

    wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenza, uid=user)
    ax1.plot(wmhd[2], wmhd[0], label=sequenza)
    ax1.legend()

    dens = ppf.ppfdata(pulse, 'JST', 'NEAV',seq=sequenza, uid=user)
    ax2.plot(dens[2], dens[0])

    elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=sequenza, uid=user)[0]
    elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=sequenza, uid=user)[2]
    ax3.plot(elm_t, elm)

    tempi=[]
    elms=[]
    count=0
    condition_met = False  # Variabile di controllo

    for index, q in enumerate(elm[5:], start=5):
        if q > 1 and not condition_met:
            count = count + 1
            elms.append(count)
            tempi.append(elm_t[index])
            condition_met = True
        if q > 1 and elm_t[index]-tempi[count-1]>0.005:
            count = count + 1
            elms.append(count)
            tempi.append(elm_t[index])

    coefficients = np.polyfit(tempi, elms, 1)
    m_r = coefficients[0]  
    q_r = coefficients[1]

    ax4.scatter(tempi, elms, label='Dati')

    x_interpolation = np.linspace(min(tempi), max(tempi), 100)
    y_interpolation = m_r * x_interpolation + q_r
    ax4.plot(x_interpolation, y_interpolation, 'r-', label='Retta di interpolazione')
    print(m_r)
    print(q_r)

    plt.show()
else:
    sequenze=[]
    gaps=[]
    for i in range(num_seq):
        elemento=input("Inserisci l'elemento {}: ".format(i+1))
        sequenze.append(elemento)

    for i in range(num_seq):
        wmhd = ppf.ppfdata(pulse, 'JST', 'WTH',seq=sequenze[i], uid=user)
        ax1.plot(wmhd[2], wmhd[0], label=sequenze[i] )
        ax1.set_ylabel("wmhd")
        ax1.legend()

        dens = ppf.ppfdata(pulse, 'JST', 'NEAV',seq=sequenze[i], uid=user)
        ax2.plot(dens[2], dens[0], label=sequenze[i])
        ax2.set_ylabel("dens")
        gap=max(dens[0])-min(dens[0])
        gaps.append(gap)

        elm = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=sequenze[i], uid=user)[0]
        elm_t = ppf.ppfdata(pulse, 'JST', 'XIBA',seq=sequenze[i], uid=user)[2]
        ax3.plot(elm_t, elm)

        tempi=[]
        elms=[]
        count=0
        condition_met = False  # Variabile di controllo

        for index, q in enumerate(elm[5:], start=5):
            if q > 1 and not condition_met:
                count = count + 1
                elms.append(count)
                tempi.append(elm_t[index])
                condition_met = True
            if q > 1 and elm_t[index]-tempi[count-1]>0.005:
                count = count + 1
                elms.append(count)
                tempi.append(elm_t[index])

        coefficients = np.polyfit(tempi, elms, 1)
        m_r = coefficients[0]  
        q_r = coefficients[1]

        ax4.scatter(tempi, elms, label='Dati')

        x_interpolation = np.linspace(min(tempi), max(tempi), 100)
        y_interpolation = m_r * x_interpolation + q_r
        ax4.plot(x_interpolation, y_interpolation, 'r-', label='Retta di interpolazione')
        print(str(sequenze[i]) + "\t" + str(m_r) + "\t" + str(q_r))


    min_value=min(gaps)
    print("Il minimo valore di gap è: " + str(min_value))
    min_index = gaps.index(min_value)
    print("La sequenza corrispondente è la numero: " + str(sequenze[min_index]))

    plt.show()






