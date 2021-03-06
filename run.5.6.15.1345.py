import numpy as np
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.6.19.14.dat')

date = '5.6.15'

def reviewresults(pair,ldate='4.20.15',ddate='6.3.14',cbase='/home/rumbaugh/Fermi/TimeBombs/output/',showresults=True,ntrials=10000,testplot=False,errstd=np.sqrt(2)*5,T='ACF'):
    tau,mu = cr[:,0][pair-1],cr[:,1][pair-1]
    sampleFile='%ssample.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    sample_infoFile='%ssample_info.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    levelsFile='%slevels.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    DataFile='/home/rumbaugh/Fermi/data/test/testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(pair,tau,mu,ddate)
    posteriorFile='%sposterior.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,tau,mu,ldate)
    plotfilebase='testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(pair,tau,mu,ldate)
    acorrplot,acorrplot2 = '%s/../plots/Acorr_%s'%(cbase,plotfilebase),'%s/../plots/Acorr_norm_%s'%(cbase,plotfilebase)
    if showresults: ShowResults(sampleFile,sample_infoFile,levelsFile,posteriorFile,DataFile,plotfilebase)
    PPMC(T,posteriorFile,DataFile,ntrials,plotfile='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_%s_testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),plotfile2='/home/rumbaugh/Fermi/TimeBombs/plots/PPMC_%s_Td_vs_tau.testlightcurve_%i.tau_%.2f.mu_%.3f.%s.png'%(T,pair,tau,mu,date),figN=7,testplot=testplot,errstd=errstd)
    figure(10)
    clf()
    crd = np.loadtxt(DataFile)
    times,data = crd[:,0],crd[:,1]
    ts = np.arange(0.1,times[-5]-times[0],0.1)
    acorr = np.zeros(len(ts))
    for t,i in zip(ts,np.arange(len(ts))):
        datashift = np.interp(times,times+t,data,left=0,right=0)
        acorr[i] = np.correlate(data,datashift)*1.#/len(datashift[datashift>0])
    plot(ts,acorr)
    ylabel('Acorr')
    xlabel('Time Delay')
    savefig(acorrplot)
    figure(10)
    clf()
    acorr = np.zeros(len(ts))
    for t,i in zip(ts,np.arange(len(ts))):
        datashift = np.interp(times,times+t,data,left=0,right=0)
        acorr[i] = np.correlate(data,datashift)*1./len(datashift[datashift>0])
    plot(ts,acorr)
    ylabel('Acorr')
    xlabel('Time Delay')
    savefig(acorrplot2)
