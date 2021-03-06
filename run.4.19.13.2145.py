import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import pyfits
import sys

try:
    runs
except NameError:
    runs = 1000

try:
    date
except NameError:
    date = '4.19.13'

try:
    maxmuratio
except NameError:
    maxmuratio = 0.2

try:
    nwalkers
except NameError:
    nwalkers = 10

try:
    maxtime
except NameError:
    maxtime = 100

try:
    tau0
except NameError:
    tau0 = -23

def calc_chi_squared(obs,exp,var,nozero=True):
    if ((len(obs) != len(exp)) | (len(obs) != len(var))): sys.exit("Inputs to calc_chi_squared must have same length: %i,%i,%i,%i"%(len(obs),len(exp),len(x_grid),len(var)))
    if nozero:
        gcs = np.where((var > 0) & (obs != 0) & (exp != 0))
    else:
        gcs = np.where((var > 0))
    gcs = gcs[0]
    if len(gcs) == 0: sys.exit("Calc_chi_squared failure: var is zero everywhere")
    chi_sq = np.sum((obs[gcs]-exp[gcs])*(obs[gcs]-exp[gcs])/var[gcs])
    return chi_sq

#FILE = open('/home/rumbaugh/BDemceetest.3.5.13.txt','w')

def delaylnprob(x,A,B,A_err,B_err,ltime,maxoffset,tau0,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1,2,3] = mu1,2,3 for the 3 seasons of data
    muoutrange = False
    #for im in range(0,3):
    #    if np.fabs(x[im+1]/mu_init_dict[im+1][idelay]-1) > maxmuratio: muoutrange = True
    if ((x[0] > tau0+maxtime) | (x[0] < tau0-maxtime)):
        #print x[0],x[1],np.log(0.00001)
        return -9999999999.
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],0.0,-9999999999.))
    elif muoutrange:
        return -9999999999.
    else:
        if x[0] < 0:
            gltime = np.where((ltime < ltime.max()-0.5*(maxoffset+x[0])) & (ltime > 0.5*(maxoffset-x[0])))
        else:
            gltime = np.where((ltime > 0.5*(maxoffset+x[0])) & (ltime < ltime.max()-0.5*(maxoffset-x[0])))
        gltime = gltime[0]
        if len(gltime) != int(maxtrials):
            if len(gltime) == int(maxtrials) + 1:
                gltime = gltime[1:]
            elif len(gltime) == int(maxtrials) - 1:
                gltime = np.append(gltime,gltime[len(gltime)-1]+1)
            elif len(gltime) == int(maxtrials) - 2:
                gltime = np.append(np.array([gltime[0]-1]),np.append(gltime,gltime[len(gltime)-1]+1))
            else:
                sys.exit("maxtrials didn't work\n%f, %f, %f,%i,%f,%f"%(x[0],ltime.max()-0.5*(maxoffset-x[0]),0.5*(maxoffset+x[0]),len(gltime),maxtrials,tau0))
        Btmp,Berrtmp = B.copy(),B_err.copy()
        Btmp *= x[1]
        Berrtmp *= x[1]
        smB,smB_var = sm.boxcar(ltime+x[0],Btmp,ltime[gltime],smooth_param,y_var=Berrtmp*Berrtmp)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = len(ltime)-x[0]
        #print x[0],x[1],Neff,-1.*(chisq_tmp/Neff)
        #FILE.write('%f %f %f %f\n'%(x[0],x[1],Neff,-1.*(chisq_tmp/Neff)))
        return -1.*(chisq_tmp)

FILE = open('/home/rumbaugh/time_delay_files/testcurvesoutput.4.9.13.dat','w')
FILE.write('#tau mu mu0 chisq Neff\n')
for i in range(0,1):
    hdulist = pyfits.open('/home/rumbaugh/time_delay_files/tdc0_rung0_pair%i.fits'%(i+1))
    hdutab = hdulist[1].data
    ltime,Aflux,Bflux,Aerr,Berr = hdutab['time'],hdutab['lc_A'],hdutab['lc_B'],hdutab['err_A'],hdutab['err_B']
    ltime,Aflux,Bflux,Aerr,Berr = ltime[0],Aflux[0],Bflux[0],Aerr[0],Berr[0]
season1len,season2len = int(len(ltime))/3,int(len(ltime))/3
season3len = len(ltime)-season1len-season2len

mu1_init,mu2_init,mu3_init = 0.,0.,0.
fluxes_dict = {'A': {0: Aflux, 1: Aflux[0:season1len], 2: Aflux[season1len:season1len+season2len], 3: Aflux[season1len+season2len:]}, 'B': {0: Bflux, 1: Bflux[0:season1len], 2: Bflux[season1len:season1len+season2len], 3: Bflux[season1len+season2len:]}, 1: {0: Aflux, 1: Aflux[0:season1len], 2: Aflux[season1len:season1len+season2len], 3: Aflux[season1len+season2len:]}, 0: {0: Bflux, 1: Bflux[0:season1len], 2: Bflux[season1len:season1len+season2len], 3: Bflux[season1len+season2len:]}}
errs_dict = {'A': {0: Aerr, 1: Aerr[0:season1len], 2: Aerr[season1len:season1len+season2len], 3: Aerr[season1len+season2len:]}, 'B': {0: Berr, 1: Berr[0:season1len], 2: Berr[season1len:season1len+season2len], 3: Berr[season1len+season2len:]}, 1: {0: Aerr, 1: Aerr[0:season1len], 2: Aerr[season1len:season1len+season2len], 3: Aerr[season1len+season2len:]}, 0: {0: Berr, 1: Berr[0:season1len], 2: Berr[season1len:season1len+season2len], 3: Berr[season1len+season2len:]}}
ltime_dict = {'rel': {0: ltime, 1: ltime[0:season1len], 2: ltime[season1len:season1len+season2len], 3: ltime[season1len+season2len:]}}
mu_init_dict = {1: mu1_init,2: mu2_init,3: mu3_init}
tau_init = tau0

for i in range(0,3):
    #gacd,gb = np.where(ltime_dict['rel'][j+1]-ltime_dict['rel'][j+1][0] > tau_init[i]),np.where(ltime_dict['rel'][j+1] < ltime_dict['rel'][j+1][len(ltime_dict['rel'][j+1])-1] - tau_init[i])
    #gacd,gb = gacd[0],gb[0]
    mean_b_tmp,mean_acd_tmp = np.mean(fluxes_dict['B'][i+1]),np.mean(fluxes_dict['A'][i+1])
    mu_init_dict[i] = mean_acd_tmp/mean_b_tmp
mu_init = np.mean(Aflux)/np.mean(Bflux)

for i in range(0,1):
    ndim = 2
    p0 = np.zeros((nwalkers,ndim))
    p0[:,0],p0[:,1] = np.ones(nwalkers)*tau_init+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*mu_init+np.random.normal(scale=0.01,size=nwalkers)
    maxoffset = np.fabs(tau_init)+maxtime
    maxtrials = len(ltime)-maxoffset
    if i != 0: sampler.reset()
    sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Aflux,Bflux,Aerr,Berr,ltime,maxoffset,tau0])
    #pos,prob,state=sampler.run_mcmc(p0,runs)
    pos,prob,state=sampler.run_mcmc(p0,100)
    sampler.reset()
    pos,prob,state=sampler.run_mcmc(pos,runs)
    tau_sort = np.sort(sampler.flatchain[:,0])
    print 'BA delay tau range: %f,%f,%f'%(np.median(tau_sort),tau_sort[int(0.16*len(tau_sort))],tau_sort[int(0.84*len(tau_sort))])
    py.hist(sampler.flatchain[:,0])
    py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_hist_tau.BA_delay.%s.ps'%(date))
    py.close()
    py.plot(sampler.flatchain[:,1])
    py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_chain_plot_mu.BA_delay.%s.ps'%(date))
    py.close()
    py.plot(sampler.flatchain[:,0])
    py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_chain_plot_tau.BA_delay.%s.ps'%(date))
    py.close()
    for j in range(0,nwalkers):
        py.plot(sampler.chain[j,:,0])
        py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_all_chain_plot_tau.BA_delay.%s.ps'%(date))
    py.close()
    for k in range(1,2):
        for j in range(0,nwalkers):
            py.plot(sampler.chain[j,:,k])
            py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_all_chain_plot_mu%i.BA_delay.%s.ps'%(k,date))
        py.close()
    py.scatter(sampler.flatchain[:,0],sampler.flatlnprobability)
    py.savefig('/home/rumbaugh/time_delay_files/test/emcee_test/testcurve.emcee_output_tau-prob_scatter.BA_delay.%s.ps'%(date))
    py.close()
    #for j in range(0,len(sampler.flatchain[:,0])): FILE.write('%f %f %f\n'%(sampler.flatchain[j,0],sampler.flatchain[j,1],sampler.flatlnprobability[j]))
    #sampler.reset()
#FILE.close()
