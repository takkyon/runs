import numpy as np
from ConcaveHull import ConcaveHull,CheckPoints
from shapely.geometry import box as makebox
import matplotlib.pyplot as plt
alpha_ref,alphaX = 11.1,1.1
execfile('/home/rumbaugh/set_spec_dict.py')
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/setup_adam_cats.py')

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053","cl1324_north","cl1324_south"])

mtol=1.
ldate='1.19.16'
pldate='4.21.16'

crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13]*3.086E22
DM=crcc[:,15]
kpc=crcc[:,12]
cc_z=crcc[:,0]

#for field in reffile_dict.keys():
for field in ['cl1324']:
    cram=np.loadtxt('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.5.5.16.dat'%(field,field,field),dtype={'names':('ID_adam','RA_phot','Dec_phot','z_peak','flag','ID_spec','RA_spec','Dec_spec','z_spec','z_spec_adam','Q','ID_xray','RA_xray','Dec_xray','nummatch','ID_xray_adam','RA_xray_adam','Dec_xray_adam','nummatch_adam','mRFU','mRFB'),'formats':('|S24','f8','f8','f8','f8','|S24','f8','f8','f8','f8','i8','|S24','f8','f8','i8','|S24','f8','f8','i8','f8','f8')})
    FILE=open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s.adammatch.7.5.16.dat'%(field,field,field),'w')
    FILE.write('# ID_adam RA_phot Dec_phot z_peak flag ID_spec RA_spec Dec_spec z_spec z_spec_adam Q ID_xray RA_xray Dec_xray nummatch ID_xray_adam RA_xray_adam Dec_xray_adam nummatch_adam restframe_M_U restframe_M_B   for flag: 0=outside spec coverage,1=inside spec coverage,2=new source\n') 
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_comb.%s.dat'%(field,field,field,ldate)
    if field=='cl1604': 
        ACSmatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_ACS_comb.%s.dat'%(field,field,field,ldate)
        crmACS=np.loadtxt(ACSmatchcat,dtype=optmatchloaddict)
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

    adammatchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_photz.%s.dat'%(field,field,field,pldate)
    crma=np.loadtxt(adammatchcat,dtype=optmatchloaddict)
    ID_adammatch=np.array(crma['optID1'],dtype='i8')
    crs=np.loadtxt('%s/%s'%(spec_dict['basepath'],spec_dict[field]['file']),dtype=specloaddict)
    ra_opt,dec_opt=crs['ra'],crs['dec']
    gq=np.where((crs['Q']>2.5)&(crs['z']>spec_dict[field]['z'][1])&(crs['z']<spec_dict[field]['z'][2]))[0]
    fz0,fzl,fzu=spec_dict[field]['z'][0],spec_dict[field]['z'][1],spec_dict[field]['z'][2]
    refcat='%s/%s/%s.mag.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if field=='rxj1821':
        cr=np.loadtxt(refcat,dtype=refdict_1821)
    elif field=='rxj0910':
        cr=np.loadtxt(refcat,dtype=refdict0910)
    else:
        cr=np.loadtxt(refcat,dtype=refdict)
    #outtmp=np.zeros((np.shape(cr)[0],4))
    #outtmp[:,3],outtmp[:,0],outtmp[:,1],outtmp[:,2]=cr['ID'],cr['ra'],cr['dec'],cr['magaper_i']+cr['apercorr']
    #magB=cr['magaper_B']+cr['apercorr']

    pzcat='%s/%s/%s.zout.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    crpz=np.loadtxt(pzcat,dtype=pzdict)
    rfcat='%s/%s/%s.restframe.gz'%(refdir,reffile_dict[field],reffile_dict[field])
    if ((field=='rxj0910')|(field=='cl1324')):
        crrf=np.loadtxt(rfcat,dtype=rfdict0910)
    else:
        crrf=np.loadtxt(rfcat,dtype=rfdict)

    RFU,RFB,RFV,RFJ,RFNUV=crrf['restflux_U'],crrf['restflux_B'],crrf['restflux_V'],crrf['restflux_J'],crrf['restflux_NUV']
    mRFU,mRFB=cram['mRFU'],cram['mRFB']
    mRFV,mRFJ,mRFNUV=np.ones(len(RFU))*99,np.ones(len(RFU))*99,np.ones(len(RFU))*99
    gdls=np.zeros(len(mRFV),dtype='i8')
    for igdl in range(0,len(gdls)):
        gdl=np.argsort(np.abs(crpz['z_peak'][igdl]-cc_z))[0]
        gdls[igdl]=gdl
    mRFV[RFV>0],mRFJ[RFJ>0],mRFNUV[RFNUV>0]=-2.5*np.log10(RFV[RFV>0])+25-DM[gdls][RFV>0],-2.5*np.log10(RFJ[RFJ>0])+25-DM[gdls][RFJ>0],-2.5*np.log10(RFNUV[RFNUV>0])+25-DM[gdls][RFNUV>0]
    #CKP_arr=np.zeros(len(RFU),dtype='bool')
    #match_arr_spec,match_arr_xray=np.ones(len(RFU),dtype='i8')*-1,np.ones(len(RFU),dtype='i8')*-1
    #for i in range(0,len(RFU)):
    #    zx,zs=crpz['z_peak'][i],crpz['z_peak']
    #    gnoz=np.where((np.abs(cr['ra'][i]-cr['ra'])*np.cos(cr['dec'][i]*np.pi/180)<20./3600)&(np.abs(cr['dec'][i]-cr['dec'])<20./3600))[0]
    #    if ((len(gnoz)>1)&(zx>0.01)):
    #        tmpdist=60*SphDist(cr['ra'][i],cr['dec'][i],cr['ra'][gnoz],cr['dec'][gnoz])*kpc[gdls[i]]
    #        tmpzdist=np.abs(((1+zx)**2-(1+zs[gnoz])**2)/((1+zx)**2+(1+zs[gnoz])**2))*3.*10.**5
    #        gCKP=np.where((tmpdist<70)&(tmpzdist<350))[0]
    #        if len(gCKP)>1: CKP_arr[i]=1
    #    gnoz=np.where((np.abs(cr['ra'][i]-ra_opt)*np.cos(cr['dec'][i]*np.pi/180)<mtol/3600)&(np.abs(cr['dec'][i]-dec_opt)<mtol/3600))[0]
    #    if len(gnoz)>0:
    #        tmpdist=60*SphDist(cr['ra'][i],cr['dec'][i],ra_opt[gnoz],dec_opt[gnoz])
    #        if len(gnoz)>1:
    #            gtmpdist=np.argsort(tmpdist)[0]
    #            match_arr_spec[i]=gnoz[gtmpdist]
    #        else:
    #            match_arr_spec[i]=gnoz[0]
    #    gnoz=np.where((np.abs(cr['ra'][i]-crm['raopt1'])*np.cos(cr['dec'][i]*np.pi/180)<mtol/3600)&(np.abs(cr['dec'][i]-crm['decopt1'])<mtol/3600))[0]
    #    if len(gnoz)>0:
    #        tmpdist=60*SphDist(cr['ra'][i],cr['dec'][i],crm['raopt1'][gnoz],crm['decopt1'][gnoz])
    #        if len(gnoz)>1:
    #            gtmpdist=np.argsort(tmpdist)[0]
    #            match_arr_xray[i]=gnoz[gtmpdist]
    #        else:
    #            match_arr_xray[i]=gnoz[0]
    
    #gall=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]
    #gall=np.where((crpz['z_peak']>=fzl)&(crpz['z_peak']<=fzu)&(cr['use']==1)&(mRFB<-20.9)&(mRFB>-80))[0]
    #gnew0=np.where((crpz['z_peak']>=fzl)&(crpz['z_peak']<=fzu)&(cr['use']==1)&(cr['z_spec']<0)&(mRFB<-20.9)&(mRFB>-80))[0]
    #gnew0=np.where((crpz['u99']>=fzl)&(crpz['l99']<=fzu)&(cr['use']==1)&(cr['z_spec']<0)&(mRFB<-20.9)&(mRFB>-80))[0]
    #CH_ref = np.zeros((len(ra_opt),2))
    #CH_ref[:,0],CH_ref[:,1]=ra_opt,dec_opt
    #CHull_ref,edges_ref=ConcaveHull(CH_ref,alpha_ref)
    #gCH=CheckPoints(CHull_ref,cr['ra'][gall],cr['dec'][gall])
    #gnew=np.where(cr['z_spec'][gall][gCH]<0)[0]
    #print field,len(gnew),len(gCH),np.sum(CKP_arr),np.sum(CKP_arr[gall][gCH])
    #flag=np.ones(len(RFU),dtype='i8')*-1
    #flag[gall]=0
    #flag[gall][gCH]=1
    #flag[gall][gCH][gnew]=2

    for i in range(0,len(RFU)):
s        ID_spec,ra_spec,dec_spec,z_spec_tmp,Q_tmp,ID_xray,rax,decx,nm,ID_xray_adam,rax_adam,decx_adam,nm_adam=cram['ID_spec'][i],cram['RA_spec'][i],cram['Dec_spec'][i],cram['z_spec'][i],cram['Q'][i],cram['ID_xray'][i],cram['RA_xray'][i],cram['Dec_xray'][i],cram['nummatch'][i],cram['ID_xray_adam'][i],cram['RA_xray_adam'][i],cram['Dec_xray_adam'][i],cram['nummatch_adam'][i]
        #if match_arr_spec[i]>=0:
        #    ga=match_arr_spec[i]
        #    ID_spec,ra_spec,dec_spec,z_spec_tmp,Q_tmp=crs['ID'][ga],crs['ra'][ga],crs['dec'][ga],crs['z'][ga],crs['Q'][ga]
        #if match_arr_xray[i]>=0:
        #    ga=match_arr_xray[i]
        #    ID_xray,rax,decx,nm=crm['indX'][ga],crm['raX'][ga],crm['decX'][ga],crm['nummatch'][ga]
        #if cr['ID'][i] in ID_adammatch:
        #    gid=np.where(cr['ID'][i]==ID_adammatch)[0]
        #    if len(gid)>1: gid=gid[0]
        #    ID_xray_adam,rax_adam,decx_adam,nm_adam=crma['indX'][gid],crma['raX'][gid],crma['decX'][gid],crma['nummatch'][gid]
        FILE.write('%6s %9.5f %9.5f %9.6f %2f %16s %9.5f %9.5f %9.6f %9.6f %2i %4s %9.5f %9.5f %i %6s %9.5f %9.5f %i %f %f %f %f %f\n'%(cr['ID'][i],cr['ra'][i],cr['dec'][i],crpz['z_peak'][i],cram['flag'][i],ID_spec,ra_spec,dec_spec,z_spec_tmp,cr['z_spec'][i],Q_tmp,ID_xray,rax,decx,nm,ID_xray_adam,rax_adam,decx_adam,nm_adam,mRFU[i],mRFB[i],mRFV[i],mRFJ[i],mRFNUV[i]))
    FILE.close()
