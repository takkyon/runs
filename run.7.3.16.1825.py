import numpy as np
import pyfits as py
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/calc_Xray_lums.py')

adamcorrval=-1.3975614258700002

alpha_ref,alphaX = 11.1,1.1
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

crRSfit=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.3.13.16.dat',dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})

mtol=1.
ldate='1.19.16'
optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

refdir='/home/rumbaugh/git/ORELSE/Catalogs/tomczak_catalogs'
reffile_dict={"cl0023":'sg0023+0423_v0.1.9','cl1604':'sc1604_v0.0.3','rxj1757':'nep200_v0.0.4','rxj1821':'nep5281_v0.0.1','rxj1716':'rxj1716+6708_v0.0.7','rxj0910':'cl0910+5422_v0.0.2'}

rfmt=('i8',)
for k in range(0,42):rfmt=rfmt+('f8',)
#for k in range(0,4):rfmt=rfmt+('i8',)
refdict={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_Rplus','erraper_Rplus','magaper_Iplus','erraper_Iplus','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_K','erraper_K','magcolor_ch1','magcolor_ch1err','magcolor_ch2','magcolor_ch2err','apercorr','weight_B','weight_V','weight_Rplus','weight_Iplus','weight_r','weight_i','weight_z','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

rfmt=('i8',)
for k in range(0,33):rfmt=rfmt+('f8',)
refdict0910={'names':('ID','z_spec','ra','dec','magaper_V','erraper_V','magaper_Rc','erraper_Rc','magaper_Iplus','erraper_Iplus','magaper_Zplus','erraper_Zplus','magaper_J','erraper_J','magaper_K','erraper_K','magcolor_ch1','errcolor_ch1','magcolor_ch2','errcolor_ch2','apercorr','weight_V','weight_Rc','weight_Iplus','weight_Zplus','weight_J','weight_K','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

rfmt=('i8',)
for k in range(0,36):rfmt=rfmt+('f8',)
refdict_1821={'names':('ID','z_spec','ra','dec','magaper_B','erraper_B','magaper_V','erraper_V','magaper_r','erraper_r','magaper_i','erraper_i','magaper_z','erraper_z','magaper_J','erraper_J','magaper_Ks','erraper_Ks','magcolor_ch1','errcolor_ch1','magcolor_ch2','errcolor_ch2','apercorr','weight_B','weight_V','weight_r','weight_i','weight_z','weight_J','weight_Ks','weight_ch1','weight_ch2','wmin','star','saturation','badfit','use'),'formats':rfmt}

zfmt=('i8',)
for k in range(0,14):zfmt=zfmt+('f8',)
zfmt=zfmt+('i8',)
for k in range(0,4):zfmt=zfmt+('f8',)
pzdict={'names':('id','z_spec','z_a','z_m1','chi_a','z_p','chi_p','z_m2','odds','l68','u68','l95','u95','l99','u99','nfilt','q_z','z_peak','peak_prob','z_mc'),'formats':zfmt}

rffmt=('i8',)
for k in range(0,23):rffmt=rffmt+('f8',)
rfdict={'names':('id','z','DM','restflux_NUV','p16_NUV','p84_NUV','restflux_U','p16_U','p84_U','restflux_B','p16_B','p84_B','restflux_V','p16_V','p84_V','restflux_r','p16_r','p84_r','restflux_J','p16_J','p84_J','restflux_2800','p16_2800','p84_2800'),'formats':rffmt}

rffmt=('i8',)
for k in range(0,16):rffmt=rffmt+('f8',)
rfdict0910={'names':('id','z','DM','restflux_NUV','errflux_NUV','restflux_U','errflux_U','restflux_B','errflux_B','restflux_V','errflux_V','restflux_r','errflux_r','restflux_J','errflux_J','restflux_2800','errflux_2800'),'formats':rffmt}

FILEl=open('/home/rumbaugh/Chandra/fluxes_newphotoz_adam.1sig.5.5.16.dat','w')
FILEl.write('# field ID RA Dec z_peak nh flux_soft flux_hard flux_full P_inclus\n')

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

carr=np.array(['blue','green','orange','red','magenta','brown','gray','cyan'])
marr=np.array(['o','s','x','+','*'])

crRS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.AGN.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','magR','magI','magZ','SCmagRed','SCmagBlue'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8')})

crRS_ACS = np.loadtxt('/home/rumbaugh/Chandra/RS_offsets.cl1604_ACS.3.6.16.dat',dtype={'names':('field','number','RA','Dec','RSoffset','F606W','F814W'),'formats':('|S24','i8','f8','f8','f8','f8','f8')})


plottargets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])#,"cl1324_north","cl1324_south"])

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}

crn=np.loadtxt('/home/rumbaugh/X-ray_lum_cat.4.17.16.dat',dtype=indict)
g1324=np.where((crn['field']=='cl1324_north')|(crn['field']=='cl1324_south'))[0]
crn['field'][g1324]='cl1324'

gAGN=np.zeros(len(crRS['RA']-2),dtype='i8')
gnot1604=np.where(crRS['field']!='cl1604')[0]
RSO=np.zeros(len(gAGN))

fieldmarkers,fieldcolors={},{}


for i in range(0,len(crRS['RA'][gnot1604])):
    tmpdist=np.sqrt((crRS['RA'][gnot1604][i]-crn['RA'])**2+(crRS['Dec'][gnot1604][i]-crn['Dec'])**2)
    gAGN[i]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i]]*3600)
    RSO[i]=-crRS['RSoffset'][gnot1604][i]
for i in range(0,len(crRS_ACS['RA'])):
    tmpdist=np.sqrt((crRS_ACS['RA'][i]-crn['RA'])**2+(crRS_ACS['Dec'][i]-crn['Dec'])**2)
    gAGN[i+len(gnot1604)]=np.argsort(tmpdist)[0]
    if tmpdist[gAGN[i+len(gnot1604)]]>1./3600: print 'Too big! %f'%(tmpdist[gAGN[i+len(gnot1604)]]*3600)
    RSO[i+len(gnot1604)]=-crRS_ACS['RSoffset'][i]

for field in reffile_dict.keys():
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.5.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    crPI=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.P_inclus.7.1.16.dat'%(field,field,field))
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
    if field=='cl1604': 
        ACSmatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_ACS_comb.%s.dat'%(field,field,field,ldate)
        crmACS=np.loadtxt(matchcat,dtype=optmatchloaddict)
        ACSnumX=len(crmACS['indX'])
        ACSmras,ACSmdecs=crmACS['raopt1'],crmACS['decopt1']
        ACSnummatch=crmACS['nummatch']
        tmpcrm=np.loadtxt(matchcat,dtype=optmatchloaddict)
        crm=np.copy(crmACS)
        crm[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]=tmpcrm[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]
        usedACS=np.ones(ACSnumX,dtype='i8')
        usedACS[((ACSnummatch==0)&(tmpcrm['nummatch']>0))]=0
    else:
        crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    gq=np.where(crs['Q']>2.5)[0]
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field=='rxj0910':
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    #magB=cr['magaper_B']+cr['apercorr']

    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj0910':
        crrf=np.loadtxt(rfcat,dtype=rfdict0910)
    else:
        crrf=np.loadtxt(rfcat,dtype=rfdict)

    RFU,RFB=crrf['restflux_U'],crrf['restflux_B']
    mRFU,mRFB=cram['mRFU'],cram['mRFB']


    numsig=3
    gf=np.where(crRSfit['field']==field)[0][0]
    y0,m,sig=crRSfit['y0'][gf],crRSfit['m'][gf],crRSfit['sig'][gf]
    width=2*numsig*sig
    rso=(y0+m*(mRFB+adamcorrval)-(mRFU-mRFB))/(0.5*width)

    crCH=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.photz_inspeccov.4.23.16.dat'%(field,field,field),dtype='i8')
    inCH=crCH[:,4]
    
    gall=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]

    P_inclus=crPI
    gnew0=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(cram['Q']!=-1)&(cram['Q']<2.5)&(mRFB<-20.9)&(mRFB>-80))[0]
    gCH=np.where(inCH[gall]>=1)[0]
    gnew=np.where(inCH[gnew0]>=1)[0]
    gxray=np.where(cram['nummatch'][gnew0][gnew]>0)[0]
    print field,np.sum(P_inclus[gall]),np.sum(P_inclus[gnew0]),np.sum(P_inclus[gnew0][gnew]),np.sum(P_inclus[gall][gCH])
    gRS,gGV,gBC=np.where(-rso[gnew0][gnew]>=-1)[0],np.where((-rso[gnew0][gnew]<-1)&(-rso[gnew0][gnew]>=-3))[0],np.where(-rso[gnew0][gnew]<-3)[0]
    gRSx,gGVx,gBCx=np.where(-rso[gnew0][gnew][gxray]>=-1)[0],np.where((-rso[gnew0][gnew][gxray]<-1)&(-rso[gnew0][gnew][gxray]>=-3))[0],np.where(-rso[gnew0][gnew][gxray]<-3)[0]
    print 'RS: %.1f  GV: %.1f  BC: %.1f'%(np.sum(P_inclus[gnew0][gnew][gRS]),np.sum(P_inclus[gnew0][gnew][gGV]),np.sum(P_inclus[gnew0][gnew][gBC]))
    print 'RS: %.1f  GV: %.1f  BC: %.1f'%(np.sum(P_inclus[gnew0][gnew][gRSx]),np.sum(P_inclus[gnew0][gnew][gGVx]),np.sum(P_inclus[gnew0][gnew][gBCx]))

    for ix in gxray:
        print crpz['l68'][gnew0][gnew][ix],crpz['u68'][gnew0][gnew][ix],np.sum(P_inclus[gnew0][gnew][ix])

FILEl.close()
