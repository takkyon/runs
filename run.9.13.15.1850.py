import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/ReverseSigmaClip.py')
execfile('/home/rumbaugh/git/TimeBombs/showresults.py')
execfile('/home/rumbaugh/git/TimeBombs/PosteriorPredictiveModelChecking.py')

execfile('/home/rumbaugh/git/triangle.py/triangle_mod.py')

cbase='/home/rumbaugh/Fermi/TimeBombs/output/'

critwidth=3.716/2.35482

date='9.13.15'
ldate='9.10.15'

errstd = 7.5
cr = np.loadtxt('/home/rumbaugh/Fermi/data/test/testlightcurve_truthvalues.8.19.15.dat')
taus,mus=cr[:,0],cr[:,1]

pairs=np.arange(30)

for i,pair in zip((pairs-1,pairs)):
    avg_fwidth,medtau,cliptau=np.zeros(100),np.zeros(100),np.zeros(100)
    medmu=np.zeros(100)
    mean_amp,mean_skew,mean_Tfl=np.zeros(100),np.zeros(100),np.zeros(100)
    mean_pamp,mean_pskew,mean_pfwidth=np.zeros(100),np.zeros(100),np.zeros(100)
    mean_pnflares,true_nflares=np.zeros(100),np.zeros(100)
    mean_hamps,mean_hwidths,mean_hcenskew,mean_hHWskew=np.zeros(100),np.zeros(100),np.zeros(100),np.zeros(100)
    tau,mu=taus[i],mus[i]
    for jiter in range(0,10):
        posteriorFile='%sposterior.testlightcurve_%i.iter_%i.tau_%.2f.mu_%.3f.%s.dat'%(cbase,pair,jiter,tau,mu,ldate)
        crpost_tmp = np.loadtxt(posteriorFile)
        if j==0:
            crpost=np.copy(crpost_tmp)
        else:
            crpost=np.append(crpost,crpost_tmp,axis=0)
    hypermean_amps=crpost[:,5]
    hypermean_widths=crpost[:,6]
    hypercenter_skews,hyperhwidth_skews=crpost[:,7],crpost[:,8]
    mean_hamps[i],mean_hwidths[i],mean_hcenskew[i],mean_hHWskew[i]=np.average(hypermean_amps),np.average(hypermean_widths),np.average(hypercenter_skews),np.average(hyperhwidth_skews)
    fwidths = crpost[:,215:315]
    pamps,pskews = crpost[:,115:215],crpost[:,315:415]
    pnflares=crpost[:,14]
    mean_pnflares[i]=np.average(pnflares)
    post_taus = np.abs(crpost[:,1])
    post_mus=np.abs(crpost[:,2])
    post_mus[post_mus>1]=1./post_mus[post_mus>1]
    truetau=np.abs(taus[i])
    avg_fwidth[i]=np.mean(fwidths[fwidths>0])
    fwidth_tmp,pamp_tmp,pskew_tmp = np.zeros(len(post_taus)),np.zeros(len(post_taus)),np.zeros(len(post_taus))
    for j in range(0,len(post_taus)): 
        fwidth_tmp[j] = np.mean(fwidths[j][:pnflares[j]])
        pamp_tmp[j] = np.mean(pamps[j][:pnflares[j]])
        pskew_tmp[j] = np.mean(pskews[j][:pnflares[j]])
    medtau[i]=np.median(post_taus)
    medmu[i]=np.median(post_mus)
    mean_pamp[i],mean_pskew[i],mean_pfwidth[i]=np.average(pamp_tmp),np.average(pskew_tmp),np.average(fwidth_tmp)
    plt.clf()
    plt.figure(it+1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    #plt.scatter(tau,mu)
    #plt.xlabel('Time Delay (days)',fontsize=14)
    #plt.ylabel('Magnification')
    #plt.title('%s'%lens)
    full_arr=np.concatenate(([np.abs(post_taus-tau)],[post_mus],[hypermean_amps],[hypermean_widths],[hypercenter_skews],[hyperhwidth_skews]),axis=0)
    full_arr=full_arr[:,np.array(1-isnan(np.sum(full_arr,axis=0)),dtype='bool')]
    label_arr=np.array(['DelTau','Mu','H.Amp.','H.Width','H.cen.Skew','H.HW.Skew'])
    #extent_dict={5:[1.,1.,1.,1.,(0,42),(0,12),1.,1.,1.,1.],10:[1.,1.,1.,1.,(0,52),(0,30),1.,1.,1.,1.],15:[1.,1.,1.,1.,(0,35),(0,25),1.,1.,1.,1.],20:[1.,1.,1.,1.,(0,40),(0,7.5),1.,1.,1.,1.]}
    extent_dict={5:[1.,1.,1.,1.,1.,1.],10:[1.,1.,1.,1.,1.,1.],15:[1.,1.,1.,1.,1.,1.],20:[1.,1.,1.,1.,1.,1.]}
    figure=corner(np.transpose(full_arr),labels=label_arr,extents=extent_dict[tau])
    #corner(np.transpose(full_arr))
    plt.savefig('/home/rumbaugh/Fermi/TimeBombs/plots/corner_plt.testlightcurve_%i.iter_%i_%s.png'%(tau,pair,date))
    plt.close()
