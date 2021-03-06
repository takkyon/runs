import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

try:
    ALAG
except NameError:
    ALAG = 31.5
try:
    CLAG
except NameError:
    CLAG = 36.5
try:
    DLAG
except NameError:
    DLAG = 80.5
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
    maxmu = 1.25
try:
    minmu
except NameError:
    minmu = 0.75

execfile("/home/rumbaugh/Load1938.py")
ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err,Anflux,Bnflux,C1nflux,C2nflux,Anerr,Bnerr,C1nerr,C2nerr = Load1938()


st = time.time()
FILEt = open('/home/rumbaugh/tracking.run.1.23.13.1635.txt','w')
FILEt.write('Starting run.1.23.13.1635.py...')
FILEt.close()

ltime = (ltime-ltime[0])
#find time delays
BA_delay_d2,BAmud2,BAdispd2 = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t1 = time.time()
print "33%% Done. Elapsed Time: %f seconds"%(t1-st)
BC1_delay_d2,BC1mud2,BC1dispd2 = calc_disp_delay(C1flux,Bflux,ltime,ltime,C1err,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t2 = time.time()
print "66%% Done. Elapsed Time: %f seconds"%(t2-st)
BC2_delay_d2,BC2mud2,BC2dispd2 = calc_disp_delay(C2flux,Bflux,ltime,ltime,C2err,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_2b',output=2,simplemuerr=True)
t3 = time.time()
if not justone:
#now use D_4_2 with range of deltas
    delta_arr = np.arange(19)+3.5
    BA_delay_d42,BAmud42,BAdispd42,BC1_delay_d42,BC1mud42,BC1dispd42,BC2_delay_d42,BC2mud42,BC2dispd42 = np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr)),np.zeros(len(delta_arr))
    for i in range(0,len(delta_arr)):
        BA_delay_d42[i],BAmud42[i],BAdispd42[i] = calc_disp_delay(Aflux,Bflux,ltime,ltime,Aerr,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)     
        tA = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.1635.txt','a')
        FILEt.write('Finished call to D_4_2b for BA with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAdispd42[i],tA-st,(tA-t3)/(3*i+1)*(3*(len(delta_arr)-i-1))+2))
        FILEt.close()
        BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i] = calc_disp_delay(C1flux,Bflux,ltime,ltime,C1err,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)    
        tC = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.1635.txt','a')
        FILEt.write('Finished call to D_4_2b for BC1 with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i],tC-st,(tC-t3)/(3*i+2)*(3*(len(delta_arr)-i-1))+1))
        FILEt.close()
        BC2_delay_d42[i],BC2mud42[i],BC2dispd42[i] = calc_disp_delay(C2flux,Bflux,ltime,ltime,C2err,Berr,maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta=delta_arr[i],output=2,simplemuerr=True)    
        tD = time.time()
        FILEt = open('/home/rumbaugh/tracking.run.1.23.13.1635.txt','a')
        FILEt.write('Finished call to D_4_2b for BC2 with delta = %4.1f\nOutput: tau = %5.1f  mu = %6.4f disp = %8.6f\nElapsed time - %f seconds. ETA: %f seconds\n'%(delta_arr[i],BC2_delay_d42[i],BC2mud42[i],BC2dispd42[i],tD-st,(tD-t3)/(3*i+3)*(3*(len(delta_arr)-i-1))+0))
        FILEt.close()
print "\n\nB-A:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(BA_delay_d2,BAmud2,BAdispd2)
print "\n\nB-C1:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(BC1_delay_d2,BC1mud2,BC1dispd2)
print "\n\nB-C2:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(BC2_delay_d2,BC2mud2,BC2dispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAdispd42[i])
        #FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BA_delay_d42[i],BAmud42[i],BAdispd42[i]))
if justone: print "\n\nB-C:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f\n"%(BC1_delay_d2,BC1mud2,BC1dispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "D_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i])
        #FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC1_delay_d42[i],BC1mud42[i],BC1dispd42[i]))
if justone: print "\n\nB-D:\nD_2 delay: %4.1f days  mu: %6.4f   disp: %f:"%(BC2_delay_d2,BC2mud2,BC2dispd2)
if not justone:
    for i in range(0,len(delta_arr)): 
        print "_4_2:\ndelta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC2_delay_d42[i],BC2mud42[i],BC2dispd42[i])
        #FILE.write("delta = %4.1f days - delay: %3.0f days  mu: %6.4f   disp: %f"%(delta_arr[i],BC2_delay_d42[i],BC2mud42[i],BC2dispd42[i]))
t3 = time.time()
print "All Done. Elapsed Time: %f seconds"%(t3-st)
FILEt = open('/home/rumbaugh/tracking.run.1.23.13.1635.txt','a')
FILEt.write("All Done. Elapsed Time: %f seconds"%(t3-st))
FILEt.close()
