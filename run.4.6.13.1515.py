import numpy as np
import pyfits
import time
import matplotlib
import matplotlib.pyplot as py

try:
    date
except NameError:
    date = '4.6.13'

try:
    maxtime
except NameError:
    maxtime = 1825
try:
    timestep
except NameError:
    timestep = 1.
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9
try:
    mustep
except NameError:
    mustep = 0.001


def calc_chi_squared(obs,exp,var,nozero=True):
    if ((len(obs) != len(exp)) | (len(obs) != len(var))): sys.exit("Inputs to calc_chi_squared must have same length: %i,%i,%i,%i"%(len(obs),len(exp),len(x_grid),len(var)))
    if nozero:
        gcs = np.where((var > 0) & (obs != 0) & (var != 0))
    else:
        gcs = np.where((var > 0))
    gcs = gcs[0]
    if len(gcs) == 0: sys.exit("Calc_chi_squared failure: var is zero everywhere")
    chi_sq = np.sum((obs[gcs]-exp[gcs])*(obs[gcs]-exp[gcs])/var[gcs])
    return chi_sq

def chi_squared_min_delays(A,B,A_t,A_err,B_err,maxtime,timestep,minmu,maxmu,mustep,output=3,chisqarray=False,chisqmatrix=False,use_overlap_mean=False):
    disparrout,disparrmu,disparrtime = np.zeros(0),np.zeros(0),np.zeros(0)
    mu0 = np.mean(A)*1.0/np.mean(B)
    #if use_overlap_mean:
    #    galag,gblag = np.where((A_t > np.min(B_t)+ALAG) & (A_t < np.max(B_t) + ALAG)),np.where((B_t + ALAG > np.min(A_t)) & (B_t + ALAG < np.max(A_t)))
    #    galag,gblag = galag[0],gblag[0]
    #    mu0 = np.mean(A[galag])/np.mean(B[gblag])
    min_chisq,tau_out,mu_out = -99,0.,0.
    tau = -1.*maxtime
    st = time.time()
    tausteps = (2*maxtime/timestep+1)
    totalsteps = tausteps*((maxmu-minmu)/mustep+1)
    while tau <= maxtime:
        B_t = A_t+tau
        gBt = np.where((B_t <= np.max(A_t)) & (B_t >= np.min(A_t)))
        gAt = np.where((A_t <= np.max(B_t)) & (A_t >= np.min(B_t)))
        gAt,gBt = gAt[0],gBt[0]
        mu = minmu*mu0
        min_chisq2,mu2 = -99,0.
        disparrtmp = np.zeros(0)
        while mu <= maxmu*mu0:
            chisq_tmp = calc_chi_squared(mu*B[gBt],A[gAt],A_err[gAt]*A_err[gAt]+mu*mu*B_err[gBt]*B_err[gBt])
            gneff = np.where(A[gAt]*B[gBt] > 0)
            gneff = gneff[0]
            Neff = len(gneff)
            chisq_tmp /= Neff
            if ((chisq_tmp < min_chisq) | (min_chisq == -99)):
                min_chisq,tau_out,mu_out = chisq_tmp,tau,mu
            if ((chisq_tmp < min_chisq2) | (min_chisq2 == -99)):
                min_chisq2,mu2 = chisq_tmp,mu
            disparrtmp = np.append(disparrtmp,chisq_tmp)
            if ((mu < (minmu+0.9*mustep)*mu0) & (tau < 0.9*timestep-maxtime)):
                t1 = time.time()
                print '\nOne Trial Complete\nElapsed Time: %f seconds\nETA: %f seconds\n'%(t1-st,(t1-st)*(totalsteps-1))
            elif ((tau < 0.9*timestep-maxtime) & (mu < (minmu+4.9*mustep)*mu0) & (mu > (minmu+3.9*mustep)*mu0)):
                t2 = time.time()
                print '\nFive Trials Complete\nElapsed Time: %f seconds\nETA: %f seconds\n'%(t2-st,0.2*(t2-st)*(totalsteps-5))
            mu += mustep*mu0
        if tau == -1*maxtime:
            dispmatrixout = np.array([disparrtmp])
        else:
            dispmatrixout = np.append(dispmatrixout,np.array([disparrtmp]),axis=0)
        #disparrout,disparrmu,disparrtime = np.append(disparrout,min_chisq2),np.append(disparrmu,mu2),np.append(disparrtime,tau)
        if ((tau > -0.5*maxtime) & (tau < timestep-0.5*maxtime)):
            t3 = time.time()
            print '\n25%% Complete\nElapsed Time: %f seconds\nETA: %f seconds\n'%(t3-st,3*(t3-st))
        if ((tau > 0) & (tau < 1.1*timestep)):
            t4 = time.time()
            print '\n50%% Complete\nElapsed Time: %f seconds\nETA: %f seconds\n'%(t4-st,(t4-st))
        if ((tau > 0.5*maxtime) & (tau < timestep+0.5*maxtime)):
            t5 = time.time()
            print '\n75%% Complete\nElapsed Time: %f seconds\nETA: %f seconds\n'%(t5-st,(t5-st)/3.)
        tau += timestep
    tdone = time.time()
    print '\nAll Done! Elapsed time: %f seconds\n'%(tdone-st)
    if chisqmatrix:
        if output == 4:
            gneff = np.where(A[gAt]*B[gBt] > 0)
            gneff = gneff[0]
            Neff = len(gneff)
            return dispmatrixout,tau_out,mu_out,min_chisq,Neff
        elif output == 5:
            gneff = np.where(A[gAt]*B[gBt] > 0)
            gneff = gneff[0]
            Neff = len(gneff)
            return dispmatrixout,tau_out,mu_out,min_chisq,Neff,mu0
        else:
            return dispmatrixout
    elif chisqarray:
        return disparrout,disparrmu,disparrtime
    elif output == 1:
        return tau_out,mu_out
    elif output == 2:
        return tau_out,mu_out,min_chisq
    else:
        gneff = np.where(A[gAt]*B[gBt] > 0)
        gneff = gneff[0]
        Neff = len(gneff)
        return tau_out,mu_out,min_chisq,Neff

for i in range(0,8):
    hdulist = pyfits.open('/home/rumbaugh/time_delay_files/tdc0_rung0_pair%i.fits'%(i+1))
    hdutab = hdulist[1].data
    ltime,A,B,A_err,B_err = hdutab['time'],hdutab['lc_A'],hdutab['lc_B'],hdutab['err_A'],hdutab['err_B']
    ltime,A,B,A_err,B_err = ltime[0],A[0],B[0],A_err[0],B_err[0]
    chisqmat,tau,mu,chisq,Neff,mu0 = chi_squared_min_delays(A,B,ltime,A_err,B_err,maxtime,timestep,minmu,maxmu,mustep,output=5,chisqmatrix=True)
    print tau,mu,chisq,Neff
    py.imshow(chisqmat/Neff,extent=[minmu,maxmu,-1*maxtime,maxtime],aspect='auto',origin='lower')
    py.savefig('/home/rumbaugh/time_delay_files/test/chisq_plot.%s.run%i.ps'%(date,i+1))
    py.close()
