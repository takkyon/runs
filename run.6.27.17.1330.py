import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.integrate

from sklearn.decomposition import PCA

try:
    alpha
except NameError:
    alpha=0.1

def gauss(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)

gtrials=10000
gsigs=np.linspace(5,0,gtrials)
try:
    gaussints
except NameError:
    gaussints=np.zeros(gtrials)
    for x,i in zip(gsigs,np.arange(gtrials)):
        gint,dum=scipy.integrate.quad(gauss,-x,x)
        gaussints[i]=1-gint


vcdf=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.velcenMC.csv',index_col='cluster')
vcdf=vcdf.rename(columns={'zcen':'zmed'})

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.csv')

df=df[(df.cluster!='RXJ1221B')&(df.cluster!='Cl0849')&(df.cluster!='0225-0019')]
df=df.set_index(df.cluster)
df=pd.merge(df,vcdf,left_index=True,right_index=True)

perc_sinds=np.searchsorted(gaussints,df.perc)
df['perc_norm']=gsigs[perc_sinds]

df['sigdiff']=np.abs(df.Sig_red-df.Sig_blue)/np.sqrt(df.Sig_red_Error**2+df.Sig_blue_Error**2)

P_DS_sinds=np.searchsorted(gaussints,df.P_DS)
df['P_DS_norm']=gsigs[P_DS_sinds]

df['P3_sig']=df.P3-df.P3LB
df['P3_cat']=pd.cut(df.P3_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P3_norm']=df.P3_cat.cat.codes-1

df['P4_sig']=df.P4-df.P4LB
df['P4_cat']=pd.cut(df.P4_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P4_norm']=df.P4_cat.cat.codes-1

df_dists=df[['dist_bcg2x', 'dist_bcg2lw', 'dist_lw2x']]
df['dist_max'],df['dist_min']=df_dists.max(axis=1),df_dists.min(axis=1)
df['dist_metric']=0.5*(df.dist_max+df.dist_min)
df['dist_norm']=df.dist_metric/df.LWerr
df['dist_bcg2x_norm'],df['dist_bcg2lw_norm'],df['dist_lw2x_norm']=df['dist_bcg2x']/df.LWerr,df['dist_bcg2lw']/df.LWerr,df['dist_lw2x']/df.LWerr

df['BCGvel_norm']=(df.BCGvel-df.zmed)/df.zUB
df.BCGvel_norm[df.BCGvel_norm<1]=(df.zmed[df.BCGvel_norm<1]-df.BCGvel[df.BCGvel_norm<1])/df.zLB[df.BCGvel_norm<1]


#df.set_value('RXJ1221B','sigdiff',np.nan)
#df.set_value('RXJ1221B','perc_norm',np.nan)


df['total_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)
df['total_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)

dfnorm=df[['field','cluster','perc_norm','sigdiff','P_DS_norm','P3_norm','P4_norm','dist_norm','dist_bcg2x_norm', 'dist_bcg2lw_norm', 'dist_lw2x_norm','BCGvel_norm','total_SR_offset','mean_SR_offset','total_SR_LxTlit_offset','mean_SR_LxTlit_offset']]

gkeep=np.isfinite(dfnorm.mean_SR_offset.values)


pca=PCA()
metrics=['perc_norm','sigdiff','P_DS_norm','P3_norm','P4_norm','dist_bcg2x_norm', 'dist_bcg2lw_norm', 'dist_lw2x_norm','BCGvel_norm']
X=np.zeros((len(dfnorm),9))
for i,norm in zip(np.arange(9),metrics): X[:,i]=dfnorm[norm].values
pca = PCA()
X_r = pca.fit(X).transform(X)
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

Xgd,dfnormgd,dfgd=X[gkeep],dfnorm[gkeep],df[gkeep]

from sklearn import linear_model
reg = linear_model.Lasso(alpha = alpha)
reg.fit(Xgd,dfnormgd.mean_SR_offset)

rege = linear_model.ElasticNet(alpha = alpha)
rege.fit(Xgd,dfnormgd.mean_SR_offset)

from sklearn import linear_model
regl = linear_model.Lasso(alpha = alpha)
regl.fit(Xgd,dfnormgd.mean_SR_LxTlit_offset)

regel = linear_model.ElasticNet(alpha = alpha)
regel.fit(Xgd,dfnormgd.mean_SR_LxTlit_offset)

from sklearn import linear_model
regl1 = linear_model.Lasso(alpha = alpha)
regl1.fit(Xgd,dfgd.mindistlit_LxT)

regel1 = linear_model.ElasticNet(alpha = alpha)
regel1.fit(Xgd,dfgd.mindistlit_LxT)

from sklearn import linear_model
regl2 = linear_model.Lasso(alpha = alpha)
regl2.fit(Xgd,dfgd.mindistfit_LxT)

regel2 = linear_model.ElasticNet(alpha = alpha)
regel2.fit(Xgd,dfgd.mindistfit_LxT)

for model,method,offset in zip([reg,rege,regl,regel,regl1,regel1],np.tile(['Lasso','ElasticNet'],4),np.repeat(['mean_SR_offset','mean_SR_LxTlit_offset','mindistlit_LxT','mindistfit_LxT'],2)):
    print method, offset, 'score: %7.5f\n'%model.score(Xgd,dfgd[offset]),model.coef_

offsets=['mindistlit_LxT','mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig','mean_SR_offset','mean_SR_LxTlit_offset']
index_arr=np.zeros((2,len(metrics)*len(offsets)),dtype='|S30')
index_arr[0]=np.repeat(metrics,len(offsets))
index_arr[1]=np.tile(offsets,len(metrics))
index_tuples=list(zip(*index_arr))
index = pd.MultiIndex.from_tuples(index_tuples, names=['metric', 'SR_offset'])
s_coef,s_score=pd.Series(np.zeros(54),index=index),pd.Series(np.zeros(54),index=index)
df_linreg=pd.DataFrame(np.zeros((len(metrics)*len(offsets),2)),index=index,columns=['coef','score'])
for metric in metrics:
    for offset in offsets:
        regt=linear_model.LinearRegression()
        Xt=dfgd[metric][:,np.newaxis]
        regt.fit(Xt,dfgd[offset])
        df_linreg.loc[metric,offset]['coef']=regt.coef_[0]
        df_linreg.loc[metric,offset]['score']=regt.score(Xt,dfgd[offset])
df_linreg.to_csv('/home/rumbaugh/Chandra/vir_metric_linreg.alpha_%.1f.6.27.17.csv'%alpha)
    
for cutmetric,im in zip(metrics,np.arange(len(metrics))):
    regtmp = linear_model.ElasticNet(alpha = alpha)
    tmpinds=np.delete(np.arange(len(metrics)),im)
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print 'No %s - score: %.5f\n'%(cutmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset)),regtmp.coef_

print '\nLxT only'    
for cutmetric,im in zip(metrics,np.arange(len(metrics))):
    regtmp = linear_model.ElasticNet(alpha = alpha)
    tmpinds=np.delete(np.arange(len(metrics)),im)
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfgd.mindistlit_LxT)
    print 'No %s - score: %.5f\n'%(cutmetric,regtmp.score(Xtmp,dfgd.mindistlit_LxT)),regtmp.coef_
print ' '
    
for cutmetric,im in zip(metrics,np.arange(len(metrics))):
    regtmp = linear_model.LinearRegression()
    tmpinds=np.delete(np.arange(len(metrics)),im)
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print '(linreg) No %s - score: %.5f'%(cutmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))


     
for addmetric,im in zip(np.delete(metrics,1),np.delete(np.arange(len(metrics)),1)):
    regtmp = linear_model.LinearRegression()
    tmpinds=[1,im]
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print 'sigdiff + %s - score: %.5f'%(addmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))

addinds=np.array([1])
for addmetric,im in zip(np.delete(metrics,1),np.delete(np.arange(len(metrics)),1)):
    regtmp = linear_model.LinearRegression()
    addinds=np.append(addinds,im)
    Xtmp=Xgd[:,addinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print '(cum) sigdiff + %s - score: %.5f'%(addmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))
addinds=np.array([-1])
for addmetric,im in zip(np.delete(metrics,-1),np.delete(np.arange(len(metrics)),-1)):
    regtmp = linear_model.LinearRegression()
    addinds=np.append(addinds,im)
    Xtmp=Xgd[:,addinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print '(cum) BCGvel_norm + %s - score: %.5f'%(addmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))

