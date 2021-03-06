import numpy as np
import matplotlib.pyplot as py
import emcee
import smoothing_1d as sm
import math as m
execfile("/home/rumbaugh/arrconv.py")

Load1938 = np.loadtxt('/home/rumbaugh/B1938+666_files/B1938+666_reduced_fluxes.3.1.13.dat')


ltime,Aflux,Bflux,C1flux,C2flux,Aerr,Berr,C1err,C2err = Load1938[:,0],Load1938[:,1],Load1938[:,2],Load1938[:,3],Load1938[:,4],Load1938[:,5],Load1938[:,6],Load1938[:,7],Load1938[:,8]
ltime /= 86400
Cflux = C1flux+C2flux
Cerr = np.zeros(len(Cflux))
for i in range(0,len(Cerr)): Cerr[i] = m.sqrt((C1err[i])**2+(C2err[i])**2)


try:
    runs
except NameError:
    runs = 1000

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

def delaylnprob(x,A,B,A_err,B_err,ltime,maxtime=60,mintime=0,t_grid_spacing=0.5,smooth_param=10.):
    #x is a vector with x[0] = tau and x[1] = mu
    if mintime == None: mintime = -1*maxtime
    if ((x[0] > maxtime) | (x[0] < mintime)):
        #print x[0],x[1],np.log(0.00001)
        return -99999999.
    else:
        grid_spaces = int((np.max(ltime)-np.min(ltime)-np.abs(x[0]))/t_grid_spacing)+2
        t_grid = (np.arange(grid_spaces)-1)*t_grid_spacing
        if x[0] > 0: t_grid += x[0]
        if x[0] < 0:
            gltime = np.where(ltime < ltime.max()-x[0])
        else:
            gltime = np.where(ltime > x[0])
        gltime = gltime[0]
        smB,smB_var = sm.boxcar(ltime+x[0],B*x[1],ltime[gltime],smooth_param,y_var=x[1]*x[1]*B_err*B_err)
        chisq_tmp = calc_chi_squared(smB,A[gltime],A_err[gltime]*A_err[gltime]+smB_var)
        Neff = (ltime[len(ltime)-1]-np.abs(x[0]))/3.7
        #print x[0],x[1],Neff,-1.*(chisq_tmp/Neff)
        return -1.*(chisq_tmp/Neff)

#load1608 = np.loadtxt('/home/rumbaugh/B1938+666_files/1608_g.ab922_nh')
#ltime = load1608[:,0].copy()
#Aflux,Bflux,Cflux,Dflux,Aerr,Berr,Cerr,Derr = load1608[:,1].copy(),load1608[:,2].copy(),load1608[:,3].copy(),load1608[:,4].copy(),load1608[:,5].copy(),load1608[:,6].copy(),load1608[:,7].copy(),load1608[:,8].copy()

ndim,nwalkers = 2,10
ltime -= ltime[0]
p0 = np.zeros((nwalkers,ndim))
p0[:,0],p0[:,1] = np.ones(nwalkers)*45.5+np.random.normal(scale=0.1,size=nwalkers),np.ones(nwalkers)*1.03083+np.random.normal(scale=0.01,size=nwalkers)
sampler = emcee.EnsembleSampler(nwalkers,ndim,delaylnprob,args=[Cflux,Bflux,Cerr,Berr,ltime])
pos,prob,state = sampler.run_mcmc(p0,100)
sampler.reset()
sampler.run_mcmc(pos,runs)
py.scatter(sampler.flatchain[:,0],sampler.flatchain[:,1])
py.savefig('/home/rumbaugh/B1938+666_files/B1938.emcee_output_2D.BC_delay.3.5.13.ps')
py.close()
tau_sort = np.sort(sampler.flatchain[:,0])
print 'BC delay tau range: %f,%f'%(tau_sort[1600],tau_sort[8400])
py.hist(sampler.flatchain[:,0])
py.savefig('/home/rumbaugh/B1938+666_files/B1938.emcee_output_hist_tau.BC_delay.3.5.13.ps')
py.close()
py.plot(sampler.flatchain[:,0])
py.savefig('/home/rumbaugh/B1938+666_files/B1938.emcee_output_chain_plot_tau.BC_delay.3.5.13.ps')
py.close()
