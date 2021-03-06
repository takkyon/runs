import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile('/home/rumbaugh/LoadEVLA_2011.py')
execfile('/home/rumbaugh/LoadVLA_2001.py')
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

date = '6.15.14'

try:
    justone
except NameError:
    justone = False
try:
    timestep
except NameError:
    timestep = 0.5
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

for source in ['B0712']:
    crS = LoadEVLA_2011(source,normalize=True)
    crS['day'] -= crS['day'][0]
    ltime = crS['day']
    rms = crS['rms']
    fluxratio_err = 0.0043
    if source == 'B1938':
        fluxratio_err = 0.0048
        imgnames = ['fluxC1','fluxC2','fluxB','fluxA']
    if source == 'B0712':
        imgnames = ['fluxA','fluxB','fluxC','fluxD']
    errnames = np.copy(imgnames)
    for n in np.arange(0,len(errnames)): errnames[n] = 'err%s'%errnames[n][4:]
    fluxA1 = crS[imgnames[0]]
    A1err = crS[errnames[0]]
    fluxA2 = crS[imgnames[1]]
    A2err = crS[errnames[1]]
    fluxA = fluxA1+fluxA2
    Aerr = np.sqrt(A1err**2+A2err**2)
    fluxB = crS[imgnames[2]]
    Berr = crS[errnames[2]]
    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]
    
    if source == 'B0712':
        days,flux_arr,flux_err_arr = LoadVLA_2001(lens='0712')
        tfluxA1,tfluxA2,tfluxB = flux_arr[0],flux_arr[1],flux_arr[2]
        tAerr1,tAerr2,tBerr = flux_err_arr[0],flux_err_arr[1],flux_err_arr[2]
        gB = np.arange(len(days))[:-9]
        ltime = np.append(days,ltime+1000)
        mtemp = np.mean(fluxB[g])/np.mean(tfluxB[gB])
        fluxA,fluxB = np.append((tfluxA1+tfluxA2)*mtemp,fluxA),np.append(tfluxB*mtemp,fluxB)
        Aerr,Berr = np.append(np.sqrt(tAerr1**2+tAerr2**2)*mtemp,Aerr),np.append(tBerr*mtemp,Berr)
    

    g = np.where((fluxA > 0)&(fluxB>0)&(Aerr > 0)&(Berr>0))[0]


#find time delays
    dispmatrixAB = calc_disp_delay(fluxB[g],fluxA[g],ltime[g],ltime[g],Berr[g],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=True,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_2.%s.dat'%(source,date))
    tauAB,muAB,dispAB = calc_disp_delay(fluxB[g],fluxA[g],ltime[g],ltime[g],Berr[g],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_2',output=2,dispmatrix=False,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_2.%s.dat'%(source,date),verbose=False)
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    BA_delay_d42,BAmud42,BAdispd42,BC_delay_d42,BCmud42,BCdispd42,BD_delay_d42,BDmud42,BDdispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    print '%s:\n\nD_2 - %f\n\nD_4_2\n'%(source,tauAB)
    for i in range(0,len(delta_arr)):
        BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(fluxB[g],fluxA[g],ltime[g],ltime[g],Berr[g],Aerr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2',delta=delta_arr[i],output=2,outfile='/mnt/data2/rumbaugh/EVLA/11A-138/disp_results/disp_out.%s.D_4_2.delta_%.1f.%s.dat'%(source,delta_arr[i],date),verbose=False)
        print '%.1f - tau: %5.1f  mu: %f\n'%(delta_arr[i],BA_delay_d42[i],BAmud42[i])
    print 'Medians- tau: %5.1f  mu: %f\n'%(np.median(BA_delay_d42),np.median(BAmud42))

