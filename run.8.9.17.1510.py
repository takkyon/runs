import numpy as np
import pandas as pd
import scipy.integrate
import matplotlib.pyplot as plt
try:
    alpha
except NameError:
    alpha=0.1

from sklearn.decomposition import PCA
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

df=pd.read_csv('/home/rumbaugh/Chandra/ORELSE.test_compiled.8.9.17.csv')

df=df[(df.cluster!='RXJ1716A')&(df.cluster!='Cl0849')&(df.cluster!='0225-0019')&(df.cluster!='1053+5735')&(df.cluster!='1324+3013')]
df=df.set_index(df.cluster)
df=pd.merge(df,vcdf,left_index=True,right_index=True)
perc_sinds=np.searchsorted(gaussints,df.perc)
df['perc_norm']=gsigs[perc_sinds]

df['sigdiff']=np.abs(df.Sig_Q-df.Sig_SF)/np.sqrt(df.Sig_Q_Error**2+df.Sig_SF_Error**2)

P_DS_sinds=np.searchsorted(gaussints,df.P_DS)
df['P_DS_norm']=gsigs[P_DS_sinds]

df['P3_sig']=df.P3-df.P3LB
df['P3_cat']=pd.cut(df.P3_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P3_norm']=df.P3_cat.cat.codes-1

df['P4_sig']=df.P4-df.P4LB
df['P4_cat']=pd.cut(df.P4_sig,[-np.inf,0,np.inf],labels=[-1,0])
df['P4_norm']=df.P4_cat.cat.codes-1

df_dists=df[['dist_mmcg2x', 'dist_mmcg2lw', 'dist_lw2x']]
df['dist_max'],df['dist_min']=df_dists.max(axis=1),df_dists.min(axis=1)
df['dist_metric']=0.5*(df.dist_max+df.dist_min)
df['dist_norm']=df.dist_metric/df.LWerr
df['dist_mmcg2x_norm'],df['dist_mmcg2lw_norm'],df['dist_lw2x_norm']=df['dist_mmcg2x']/df.LWerr,df['dist_mmcg2lw']/df.LWerr,df['dist_lw2x']/df.LWerr

df['MMCGvel_norm']=(df.MMCGvel-df.zmed)/df.zUB
df.MMCGvel_norm[df.MMCGvel_norm<1]=(df.zmed[df.MMCGvel_norm<1]-df.MMCGvel[df.MMCGvel_norm<1])/df.zLB[df.MMCGvel_norm<1]


#df.set_value('RXJ1221B','sigdiff',np.nan)
#df.set_value('RXJ1221B','perc_norm',np.nan)


df['total_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_offset']=df[['mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)
df['total_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].sum(axis=1)
df['mean_SR_LxTlit_offset']=df[['mindistlit_LxT','mindistfit_sigT','mindistfit_Lxsig']].mean(axis=1,skipna=True)

plt.figure(1)
plt.clf()
plt.errorbar(df.mean_SR_offset.values,df.qfrac.values,yerr=df.qfracerr.values,color='r',fmt='o',capsize=3,mew=1,ms=4)
plt.xlabel(r'Mean Scaling Relation Offset ($\sigma$)')
plt.ylabel('Quiescent Fraction')
plt.savefig('/home/rumbaugh/SRoffset_vs_Qfrac.png')


dfnorm=df[['field','cluster','perc_norm','sigdiff','P_DS_norm','P3_norm','P4_norm','dist_norm','dist_mmcg2x_norm', 'dist_mmcg2lw_norm', 'dist_lw2x_norm','MMCGvel_norm','total_SR_offset','mean_SR_offset','total_SR_LxTlit_offset','mean_SR_LxTlit_offset','qfrac','qfracspec','qfracerr','qfracspecerr','zcen']]

gkeep=np.isfinite(dfnorm.qfrac.values)


pca=PCA()
metrics=['perc_norm','sigdiff','P_DS_norm','P3_norm','P4_norm','dist_mmcg2x_norm', 'dist_mmcg2lw_norm', 'dist_lw2x_norm','MMCGvel_norm','qfrac']
X=np.zeros((len(dfnorm),len(metrics)))
for i,norm in zip(np.arange(len(metrics)),metrics): X[:,i]=dfnorm[norm].values
pca = PCA()
X_r = pca.fit(X).transform(X)
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

Xgd,dfnormgd,dfgd=X[gkeep],dfnorm[gkeep],df[gkeep]

from sklearn import linear_model
reg = linear_model.Lasso(alpha = alpha)
reg.fit(Xgd,dfnormgd.qfrac)

rege = linear_model.ElasticNet(alpha = alpha)
rege.fit(Xgd,dfnormgd.qfrac)

for model,method,offset in zip([reg,rege],['Lasso','ElasticNet'],['qfrac','qfrac']):
    print method, offset, 'score: %7.5f\n'%model.score(Xgd,dfgd[offset]),model.coef_

offsets=['mindistlit_LxT','mindistfit_LxT','mindistfit_sigT','mindistfit_Lxsig','mean_SR_offset','mean_SR_LxTlit_offset']
index_arr=np.zeros((2,len(metrics)*len(offsets)),dtype='|S30')
index_arr[0]=np.repeat(metrics,len(offsets))
index_arr[1]=np.tile(offsets,len(metrics))
index_tuples=list(zip(*index_arr))
index = pd.MultiIndex.from_tuples(index_tuples, names=['metric', 'SR_offset'])
s_coef,s_score=pd.Series(np.zeros(len(metrics)*len(offsets)),index=index),pd.Series(np.zeros(len(metrics)*len(offsets)),index=index)
df_linreg=pd.DataFrame(np.zeros((len(metrics)*len(offsets),2)),index=index,columns=['coef','score'])
for metric in metrics:
    for offset in offsets:
        regt=linear_model.LinearRegression()
        Xt=dfgd[metric][:,np.newaxis]
        regt.fit(Xt,dfgd[offset])
        df_linreg.loc[metric,offset]['coef']=regt.coef_[0]
        df_linreg.loc[metric,offset]['score']=regt.score(Xt,dfgd[offset])
df_linreg.to_csv('/home/rumbaugh/Chandra/vir_metric_linreg.alpha_%.1f.8.9.17.csv'%alpha)

  
regall=linear_model.LinearRegression()
regall.fit(Xgd,dfnormgd.mean_SR_offset)
for i in range(0,len(metrics)): print '{}: {}'.format(metrics[i],regall.coef_[i])
print 'Score: ',regall.score(Xgd,dfnormgd.mean_SR_offset)
print ' '
regall=linear_model.LinearRegression()
regall.fit(Xgd,dfnormgd.mean_SR_LxTlit_offset)
for i in range(0,len(metrics)): print '{}: {}'.format(metrics[i],regall.coef_[i])
print 'Score: ',regall.score(Xgd,dfnormgd.mean_SR_LxTlit_offset)

for cutmetric,im in zip(metrics,np.arange(len(metrics))):
    regtmp = linear_model.LinearRegression()
    tmpinds=np.delete(np.arange(len(metrics)),im)
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print '(linreg) No %s - score: %.5f'%(cutmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))

print 'addmetric'
for addmetric,im in zip(metrics[:-1],np.arange(len(metrics)-1)):
    regtmp = linear_model.LinearRegression()
    tmpinds=[im,len(metrics)-1]
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_offset)
    print 'qfrac + %s - score: %.5f'%(addmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))

print 'addmetric, LxTlit'
for addmetric,im in zip(metrics[:-1],np.arange(len(metrics)-1)):
    regtmp = linear_model.LinearRegression()
    tmpinds=[im,len(metrics)-1]
    Xtmp=Xgd[:,tmpinds]
    regtmp.fit(Xtmp,dfnormgd.mean_SR_LxTlit_offset)
    print 'qfrac + %s - score: %.5f'%(addmetric,regtmp.score(Xtmp,dfnormgd.mean_SR_LxTlit_offset))

