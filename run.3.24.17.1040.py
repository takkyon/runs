execfile('/home/rumbaugh/pythonscripts/plot_DB_lightcurves.py')
import pyfits as py
import time

clqsize=16

hdu=py.open('/home/rumbaugh/var_database/Y3A1/masterfile.fits')
data=hdu[1].data 

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdr=np.where(crdb['SDSSNAME']!='-1')[0]
crdb=crdb[gdr]

try:
    crp=np.loadtxt('/home/rumbaugh/primarydbid_table.3.24.17.1040.dat',dtype='|S48')
    PrimaryDBID={crp[:,0][x]: crp[:,1][x] for x in np.arange(len(crp))}
except:
    print 'Starting first loop...'
    st=time.time()
    gdb=np.where(crdb['SDSSNAME']!='-1')[0]
    PrimaryDBID_dict={}
    for i in range(0,len(gdb)):
        PrimaryDBID=crdb['DatabaseID'][gdb[i]]
        AllDBIDs = crdb['DBIDS'][gdb[i]]
        AllDBIDs=AllDBIDs.split(';')
        for DBID in AllDBIDs:
            if DBID[:2]=='DR': PrimaryDBID_dict[DBID]=PrimaryDBID
        try:
            PrimaryDBID_dict[DBID]
        except KeyError:
            print "Couldn't find DBID for "+PrimaryDBID
    poutcr=np.zeros((len(gdb),),dtype={'names':('key','val'),'formats':('|S48','|S48')})
    pkeys=PrimaryDBID_dict.keys()
    for i in range(0,len(gdb)): poutcr['key'][i],poutcr['val'][i]=pkeys[i],PrimaryDBID_dict[pkeys[i]]
    np.savetxt('/home/rumbaugh/primarydbid_table.3.24.17.1040.dat',poutcr,fmt='%s %s')
    end=time.time()
    print 'First loop took %f'%(end-st)

gmf_dr7=np.where(data['SDSSNAME']!='-1')[0]

#cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/CLQ_candidates_DR7.3.8.17.dat',dtype={'names':('DBID','drop','S1','S2','S82','flag'),'formats':('|S24','f8','|S4','|S4','i8','i8')},skiprows=1)

cr=np.loadtxt('/home/rumbaugh/var_database/Y3A1/max_mag_drop_DR7.3.23.17.dat',dtype={'names':('DBID','drop','Surv1','Surv2','S82','Baseline'),'formats':('|S32','f8','|S8','|S8','i8','f8')},skiprows=1)
cr=cr[gdr]
try:
    gmf=np.loadtxt('/home/rumbaugh/gmf_table.3.24.17.1040.dat',dtype='i8')
except:
    print 'Starting second loop...'
    st=time.time()
    gmf=np.zeros(len(cr),dtype='i8')
    for i in range(0,len(gmf)):
        #PDBID=PrimaryDBID_dict[cr['DBID'][i]]
        #gp=np.where(data['DatabaseID']==PDBID)[0]
        gp=np.where(data['DatabaseID']==cr['DBID'][i])[0]
        gmf[i]=gp[0]
    np.savetxt('/home/rumbaugh/gmf_table.3.24.17.1040.dat',gmf,fmt='%i')
    end=time.time()
    print 'Second loop took %f'%(end-st)
medu,medg,medr,medi,medz=data['med_SDSS_u'][gmf],data['med_SDSS_g'][gmf],data['med_SDSS_r'][gmf],data['med_SDSS_i'][gmf],data['med_SDSS_z'][gmf]
medu_all,medg_all,medr_all,medi_all,medz_all=data['med_SDSS_u'][gmf_dr7],data['med_SDSS_g'][gmf_dr7],data['med_SDSS_r'][gmf_dr7],data['med_SDSS_i'][gmf_dr7],data['med_SDSS_z'][gmf_dr7]

crmd=cr[np.abs(cr['drop'])>1]
gmf_md=gmf[np.abs(cr['drop'])>1]

good_dbids=crmd['DBID'][np.abs(crmd['drop'])>1]
gooddrops=np.abs(crmd['drop'])[np.abs(crmd['drop'])>1]

hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
bhdata=hdubh[1].data
hduc=py.open('/home/rumbaugh/dr7_control.fits')
cdata=hduc[1].data
gl=np.where(bhdata['LOGLBOL']>0)[0]
bhdata=bhdata[gl]
bhz,bhname,bhL=bhdata['REDSHIFT'],bhdata['SDSS_NAME'],bhdata['LOGLBOL']
bhmagu,bhmagg,bhmagr,bhmagi,bhmagz,bhmagwise1,bhmagwise2,bhmagwise3,bhmagwise4=bhdata['UGRIZ'][:,0],bhdata['UGRIZ'][:,1],bhdata['UGRIZ'][:,2],bhdata['UGRIZ'][:,3],bhdata['UGRIZ'][:,4],bhdata['WISE1234'][:,0],bhdata['WISE1234'][:,1],bhdata['WISE1234'][:,2],bhdata['WISE1234'][:,3]
glc=np.where(cdata['LOGLBOL']>0)[0]
cdata=cdata[glc]
cz,cname,cL=cdata['REDSHIFT'],cdata['SDSS_NAME'],cdata['LOGLBOL']
cmagu,cmagg,cmagr,cmagi,cmagz,cmagwise1,cmagwise2,cmagwise3,cmagwise4=cdata['UGRIZ'][:,0],cdata['UGRIZ'][:,1],cdata['UGRIZ'][:,2],cdata['UGRIZ'][:,3],cdata['UGRIZ'][:,4],cdata['WISE1234'][:,0],cdata['WISE1234'][:,1],cdata['WISE1234'][:,2],cdata['WISE1234'][:,3]
bhdbid,cdbid=np.array(bhname,copy=True,dtype='|S24'),np.array(cname,copy=True,dtype='|S24')
for i in range(0,len(bhname)):
    try:
        bhdbid[i]=PrimaryDBID_dict['DR7BH%s'%bhname[i]]
    except:
        bhdbid[i]='DR7BH%s'%bhname[i]
for i in range(0,len(cname)):
    try:
        cdbid[i]=PrimaryDBID_dict['DR7BH%s'%cname[i]]
    except:
        cdbid[i]='DR7BH%s'%cname[i]

#try:
#    crcon=np.loadtxt('/home/rumbaugh/control_DBIDs.3.24.17.1040.dat',dtype={'names':('DBID','gdb'),'formats':('|S24','i8')})
#    cDBIDs,cgdb=crcon['DBID'],crcon['gdb']
#except:
#    print 'Starting third loop...'
#    st=time.time()
#    cDBIDs,cgdb=np.zeros(len(cz),dtype='|S24'),np.zeros(len(cz),dtype='i8')
#    for i in range(0,len(cgdb)):
#        cgdb[i]=np.where(crdb['DatabaseID']==PrimaryDBID_dict['DR7BH%s'%cname[i]])[0][0]
#        cDBIDs[i]=crdb['DatabaseID'][cgdb[i]]
#    conoutcr=np.zeros((len(cgdb),),dtype={'names':('DBID','gdb'),'formats':('|S24','i8')})
#    conoutcr['DBID'],conoutcr['gdb']=cDBIDs,cgdb
#    np.loadtxt('/home/rumbaugh/control_DBIDs.3.24.17.1040.dat',conoutcr,fmt='%s %i')
#    end=time.time()
#    print 'Third loop took %f'%(end-st)

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

plt.figure(1)
plt.clf()
plt.plot(np.sort(np.abs(cr['drop'])),(np.arange(len(cr))+1.)/len(cr),lw=2,color='k')
plt.xlabel('Magnitude Change')
plt.ylabel('Cumulative Fraction')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/MagDropPlot.CLQ_candidates.DR7.3.24.17.png')

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=2)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax2.tick_params(which='major',length=8,width=2,labelsize=14)
ax2.tick_params(which='minor',length=4,width=1.5,labelsize=14)
a=ax.hist(cr['Baseline'],range=(0,6500),bins=26,color='k',edgecolor='k',facecolor='None')
b=ax2.plot(np.sort(cr['Baseline']),(np.arange(len(cr))+1.)/len(cr),lw=2,color='r')
ax.set_xlabel('Maximum Change Baseline (days)')
ax.set_ylabel(r'N$_{obj}$')
ax2.set_ylabel('Cumulative Fraction')
ax.set_xlim(0,6500)
ax2.set_xlim(0,6500)
ax2.set_ylim(0,1)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/MaxChangeBaselinePlot.CLQ_candidates.DR7.3.24.17.png')

print 'Starting good_id loops...'
st=time.time()
ggd=np.zeros(len(good_dbids),dtype='i8')
gkeep=np.ones(len(good_dbids),dtype='bool')
for i in range(0,len(ggd)): 
    ggddb=np.where(good_dbids[i]==crdb['DatabaseID'])[0][0]
    try:
        ggd[i]=np.where(bhname==crdb['SDSSNAME'][ggddb])[0][0]
    except IndexError:
        gkeep[i]=0
good_dbids,ggd,gooddrops=good_dbids[gkeep],ggd[gkeep],gooddrops[gkeep]
extra_good_dbids=good_dbids[gooddrops>1.5]
extra_extra_good_dbids=good_dbids[gooddrops>2]
gegd=np.zeros(len(extra_good_dbids),dtype='i8')
for i in range(0,len(gegd)): 
    gegddb=np.where(extra_good_dbids[i]==crdb['DatabaseID'])[0][0]
    gegd[i]=np.where(bhname==crdb['SDSSNAME'][gegddb])[0][0]
geegd=np.zeros(len(extra_extra_good_dbids),dtype='i8')
for i in range(0,len(geegd)): 
    geegddb=np.where(crdb['DatabaseID']==extra_extra_good_dbids[i])[0][0]
    geegd[i]=np.where(bhname==crdb['SDSSNAME'][geegddb])[0][0]
end=time.time()
print 'good_id loops took %f'%(end-st)


plt.figure(1)
plt.clf()
plt.scatter(gooddrops,bhL[ggd])
plt.xlabel('Magnitude Drop')
plt.ylabel(r'$log\left(L_{BOL}\right)$')
#plt.xlim(zmin,zmax)
#plt.ylim(Lmin,Lmax)
plt.xlim(0.99,3.2)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdrop-lum_plot.DR7_CLQ_candidates.3.24.17.png')


execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

plt.figure(1)
plt.clf()
#Lmin,Lmax,zmin,zmax=np.min(bhL),np.max(bhL),np.min(bhz),np.max(bhz)
#tsize=30
#Lbnds,zbnds=np.linspace(Lmin,Lmax,tsize+1),np.linspace(zmin,zmax,tsize+1)
#zcens,Lcens=0.5*(zbnds[:-1]+zbnds[1:]),0.5*(Lbnds[:-1]+Lbnds[1:])
#zsize,Lsize=zcens[1]-zcens[0],Lcens[1]-Lcens[0]
#zL_pairs=np.meshgrid(zcens,Lcens)
#richness=np.zeros(np.shape(zL_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhz,cur_bhL=zL_pairs[0][i][j],zL_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhz-bhz)<=0.5*zsize)&(np.abs(cur_bhL-bhL)<=0.5*Lsize))[0])
plt.scatter(bhz,bhL,s=2,edgecolor='None',marker='.',color='k')
plt.scatter(cz,cL,s=8,edgecolor='None',marker='.',color='b')
#plt.contour(zL_pairs[0],zL_pairs[1],richness,color='k')
plt.scatter(bhz[ggd],bhL[ggd],color='green',s=clqsize)
plt.scatter(bhz[gegd],bhL[gegd],color='magenta',s=clqsize+2)
plt.scatter(bhz[geegd],bhL[geegd],color='red',s=clqsize+4)
plt.xlabel('Redshift')
plt.ylabel(r'$log\left(L_{BOL}\right)$')
#plt.xlim(zmin,zmax)
#plt.ylim(Lmin,Lmax)
plt.xlim(0,3.5)
plt.ylim(44.75,47.4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/L-z_plot.DR7_CLQ_candidates.3.24.17.png')

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')


bhOIII,bhHB,bhFe=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']
bhOIIIorig,bhHBorig,bhFeorig=bhdata['EW_OIII_5007'],bhdata['FWHM_BROAD_HB'],bhdata['EW_FE_HB_4434_4684']

ggs=np.where((bhHB>0)&(bhFe>0))[0]
bhOIII,bhHB,bhFe=bhOIII[ggs],bhHB[ggs],bhFe[ggs]

plt.figure(1)
plt.clf()
#HBmin,HBmax,Femin,Femax=np.min(bhHB),np.max(bhHB),np.min(bhFe),np.max(bhFe)
#HBmin,HBmax,Femin,Femax=0,10000,0,200
#tsize=30
#HBbnds,Febnds=np.linspace(HBmin,HBmax,tsize+1),np.linspace(Femin,Femax,tsize+1)
#Fecens,HBcens=0.5*(Febnds[:-1]+Febnds[1:]),0.5*(HBbnds[:-1]+HBbnds[1:])
#Fesize,HBsize=Fecens[1]-Fecens[0],HBcens[1]-HBcens[0]
#zHB_pairs=np.zeros((2,tsize**2))
#zHB_pairs[0],zHB_pairs[1]=np.repeat(zcens,len(HBcens)),np.tile(HBcens,len(zcens))
#richness=np.zeros(len(zHB_pairs[0]))
#FeHB_pairs=np.meshgrid(Fecens,HBcens)
#richness=np.zeros(np.shape(FeHB_pairs[0]))
#for i in np.arange(tsize):
#    for j in np.arange(tsize):
#        cur_bhFe,cur_bhHB=FeHB_pairs[0][i][j],FeHB_pairs[1][i][j]
#        richness[i][j]=len(np.where((np.abs(cur_bhFe-bhFe)<=0.5*Fesize)&(np.abs(cur_bhHB-bhHB)<=0.5*HBsize))[0])
plt.scatter(bhFe,bhHB,s=2,edgecolor='None',marker='.',color='k')
#plt.contour(FeHB_pairs[0],FeHB_pairs[1],richness,color='k')
ggz,gegz,geegz=np.where((bhFeorig[ggd]>0)&(bhHBorig[ggd]>0))[0],np.where((bhFeorig[gegd]>0)&(bhHBorig[gegd]>0))[0],np.where((bhFeorig[geegd]>0)&(bhHBorig[geegd]>0))[0]
plt.scatter(bhFeorig[ggd[ggz]],bhHBorig[ggd[ggz]],color='green',s=clqsize)
plt.scatter(bhFeorig[gegd[gegz]],bhHBorig[gegd[gegz]],color='magenta',s=clqsize+2)
plt.scatter(bhFeorig[geegd[geegz]],bhHBorig[geegd[geegz]],color='red',s=clqsize+4)
plt.xlabel('EW(Fe)')
plt.ylabel(r'FWHM(H$\beta$)')
#plt.xlim(Femin,Femax)
#plt.ylim(HBmin,HBmax)
plt.xlim(0,200)
plt.ylim(0,10000)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/HB-Fe_plot.DR7_CLQ_candidates.3.24.17.png')

csize=8
gdsize=16

plt.figure(1)
plt.clf()
bhgr,bhug=bhmagg-bhmagr,bhmagu-bhmagg
cgr,cug=cmagg-cmagr,cmagu-cmagg
ggdgr,ggdug=bhmagg[ggd]-bhmagr[ggd],bhmagu[ggd]-bhmagg[ggd]
gegdgr,gegdug=bhmagg[gegd]-bhmagr[gegd],bhmagu[gegd]-bhmagg[gegd]
geegdgr,geegdug=bhmagg[geegd]-bhmagr[geegd],bhmagu[geegd]-bhmagg[geegd]
plt.scatter(bhgr,bhug,color='k',s=2,edgecolor='None',marker='.')
plt.scatter(cgr,cug,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdgr,ggdug,color='green',s=gdsize,edgecolor='None',marker='o')
plt.scatter(gegdgr,gegdug,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
plt.scatter(geegdgr,geegdug,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.xlabel(r'$g-r$')
plt.ylabel(r'$u-g$')
#plt.xlim(-0.5,1.2)
#plt.ylim(-0.5,4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/u-g_vs_g-r.DR7_CLQ_candidates.3.24.17.png')

plt.figure(1)
plt.clf()
bhri,bhgr=bhmagr-bhmagi,bhmagg-bhmagr
cri,cgr=cmagr-cmagi,cmagg-cmagr
ggdri,ggdgr=bhmagr[ggd]-bhmagi[ggd],bhmagg[ggd]-bhmagr[ggd]
gegdri,gegdgr=bhmagr[gegd]-bhmagi[gegd],bhmagg[gegd]-bhmagr[gegd]
geegdri,geegdgr=bhmagr[geegd]-bhmagi[geegd],bhmagg[geegd]-bhmagr[geegd]
plt.scatter(bhri,bhgr,color='k',s=2,edgecolor='None',marker='.')
plt.scatter(cri,cgr,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdri,ggdgr,color='green',s=gdsize,edgecolor='None',marker='o')
plt.scatter(gegdri,gegdgr,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
plt.scatter(geegdri,geegdgr,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.xlabel(r'$g-r$')
plt.ylabel(r'$r-i$')
#plt.xlim(-0.5,1.2)
#plt.ylim(-0.5,4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/r-i_vs_g-r.DR7_CLQ_candidates.3.24.17.png')


plt.figure(1)
plt.clf()
bhW1W2,bhrW1=bhmagwise1-bhmagwise2,bhmagr-bhmagwise1
cW1W2,crW1=cmagwise1-cmagwise2,cmagr-cmagwise1
ggdW1W2,ggdrW1=bhmagwise1[ggd]-bhmagwise2[ggd],bhmagr[ggd]-bhmagwise1[ggd]
gegdW1W2,gegdrW1=bhmagwise1[gegd]-bhmagwise2[gegd],bhmagr[gegd]-bhmagwise1[gegd]
geegdW1W2,geegdrW1=bhmagwise1[geegd]-bhmagwise2[geegd],bhmagr[geegd]-bhmagwise1[geegd]
plt.scatter(bhW1W2,bhrW1,color='k',s=2,edgecolor='None',marker='.')
plt.scatter(cW1W2,crW1,color='b',s=csize,edgecolor='None',marker='.')
plt.scatter(ggdW1W2,ggdrW1,color='green',s=gdsize,edgecolor='None',marker='o')
plt.scatter(gegdW1W2,gegdrW1,color='magenta',s=gdsize+2,edgecolor='None',marker='o')
plt.scatter(geegdW1W2,geegdrW1,color='red',s=gdsize+4,edgecolor='None',marker='o')
plt.xlabel('W1-W2')
plt.ylabel(r'$r-$W1')
#plt.xlim(-0.5,1.2)
#plt.ylim(-0.5,4)
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/W1-W2_vs_r-W1.DR7_CLQ_candidates.3.24.17.png')

