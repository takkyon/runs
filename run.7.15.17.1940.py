import carmcmc as cm
import numpy as np
import pandas as pd
import pickle
import pyfits as py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf

outlier_window=300
outlier_thresh=0.5
num=5000

ri=30122
normfrac=0.317310507863
nsamples=20000

iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

hdu=py.open('/home/rumbaugh/S2_lc.fits')
sndata=hdu[1].data

cenra,cendec=sndata['RA'][ri],sndata['DEC'][ri]
gri=np.sort(np.where((np.abs(cenra-sndata["RA"])<0.3)&(np.abs(cendec-sndata['DEC'])<0.3))[0])
data=sndata[gri]

outdf=pd.DataFrame({x: np.zeros(len(gri)) for x in ['tau','taulb','tauub','sig','siglb','sigub','numepoch_tot','numepoch']})
outdf['DataID']=gri
for ind in np.arange(len(data['COADD_OBJECT_ID'])):
    len_lc=np.count_nonzero(data[ind]['LC_MJD_G'])
    outdf.numepoch_tot[ind]=len_lc
    if len_lc<6:
        continue
    DBID=data['COADD_OBJECT_ID'][ind]
    mjd,mag,magerr=np.zeros(len_lc),np.zeros(len_lc),np.zeros(len_lc)
    mjd[:],mag[:],magerr[:]=data[ind]['LC_MJD_G'][:len_lc],data[ind]['LC_MAG_AUTO_G'][:len_lc],data[ind]['LC_MAGERR_AUTO_G'][:len_lc]
    inf_or_nan=np.ones(len(mjd),dtype='bool')
    for arr in [mjd,mag,magerr]:
        for func in [np.isnan,np.isinf]:
            inf_or_nan*=np.invert(func(arr))
    mjd,mag,magerr=mjd[inf_or_nan],mag[inf_or_nan],magerr[inf_or_nan]
    len_lc=len(mjd)
    outlier_arr= np.zeros(len_lc,dtype='bool')
    for ipt in np.arange(len(outlier_arr)):
        gthresh=np.where(np.abs(mjd-mjd[ipt])<outlier_window)[0]
        if len(gthresh)>1:
            outlier_arr[ipt]= np.abs(np.median(mag[gthresh])-mag[ipt]) > outlier_thresh
    mjd,mag,magerr=mjd[outlier_arr==False],mag[outlier_arr==False],magerr[outlier_arr==False]
    outdf.numepoch[ind]=len(mjd)
    DRWmodel=cm.CarmaModel(mjd,mag,magerr,p=1,q=0)
    DRWsample=DRWmodel.run_mcmc(nsamples)

    lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
    lomega,sigma=np.median(lomega_samples),np.median(sigma_samples)
    lomegaLB,lomegaUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
    pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/SN_fields/S2/%i.DRWsample_AUTO_OR.pickle'%DBID,'wb'))
    outdf['tau'][ind],outdf['taulb'][ind],outdf['tauub'][ind],outdf['sig'][ind],outdf['siglb'][ind],outdf['sigub'][ind]=np.exp(-lomega),np.exp(-lomegaUB),np.exp(-lomegaLB),sigma,sigmaLB,sigmaUB
outdf['cid']=data['COADD_OBJECT_ID']
outdf['RA'],outdf["DEC"]=data['RA'],data['DEC']
outdf.to_csv('/home/rumbaugh/SN_fields.S2.cen_{}.AUTO_CAR1fits.csv'.format(ri),index=False)
