import numpy as np
import pandas as pd
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

ntrials=10000
normfrac=0.317310507863
iUB=int(ntrials*(1-normfrac))

def open_csv(fname):
    df=pd.read_csv(fname,delim_whitespace=True)
    if df.columns[0]=='#':
        newnames=df.columns[1:].tolist()
        df=pd.read_csv(fname,delim_whitespace=True,comment='#',names=newnames)
    return df

clbdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_bounds.dat')
clmdf=open_csv('/home/rumbaugh/Chandra/ORELSE.cluster_members.dat')
bcgdf=open_csv('/home/rumbaugh/Chandra/ORELSE_cluster_member_info_all.dat')
tbcgdf=bcgdf[bcgdf.isBCG_tot==1].set_index(['cluster'])

bcgra,bcgdec,lwra,lwdec,lwN=np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf),dtype='i8')
dist_bcg2x,dist_bcg2lw,dist_lw2x=np.zeros(len(clbdf)),np.zeros(len(clbdf)),np.zeros(len(clbdf))
LWerr=np.zeros(len(clbdf))
for cluster,ic in zip(clbdf.cluster.unique(),np.arange(len(clbdf.cluster.unique()))):
    bcgra[ic],bcgdec[ic]=tbcgdf.loc[cluster].ra,tbcgdf.loc[cluster].dec
    lw_wt=(1./clmdf[clmdf.cluster==cluster].Mred).sum()
    lwra[ic],lwdec[ic]=(clmdf[clmdf.cluster==cluster].ra/clmdf[clmdf.cluster==cluster].Mred).sum()/lw_wt,(clmdf[clmdf.cluster==cluster].dec/clmdf[clmdf.cluster==cluster].Mred).sum()/lw_wt
    lwN[ic]=len(clmdf[clmdf.cluster==cluster])
    tmpdf=clmdf[clmdf.cluster==cluster]
    dist_bcg2x[ic],dist_bcg2lw[ic],dist_lw2x[ic]=SphDist(bcgra[ic],bcgdec[ic],clbdf.ra[ic],clbdf.dec[ic])*60,SphDist(bcgra[ic],bcgdec[ic],lwra[ic],lwdec[ic],)*60,SphDist(lwra[ic],lwdec[ic],clbdf.ra[ic],clbdf.dec[ic])*60
    grand=np.random.choice(np.arange(len(tmpdf)),((ntrials,len(tmpdf))))
    tmplw_wt=np.sum(1./tmpdf.Mred.values[grand],axis=1)
    tmplwra,tmplwdec=np.sum(tmpdf.ra.values[grand]/tmpdf.Mred.values[grand],axis=1)/tmplw_wt,np.sum(tmpdf.dec.values[grand]/tmpdf.Mred.values[grand],axis=1)/tmplw_wt
    tmpracen,tmpdeccen=np.median(tmplwra),np.median(tmplwdec)
    tmpdists=np.sort(SphDist(tmplwra,tmplwdec,tmpracen,tmpdeccen)*60)
    LWerr[ic]=tmpdists[iUB]
outdf=pd.DataFrame({'field':clbdf.field,'cluster':clbdf.cluster.unique(),'Xray_ra':clbdf.ra,'Xray_dec':clbdf.dec,'BCG_ra':bcgra,'BCG_dec':bcgdec,'LWM_ra':lwra,'LWM_dec':lwdec,'LWM_Ngal':lwN,'dist_bcg2x':dist_bcg2x,'dist_bcg2lw':dist_bcg2lw,'dist_lw2x':dist_lw2x,'LWerr':LWerr})
outdf=outdf[['field','cluster','Xray_ra','Xray_dec','BCG_ra','BCG_dec','LWM_ra','LWM_dec','LWM_Ngal','dist_bcg2x','dist_bcg2lw','dist_lw2x','LWerr']]
outdf.to_csv('/home/rumbaugh/Chandra/ORELSE.cluster_centroids.csv',index=False)
