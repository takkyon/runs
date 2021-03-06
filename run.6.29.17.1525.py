import numpy as np
import pandas as pd
import carmcmc as cm
import pickle

outlier_window=300
outlier_thresh=0.5

try:
    dotest
except NameError:
    dotest=False
try:
    tests
except NameError:
    tests=10

normfrac=0.317310507863
nsamples=20000
iLB,iUB=int(normfrac*0.5*nsamples),int((1-0.5*normfrac)*nsamples)

DBdf=pd.read_csv('/home/rumbaugh/DB_QSO_S82.dat',delim_whitespace=True,names=['DBID','ra','dec','SDR5ID','Mi','Micorr','redshift','massBH','Lbol','u','g','r','i','z','Au'],skiprows=2)

if dotest: DBdf=DBdf.iloc[:tests]
#if dotest: DBdf=DBdf.iloc[np.random.choice(np.arange(len(DBdf)),tests,replace=False)]

params_df=pd.DataFrame({'DBID':DBdf.DBID})
for x in ['tau','taulb','tauub','sigma','sigmalb','sigmaub']: params_df[x]=np.zeros(len(DBdf))

for i in range(0,len(DBdf)):
    LCdf=pd.read_csv('/home/rumbaugh/QSO_S82/%i'%DBdf.iloc[i]['DBID'],delim_whitespace=True,names=['MJD_u','u','u_err','MJD_g','g','g_err','MJD_r','r','r_err','MJD_i','i','i_err','MJD_z','z','z_err','ra_median','dec_median'])
    LCdf=LCdf[(LCdf.g.values>0)&(LCdf.g.values<30)&(LCdf.g_err.values<3)&(LCdf.g_err.values>0)]

    try:
        outlier_arr=pickle.load(open('/home/rumbaugh/CARpickles/%i.outliers_g.pickle'%DBdf.iloc[i]['DBID'],'rb'))
    except IOError:
        outlier_arr= np.zeros(len(LCdf.g.values),dtype='bool')
        for ipt in np.arange(len(outlier_arr)):
            gthresh=np.where(np.abs(LCdf.MJD_g.values-LCdf.MJD_g.values[ipt])<outlier_window)[0]
            if len(gthresh)>1:
                outlier_arr[ipt]= np.abs(np.median(LCdf.g.values[gthresh])-LCdf.g.values[ipt]) > outlier_thresh
        pickle.dump(outlier_arr,open('/home/rumbaugh/CARpickles/%i.outliers_g.pickle'%DBdf.iloc[i]['DBID'],'wb'))
    if np.sum(outlier_arr)>0:
        LCdf=LCdf[outlier_arr==False]
        DRWmodel=cm.CarmaModel(LCdf.MJD_g.values,LCdf.g.values,LCdf.g_err.values,p=1,q=0)
        DRWsample=DRWmodel.run_mcmc(nsamples)
        lomega_samples,sigma_samples=np.sort(DRWsample.get_samples('log_omega').flatten()),np.sort(DRWsample.get_samples('sigma').flatten())
        lomega,sigma=np.median(lomega_samples),np.median(sigma_samples)
        lomegaLB,lomegaUB,sigmaLB,sigmaUB=lomega_samples[iLB],lomega_samples[iUB],sigma_samples[iLB],sigma_samples[iUB]
        params_df.loc[i,'tau'],params_df.loc[i,'sigma']=np.exp(-lomega),sigma
        params_df.loc[i,'taulb'],params_df.loc[i,'tauub'],params_df.loc[i,'sigmalb'],params_df.loc[i,'sigmaub']=np.exp(-lomegaUB),np.exp(-lomegaLB),sigmaLB,sigmaUB
        pickle.dump(DRWsample,open('/home/rumbaugh/CARpickles/%i.DRWsample_OR.pickle'%DBdf.iloc[i]['DBID'],'wb'))
params_df.to_csv('/home/rumbaugh/QSO_S82_CAR1_fits.OR.csv',index=False)
