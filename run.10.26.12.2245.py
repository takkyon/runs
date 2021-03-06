import numpy as np
import math as m
import arrconv
from crates_contrib.utils import *

try:
    rewrite
except NameError:
    rewrite = False

ymax = np.array([0.35,0.25,0.1,0.16,0.09,0.06,0.12,0.5,0.35])

anninner = np.array([120,100,160,100,160,150,100,100,100])*0.5
ai = arrconv.float2int(anninner/2.5-1)
names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
crb = np.loadtxt('/home/rumbaugh/DE_counts.bkg_data.10.13.12.dat',dtype='string')
bgcnts = arrconv.str2float(crb[:,1])
bgSBas = arrconv.str2float(crb[:,3])
bgann1,bgann2 = arrconv.str2float(crb[:,6]),arrconv.str2float(crb[:,7])
bgSBas_err = np.zeros(len(bgSBas))

sigma = np.array([921,652,880,914,819,619,811,675,1028])
crc = np.loadtxt("/home/rumbaugh/cc_out.6.29.12.nh.dat")
mpc = crc[:,11]*0.7
Hz = crc[:,4]*0.7

#FILEfit = open('/home/rumbaugh/SBfits.10.26.12.dat','w')

for i in range(0,len(bgSBas)): 
    if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
        bgSBas_err[i] = m.sqrt(bgcnts[i])/(m.pi*(bgann2[i]**2-bgann1[i]**2))
    else:
        bgSBas_err[i] = m.sqrt(bgcnts[i])/(m.pi*(bgann2[i-1]**2-bgann1[i-1]**2))
for i in range(0,len(names)):
    r0 = 0.18*(mpc[i]*60)
    r500 = (mpc[i]*60)*2*sigma[i]/(m.sqrt(500)*Hz[i])
    print names[i], r0
    cr = np.loadtxt('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arr = cr[:,2]
    C = cnts_arr[ai[i]]
    NC = C-bgSBas[i]*m.pi*anninner[i]**2
    NCerr = m.sqrt(C+bgSBas_err[i]**2*m.pi**2*anninner[i]**2)
    cum_cnts = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = sum(cnts_arr[0:j])
    SB_arr = cr[:,4]
    SB_err_arr = cr[:,6]
    ann_arr = cr[:,1]
    #if ((i == 0) | (i == 1) | (i == 2) | (i == 3) | (i == 6) | (i == 7) | (i == 8)):
    if i >= -77:
        ann_step = 10
        ann_arr = np.arange(12)*10+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    #elif ((i == 4)):
    elif ((i == 44)):
        ann_step = 10
        ann_arr = np.arange(12)*10+10
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    else:
        ann_step = 1
        ann_arr = np.arange(8)*15+15
        cnts_arrt = np.copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = np.zeros(len(ann_arr)),np.zeros(len(ann_arr)),np.zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[6*j+5]
    cum_ncnts = np.zeros(len(cnts_arr))
    cum_ncnts_err = np.zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): 
        cum_ncnts[j] = cnts_arr[j]-bgSBas[i]*m.pi*ann_arr[j]**2
        cum_ncnts_err[j] = m.sqrt(cum_cnts[j]+m.pi*m.pi*ann_arr[j]**4*bgSBas_err[i]**2)
    area_arr = np.zeros(len(ann_arr))
    area_arr[0] = m.pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = m.pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = np.append(np.zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (m.sqrt(cnts_arr[j])+m.sqrt(cnts2[j]))/area_arr[j]
    bkginit = np.average(SB_arr[len(SB_arr)-3:len(SB_arr)])
    ann_temp,SB_temp,SB_err_temp = np.copy(ann_arr)-0.5*ann_step,np.copy(SB_arr),np.copy(SB_err_arr)
    if names[i] == 'Cl1324+3013': ann_temp,SB_temp,SB_err_temp = ann_arr[0:8],SB_arr[0:8],SB_err_arr[0:8]
    write_columns("temp.SB_fitting.%s.10.26.12.fits"%names[i],ann_temp,SB_temp,SB_err_temp,colnames=["ann","SB","SB_err"],format="fits")
    load_data(1,"temp.SB_fitting.%s.10.26.12.fits"%names[i], 3,['ann','SB','SB_err'])
    set_source("beta1d.b1d+const1d.bkg")
    b1d.beta = 2.0/3
    freeze(b1d.beta)
    bkg.c0 = bgSBas[i]
    b1d.r0 = r0
    b1d.ampl = (NC/(2*m.pi*b1d.r0**2))/(1.0-1.0/(1+anninner[i]**2*b1d.r0**(-2))**0.5)
    set_stat("chi2gehrels")
    fit()
    print '\n%s'%(names[i])
    projection()
    print '\n'
    #FILEfit.write('%13s %f %f  %f %f %f %f\n'%(names[i],NC,NCerr,r500cnts_nofit,r500cntserr_nofit,tcnts_nofit,tcntserr_nofit))
    #print '%12s:\n2-par, fix. bkg: A: %f %f +%f r0: %f %f +%f NCcnt: %f NC: %f\n2-par, fc2: r0: %f %f +%f\ntcnts 1par: %f 2par, fix. bkg: %f 2par, fc2: %f\n step: %4.1f r0: %f bkginit: %f bgSB: %f\n'%(names[i],Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,NCcnts,NC,bkgfit4par,bkgerr4parl,bkgerr4paru,r0fit3,r0fit3errl,r0fit3erru,tcnts1,tcnts2,tcnts4,ann_step,r0,bkginit,bgSBas[i])


 
