import numpy as np
import matplotlib
import matplotlib.pylab as pylab
import math as m
try:
    t3013
except NameError:
    t3013 = 300

#5281,1757,1324+3059,1324+3011,1604A,1604B

pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)

names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','RXJ0910+5422','RXJ0910+5419'])
names2 = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])
#ncnts = np.array([670,298,96,212,108,219,69])

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.soft.9.22.11.dat')
lums = get_colvals(crl,'col2')/10.0
lumes = get_colvals(crl,'col3')/10.0

crl = read_file('/home/rumbaugh/paperstuff/clus.lums.bol.9.22.11.dat')
lumbol = get_colvals(crl,'col1')

lumboles = np.zeros(len(lumbol))
for i in range(0,len(lumbol)): lumboles[i] = lumes[i]*lumbol[i]/lums[i]

Temps = np.array([4.95,3.75,3.6,3.71,t3013,3.50,1.64,4.50,2.52])
TerrU = np.array([0.99,1.00,3.5,1.44,10,1.82,0.65,1.07,0.59])
TerrD = np.array([0.74,0.68,1.56,0.94,2.99,1.08,0.45,0.78,0.48])
#sigma = np.array([921,652,880,914,819,619,811,675,1028])
sigma = np.array([1068,893,892,917,677,717,812,776,945])
sigerr = np.array([86,142,129,122,144,133,77,135,190])
#sigerr = np.array([76,123,124,137,242,96,76,190,140])
sigma2 = np.array([921,652,880,914,819,619,811,1028,675])
sigerr2 = np.array([76,123,124,137,242,96,76,140,190])
Temps2 = np.array([4.95,3.75,3.6,3.71,t3013,3.50,1.64,2.52,4.50])
TerrU2 = np.array([0.99,1.00,3.5,1.44,10,1.82,0.65,0.59,1.07])
TerrD2 = np.array([0.74,0.68,1.56,0.94,2.99,1.08,0.45,0.48,0.78])

lineslope = (m.log(1125)-m.log(0.1))/(m.log(20)-m.log(1.333333))
lineb = m.log(1125)-lineslope*m.log(20)
expb = m.exp(lineb)
expb = 3.11/(0.7*0.7)
lineslope = 2.64
lineX = (np.arange(10000)+1)*(10.0/10000)
lineY = expb*(lineX/6.0)**lineslope


pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
pylab.ylim(0.5,7.5)
pylab.loglog(lineX,lineY,lw=2)
pylab.errorbar(Temps, lumbol, xerr=[TerrD,TerrU],yerr=[lumboles,lumboles],fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('T (keV)',fontsize='16')
pylab.ylabel('L$_x$ E(z)$^{-1}$ (10$^{44}$ erg s$^{-1}$)',fontsize='16')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(Temps[i]-1.2,lumbol[i]+0.12,names[i],color='black',weight='extra bold')
    elif i == 1: 
        pylab.text(Temps[i]-0.9,lumbol[i]+0.10,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(Temps[i]+0.1,lumbol[i]+0.005,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(Temps[i]+0.18,lumbol[i]-0.17,names[i],color='black',weight='extra bold')
    elif i == 5:
        pylab.text(Temps[i]-0.85,lumbol[i]-0.2,names[i],color='black',weight='extra bold')
    elif i == 6:
        pylab.text(Temps[i]+0.05,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(Temps[i]-0.95,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    else:
        pylab.text(Temps[i]+0.15,lumbol[i]+0.1,names[i],color='black',weight='extra bold')
pylab.xticks([1],['1'])
pylab.yticks([1],['1'])
pylab.savefig('/home/rumbaugh/LxT.plot.bol.4.10.12.png')
pylab.close('all')

print '\nLx-T\n'
for i in range(0,len(names)):
    distmin = 99999
    Terrt = TerrU[i]
    if ((i == 7) | (i == 2) | (i == 3)): Terrt = TerrD[i]
    for j in range(0,len(lineX)):
        diststemp = m.sqrt(((Temps[i]-lineX[j])/Terrt)**2+((lumbol[i]-lineY[j])/lumboles[i])**2)
        if diststemp < distmin: distmin = diststemp
    print '%s - %f\n'%(names[i],distmin)


lineslope = (m.log(200)-m.log(0.1))/(m.log(1800)-m.log(429))
lineb = m.log(200)-lineslope*m.log(1800)
expb = m.exp(lineb)
expb = 0.01*10**(-13.68)*(7/5.0)**(5.3)
lineslope = 5.30
lineX = (np.arange(10000)+1)/3.0
lineY = expb*lineX**lineslope


pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.ylim(0.5,7.5)
#pylab.xlim(450,1200)
pylab.xlim(468.75,1250)
pylab.loglog(lineX,lineY,lw=2)
pylab.errorbar(sigma, lumbol, xerr=[sigerr,sigerr],yerr=[lumboles,lumboles],fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('$\sigma_v$ (km s$^{-1}$)',fontsize=16)
pylab.ylabel('L$_x$ E(z)$^{-1}$ (10$^{44}$ erg s$^{-1}$)',fontsize=16)
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(sigma[i]-65,lumbol[i]+0.33,names[i],color='black',weight='extra bold')
    elif i == 5: 
        pylab.text(sigma[i]-105,lumbol[i]-0.16,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(sigma[i]+20,lumbol[i]-0.14,names[i],color='black',weight='extra bold')
    elif i == 4:
        pylab.text(sigma[i]-74,lumbol[i]+0.15,names[i],color='black',weight='extra bold')
    elif i == 6:
        pylab.text(sigma[i]-105,lumbol[i]+0.022,names[i],color='black',weight='extra bold')
    elif i == 7:
        pylab.text(sigma[i]-175,lumbol[i]+0.05,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(sigma[i]+20,lumbol[i]-0.19,names[i],color='black',weight='extra bold')
    else:
        pylab.text(sigma[i]+10,lumbol[i]+0.05,names[i],color='black',weight='extra bold')
pylab.xticks([1000],['1000'])
pylab.yticks([1],['1'])
pylab.savefig('/home/rumbaugh/sigLx.plot.4.11.12.png')
pylab.close('all')
print '\nsig-Lx\n'
for i in range(0,len(names)):
    distmin = 99999
    for j in range(0,len(lineX)):
        diststemp = m.sqrt(((lumbol[i]-lineY[j])/lumboles[i])**2+((sigma[i]-lineX[j])/sigerr[i])**2)
        if diststemp < distmin: distmin = diststemp
    print '%s - %f\n'%(names[i],distmin)

lineslope = (m.log(2146)-m.log(308))/(m.log(20))
lineb = m.log(308)
expb = 308.0
expb = 10**2.49
lineslope=0.65
lineX = (np.arange(10000)+5)*(10.0/10000)
lineY = expb*lineX**lineslope

pylab.rc('axes',linewidth=2)
pylab.fontsize = 14
pylab.tick_params(which='major',length=8,width=2,labelsize=14)
pylab.tick_params(which='minor',length=4,width=1.5,labelsize=14)
pylab.xlim(1,8)
#pylab.ylim(450,1200)
pylab.ylim(468.75,1250)
pylab.loglog(lineX,lineY,lw=2)
pylab.errorbar(Temps, sigma, xerr=[TerrD,TerrU], yerr=[sigerr,sigerr], fmt='ro',lw=2,capsize=5,mew=2)
pylab.xlabel('T (keV)',fontsize='16')
pylab.ylabel('$\sigma_v$ (km s$^{-1}$)',fontsize='16')
for i in range(0,len(Temps)): 
    if i == 0: 
        pylab.text(Temps[i]-0.565,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 2:
        pylab.text(Temps[i]-1.35,sigma[i]-30,names[i],color='black',weight='extra bold')
    elif i == 3:
        pylab.text(Temps[i]+0.09,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 7:
        pylab.text(Temps[i]+0.05,sigma[i]+10,names[i],color='black',weight='extra bold')
    elif i == 8:
        pylab.text(Temps[i]-0.95,sigma[i]+13,names[i],color='black',weight='extra bold')
    elif i == 5:
        pylab.text(Temps[i]-0.92,sigma[i]-23,names[i],color='black',weight='extra bold')
    elif i == 1:
        pylab.text(Temps[i]+0.09,sigma[i]-30,names[i],color='black',weight='extra bold')
    else:
        pylab.text(Temps[i]+0.05,sigma[i]+10,names[i],color='black',weight='extra bold')
pylab.yticks([1000],['1000'])
pylab.xticks([1],['1'])
pylab.savefig('/home/rumbaugh/sigT.plot.4.11.12.png')
pylab.close('all')

print '\nsig-T\n'
for i in range(0,len(names)):
    distmin = 99999
    Terrt = TerrU[i]
    if i == 7: Terrt = TerrD[i]
    for j in range(0,len(lineX)):
        diststemp = m.sqrt(((Temps[i]-lineX[j])/Terrt)**2+((sigma[i]-lineY[j])/sigerr[i])**2)
        if diststemp < distmin: distmin = diststemp
    print '%s - %f\n'%(names[i],distmin)
