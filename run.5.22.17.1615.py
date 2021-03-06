import numpy as np
import pyfits as py
import os
execfile('/home/rumbaugh/pythonscripts/angconvert.py')
execfile('/home/rumbaugh/pythonscripts/SphDist.py')
DB_path='/home/rumbaugh/var_database/Y3A1'
os.chdir(DB_path) 
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
POSSbands=np.array(['g','r','i'])
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

mac_thresh=5.

def POSS2SDSS(g,r,i):
    b_arr=np.array([b for b in [g,r,i]],dtype='object')
    for ib in range(0,len(b_arr)):
        if np.shape(b_arr[ib])!=():
            if len(b_arr[ib])>0: 
                b_arr[ib]=np.median(b_arr[ib])
            else:
                b_arr[ib]=0
    if (b_arr[0]!=0)&(b_arr[1]!=0):
        g,r=g+0.392*(b_arr[0]-b_arr[1])-0.28, r +0.127*(b_arr[0]-b_arr[1])+0.1
    else: 
        g,r=0,0
    if (b_arr[2]!=0)&(b_arr[1]!=0):   
        i=i+0.27*(b_arr[1]-b_arr[2])+0.32
    else:
        i=0
    return g,r,i

def DES2SDSS_gr(g,r):
    return (133625*g-9375*r-218)/124250.,(69.*g+925*r)/994.+516./62125.

def DES2SDSS_iz(i,z):
    return (-89*np.sqrt(-96000*i+96000*z+181561)+8000*z+37827)/8000.,(-17*np.sqrt(-96000*i+96000*z+181561)+24000*z+6731)/24000.

def make_cid_dict(incr,col='cid'):
    tdict={}
    for i,cid in zip(np.arange(0,len(incr)),incr[col]):
        try:
            tdict[cid]=np.append(tdict[cid],i)
        except KeyError:
            tdict[cid]=np.array([i])
    return tdict

fmt_dict={'i8': 'K','<i': 'D','i4': 'D','f8': 'E', '|S': 'A', 'int64': 'K', 'int32':'D','float64': 'E'}
def make_hdu(arr):
    colarr=[]
    for name in arr.dtype.names: 
        dfmt=np.str(arr.dtype[name])
        try:
            fmt=fmt_dict[dfmt]
        except KeyError:
            fmt=fmt_dict[dfmt[:2]]
        if fmt=='A': fmt='A%s'%dfmt[2:]
        colarr+=[py.Column(name=name,format=fmt,array=arr[name])]
    cols=py.ColDefs(colarr)
    tbhdu=py.BinTableHDU.from_columns(cols)
    return tbhdu

try:
    doload
except NameError:
    doload=True
if doload:
    cram=np.loadtxt('/home/rumbaugh/DR13_ALTMAGS.csv',dtype={'names':('thingid','objid','ra','dec','mjd_g','run','rerun','stripe','psfmag_u','psfmag_g','psfmag_r','psfmag_i','psfmag_z','psfmagerr_u','psfmagerr_g','psfmagerr_r','psfmagerr_i','psfmagerr_z','fibermag_u','fibermag_g','fibermag_r','fibermag_i','fibermag_z','fibermagerr_u','fibermagerr_g','fibermagerr_r','fibermagerr_i','fibermagerr_z','modelmag_u','modelmag_g','modelmag_r','modelmag_i','modelmag_z','modelmagerr_u','modelmagerr_g','modelmagerr_r','modelmagerr_i','modelmagerr_z'),'formats':('i8','i8','f8','f8','f8','i8','i8','|S8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1,delimiter=',')
    gam_dict={}
    for i in range(0,len(cram)):
        try:
            gam_dict[cram['thingid'][i]]=np.append(gam_dict[cram['thingid'][i]],i)
        except KeyError:
            gam_dict[cram['thingid'][i]]=np.array([i],dtype='i8')
    

    crac=np.loadtxt('/home/rumbaugh/all_coadd_object_ids_info.tab',dtype={'names':('cid','ra','dec','ind'),'formats':('i8','f8','f8','i8')},skiprows=1)
    cid_radec_dict={crac['cid'][x]: {'ra': crac['ra'][x], 'dec': crac['dec'][x]} for x in range(0,len(crac))}
    crat=np.loadtxt('/home/rumbaugh/DR13_THINGIDS_INFO.csv',dtype={'names':('tid','ra','dec','ind'),'formats':('i8','f8','f8','i8')},skiprows=1,delimiter=',')
    tid_radec_dict={crat['tid'][x]: {'ra': crat['ra'][x], 'dec': crat['dec'][x]} for x in range(0,len(crat))}


    hdubh=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
    bhdata=hdubh[1].data
    bhz,bhname=bhdata['REDSHIFT'],bhdata['SDSS_NAME']
    gbh_dict={bhname[x]: x for x in range(0,len(bhname))}

    bhRAdict,bhDECdict={bhname[x]: bhdata['RA'][x] for x in range(len(bhdata))},{bhname[x]: bhdata['DEC'][x] for x in range(len(bhdata))}

    crch=np.loadtxt('/home/rumbaugh/dr7_bh_y3a1_match_closechanges.csv',dtype={'names':('SDSSNAME','RA','DEC','HPIX','CID'),'formats':('|S24','f8','f8','i8','i8')},skiprows=1,delimiter=',')
    for i in range(0,len(crch)): crch['SDSSNAME'][i]=crch['SDSSNAME'][i].strip()

    double_count_indexes=np.zeros(0,dtype='|S30')

    crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DBID','CID','thingid','sdr7id','MQrownum','SPrownum','SDSSNAME'),'formats':('|S64','i8','i8','|S24','i8','i8','|S64')})

    crsp=np.loadtxt('/home/rumbaugh/sdss-poss_release.dat',dtype={'names':('ra','dec','plateID','EpochG','EpochR','EpochI','G_POSS','G_ERR','G_GOOD','R_POSS','R_ERR','R_GOOD','I_POSS','I_ERR','I_GOOD','SDR7ID','M_i','redshift','mbh','lbol','A_u','nobs','s82flag','mjd_r_SDSS','g_SDSS','g_ERR','r_SDSS','r_ERR','i_SDSS','i_ERR'),'formats':('f8','f8','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S12','f8','f8','|S12','|S12','|S12','|S12','|S12','f8','f8','f8','f8','f8','f8','f8')})
    spRAdict,spDECdict={crsp['SDR7ID'][x]: crsp['ra'][x] for x in range(0,len(crsp))},{crsp['SDR7ID'][x]: crsp['dec'][x] for x in range(0,len(crsp))}


    crmi=np.loadtxt('/home/rumbaugh/var_database/Y3A1/match_index.dat',dtype={'names':('MQ_ROWNUM','SP_ROWNUM','SDSS_NAME','RA','DEC','HPIX','COADD_OBJECTS_ID','TILENAME'),'formats':('i8','i8','|S32','f8','f8','i8','i8','|S32')},skiprows=1)
    gcrmi_match=np.where((crmi['COADD_OBJECTS_ID']>0)&((crmi['SP_ROWNUM']>-1)|(crmi['SDSS_NAME']!='-1')))[0]
    crmim=crmi[gcrmi_match]
    mihdu=make_hdu(crmi)

mastercr=np.zeros((len(crmim),),dtype={'names':('DatabaseID','Survey','Y3A1_CoaddObjectsID','DR13_thingid','sdr7id','SDSSNAME','SP_ROWNUM','FIRST_MJD','LAST_MJD','Redshift','Stripe82','RA_DES','DEC_DES','RA_SDSS','DEC_SDSS','RA_POSS','DEC_POSS','Epochs_DES_g','Epochs_DES_r','Epochs_DES_i','Epochs_DES_z','Epochs_DES_Y','Epochs_SDSS_g','Epochs_SDSS_r','Epochs_SDSS_i','Epochs_SDSS_z','Epochs_SDSS_u','med_DES_g','med_DES_r','med_DES_i','med_DES_z','med_DES_Y','med_SDSS_g','med_SDSS_r','med_SDSS_i','med_SDSS_z','med_SDSS_u','med_POSS_g','med_POSS_r','med_POSS_i','Y3A1TILE','OldDatabaseID'),'formats':('|S40','|S20','i8','i8','|S20','|S40','i8','f8','f8','f8','i8','f8','f8','f8','f8','f8','f8','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','<i4','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S40','|S40')})
mastercr['sdr7id'],mastercr['SDSSNAME'],mastercr['SP_ROWNUM']=-1,'-1',-1

for cid,MQrn,SPrn,SDSSNAME,imi,TILENAME in zip(crmim['COADD_OBJECTS_ID'],crmim['MQ_ROWNUM'],crmim['SP_ROWNUM'],crmim['SDSS_NAME'],np.arange(len(crmim)),crmim['TILENAME']):
    inSN=False
    outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
    Y3A1outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
    DR13outcr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
    oldDBID=None
    DBID=None
    if SDSSNAME!='-1':
        gbh=gbh_dict[SDSSNAME]
        try:
            BHRA,BHDEC=bhRAdict[SDSSNAME],bhDECdict[SDSSNAME]
            bhrah,bhram,bhras=deg2hms(BHRA)
            bhdecd,bhdecm,bhdecs=deg2dms(BHDEC)
            DBID='%02i%02i%02i%+03i%02i%02i'%(bhrah,bhram,bhras,bhdecd,bhdecm,int(bhdecs))
            if oldDBID==None:oldDBID='DR7BH%s'%SDSSNAME
        except KeyError:
            BHRA,BHDEC=0,0
    if SPrn!=-1:
        curdr7=crsp['SDR7ID'][SPrn]
        try:
            SPRA,SPDEC=spRAdict[curdr7],spDECdict[curdr7]
            sprah,spram,spras=deg2hms(SPRA)
            spdecd,spdecm,spdecs=deg2dms(SPDEC)
            if DBID==None:DBID='%02i%02i%02i%+03i%02i%02i'%(sprah,spram,spras,spdecd,spdecm,int(spdecs))
            if oldDBID==None:oldDBID='SDSSPOSS%s'%curdr7
        except KeyError:
            SPRA,SPDEC=0,0
    os.system('ln -sf %s %s'%(oldDBID,DBID))
    try:
        cr=np.loadtxt('%s/%s/LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    except IOError:
        cr=np.zeros((0,),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
    if np.shape(cr)==():
        mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
        outcr=np.zeros((1,),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
        outcr['Survey'],outcr['SurveyCoaddID'],outcr['SurveyObjectID'],outcr['RA'],outcr['DEC'],outcr['MJD'],outcr['TAG'],outcr['BAND'],outcr['MAGTYPE'],outcr['MAG'],outcr['MAGERR'],outcr['FLAG']=np.array([cr['Survey']]),np.array([cr['SurveyCoaddID']]),np.array([cr['SurveyObjectID']]),np.array([cr['RA']]),np.array([cr['DEC']]),np.array([cr['MJD']]),np.array([cr['TAG']]),np.array([cr['BAND']]),np.array([cr['MAGTYPE']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['FLAG']])
    else:
        outcr=np.zeros((len(cr),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
        outcr['Survey'],outcr['SurveyCoaddID'],outcr['SurveyObjectID'],outcr['RA'],outcr['DEC'],outcr['MJD'],outcr['TAG'],outcr['BAND'],outcr['MAGTYPE'],outcr['MAG'],outcr['MAGERR'],outcr['FLAG']=cr['Survey'],cr['SurveyCoaddID'],cr['SurveyObjectID'],cr['RA'],cr['DEC'],cr['MJD'],cr['TAG'],cr['BAND'],cr['MAGTYPE'],cr['MAG'],cr['MAGERR'],cr['FLAG']
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
    if len(outcr)>0: outcr['TAG'][outcr['SurveyObjectID']==0]='SN'
    try:
        crout=np.loadtxt('%s/%s/outliers.tab'%(DB_path,DBID),dtype='i8')
        #if len(crout)==len(outcr):
        #    outcr['OUTLIER']=crout
        #    outcr['OUTLIER'][(crout==0)&(outcr['BAND']=='g')]=-1
    except IOError:
        crout=np.zeros(len(cr))
    try:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DB_path,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('|S24','f8','f8','f8','|S4','f8','f8','i8')})
        outcrmac=np.zeros((len(crmac),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')})
        outcrmac['Survey'],outcrmac['SurveyCoaddID'],outcrmac['RA'],outcrmac['DEC'],outcrmac['MJD'],outcrmac['TAG'],outcrmac['BAND'],outcrmac['MAGTYPE'],outcrmac['MAG'],outcrmac['MAGERR'],outcrmac['FLAG']='SDSS',crmac['DatabaseID'],crmac['RA'],crmac['DEC'],crmac['MJD'],'MACLEOD',crmac['BAND'],'PSF',crmac['MAG'],crmac['MAGERR'],crmac['FLAG']
        try:
            croutmac=np.loadtxt('%s/%s/outliers_Macleod.tab'%(DB_path,DBID),dtype='i8')
            #outcrmac['OUTLIER']=croutmac
            #outcrmac['OUTLIER'][(croutmac==0)&(outcrmac['BAND']=='g')]=-1
        except IOError:
            croutmac=np.zeros(0)
        appmac_dict={}
        mac=True
        for b in ['g','r','i','z','u']:
            gb=np.where(bands==b)[0]
            gbmac=np.where(crmac['BAND']==b)[0]
            if len(gb)>0:
                gb0=np.where((cr['BAND']==b)&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0]
                if ((len(gb0)>0)&(len(gbmac)>0)):
                    mjd0,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
                    mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                    mindists=np.min(mjddists,axis=1)
                    gmac2=np.where(mindists>mac_thresh)[0]
                else:
                    gmac2=np.zeros(0,dtype='i8')
            else:
                gmac2=np.arange(len(gbmac))
            crappmac=np.zeros((len(gmac2),),dtype={'names':('Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG','UNIMAG'),'formats':('|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8','f8')})
            crappmac['Survey'],crappmac['SurveyCoaddID'],crappmac['RA'],crappmac['DEC'],crappmac['MJD'],crappmac['TAG'],crappmac['BAND'],crappmac['MAGTYPE'],crappmac['MAG'],crappmac['MAGERR']='SDSS',crmac['DatabaseID'][gbmac[gmac2]],crmac['RA'][gbmac[gmac2]],crmac['DEC'][gbmac[gmac2]],crmac['MJD'][gbmac[gmac2]],'MACLEOD',b,'PSF',crmac['MAG'][gbmac[gmac2]],crmac['MAGERR'][gbmac[gmac2]]
            #if len(crappmac)==len(croutmac): crappmac['OUTLIER']=croutmac[gbmac[gmac2]]
            appmac_dict[b]=crappmac
        crappmac=np.concatenate((appmac_dict['u'],appmac_dict['g'],appmac_dict['r'],appmac_dict['i'],appmac_dict['z']))
        #crappmac['OUTLIER'][(crappmac['OUTLIER']==0)&(crappmac['BAND']=='g')]=-1
        outcr=np.concatenate((outcr,crappmac))
    except IOError:
        crmac=np.zeros(0)
        mac=False
    try:
        crdes=np.loadtxt('%s/%s/DES_data.tab'%(DB_path,DBID),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')},skiprows=1)
        if np.shape(crdes)==():
            crdestmp=np.zeros((1,),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
            crdestmp['MJD'],crdestmp['IMAGEID'],crdestmp['OBJECTID'],crdestmp['COADD_OBJECTS_ID'],crdestmp['RA'],crdestmp['DEC'],crdestmp['MAG_AUTO'],crdestmp['MAGERR_AUTO'],crdestmp['MAG_PSF'],crdestmp['MAGERR_PSF'],crdestmp['BAND']=np.array([crdestmp['MJD']]),np.array([crdestmp['IMAGEID']]),np.array([crdestmp['OBJECTID']]),np.array([crdestmp['COADD_OBJECTS_ID']]),np.array([crdestmp['RA']]),np.array([crdestmp['DEC']]),np.array([crdestmp['MAG_AUTO']]),np.array([crdestmp['MAGERR_AUTO']]),np.array([crdestmp['MAG_PSF']]),np.array([crdestmp['MAGERR_PSF']]),np.array([crdestmp['BAND']])
            crdes=crdestmp
    except IndexError:
        try:
            crdes=np.loadtxt('%s/%s/DES_data.tab'%(DB_path,DBID),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8')},skiprows=1)
            if np.shape(crdes)==():
                crdestmp=np.zeros((1,),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
                crdestmp['MJD'],crdestmp['IMAGEID'],crdestmp['OBJECTID'],crdestmp['COADD_OBJECTS_ID'],crdestmp['RA'],crdestmp['DEC'],crdestmp['MAG_AUTO'],crdestmp['MAGERR_AUTO'],crdestmp['MAG_PSF'],crdestmp['MAGERR_PSF'],crdestmp['BAND']=np.array([crdestmp['MJD']]),np.array([crdestmp['IMAGEID']]),np.array([crdestmp['OBJECTID']]),np.array([crdestmp['COADD_OBJECTS_ID']]),np.array([crdestmp['RA']]),np.array([crdestmp['DEC']]),np.array([crdestmp['MAG_AUTO']]),np.array([crdestmp['MAGERR_AUTO']]),np.array([crdestmp['MAG_PSF']]),np.array([crdestmp['MAGERR_PSF']]),np.array(['None'])
            crdestmp=np.zeros((len(crdes),),dtype={'names':('MJD','IMAGEID','OBJECTID','COADD_OBJECTS_ID','RA','DEC','MAG_AUTO','MAGERR_AUTO','MAG_PSF','MAGERR_PSF','BAND'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','f8','f8','|S2')})
            crdestmp['MJD'],crdestmp['IMAGEID'],crdestmp['OBJECTID'],crdestmp['COADD_OBJECTS_ID'],crdestmp['RA'],crdestmp['DEC'],crdestmp['MAG_AUTO'],crdestmp['MAGERR_AUTO'],crdestmp['MAG_PSF'],crdestmp['MAGERR_PSF'],crdestmp['BAND']=crdestmp['MJD'],crdestmp['IMAGEID'],crdestmp['OBJECTID'],crdestmp['COADD_OBJECTS_ID'],crdestmp['RA'],crdestmp['DEC'],crdestmp['MAG_AUTO'],crdestmp['MAGERR_AUTO'],crdestmp['MAG_PSF'],crdestmp['MAGERR_PSF'],np.full(len(crdes),'None',dtype='|S4')
            crdes=crdestmp
        except IOError:
            crdes=np.zeros(0)
    except IOError:
        crdes=np.zeros(0)
    prihdr = py.Header()
    prihdr['DatabaseID']=DBID
    prihdr['OldDatabaseID']=oldDBID
    prihdu = py.PrimaryHDU(header=prihdr)
    outcr=outcr[np.argsort(outcr['MJD'])]
    lchdu=make_hdu(outcr)
    hdulistarr=[prihdu,lchdu]
    macind,desind=99,99
    curind=2
    if mac:
        machdu=make_hdu(outcrmac)
        hdulistarr+=[machdu]
        macind=curind
        curind+=1
    if len(crdes)>0:
        deshdu=make_hdu(crdes)
        hdulistarr+=[deshdu]
        desind=curind
        curind+=1
    for surv in np.unique(outcr['Survey']):
        mastercr['RA_%s'%surv][imi]=np.median(outcr['RA'][outcr['Survey']==surv])
        mastercr['DEC_%s'%surv][imi]=np.median(outcr['DEC'][outcr['Survey']==surv])
        tdists=SphDist(mastercr['RA_%s'%surv][imi],mastercr['DEC_%s'%surv][imi],outcr['RA'][outcr['Survey']==surv],outcr['DEC'][outcr['Survey']==surv])/60.
        if np.sort(tdists)[0]>1:
            if mastercr['RA_%s'%surv][imi]>180: 
                mastercr['RA_%s'%surv][imi]-=180
            else:
                mastercr['RA_%s'%surv][imi]+=180
            tdists=SphDist(mastercr['RA_%s'%surv][imi],mastercr['DEC_%s'%surv][imi],outcr['RA'][outcr['Survey']==surv],outcr['DEC'][outcr['Survey']==surv])/60.
            if np.sort(tdists)[0]>1: print 'median coords for %s,%s still messed up'%(DBID,surv)
        if mastercr['Survey'][imi]=='':
            mastercr['Survey'][imi]=surv
        else:
            mastercr['Survey'][imi]='%s;%s'%(mastercr['Survey'][imi],surv)
    if SPrn!=-1:
        mastercr['Redshift'][imi]=crsp['redshift'][SPrn]
    if SDSSNAME!='-1':
        mastercr['Redshift'][imi]=bhz[gbh]
    if len(outcr)>0:
        mastercr['LAST_MJD'][imi],mastercr['FIRST_MJD'][imi]=np.max(outcr['MJD']),np.min(outcr['MJD'])
        for b in np.unique(outcr['BAND'][outcr['Survey']=='DES']):
            mastercr['Epochs_DES_%s'%b][imi]=len(outcr[(outcr['Survey']=='DES')&(outcr['BAND']==b)])
            mastercr['med_DES_%s'%b][imi]=np.median(outcr['MAG'][(outcr['Survey']=='DES')&(outcr['BAND']==b)])
        for b in np.unique(outcr['BAND'][outcr['Survey']=='SDSS']):
            mastercr['Epochs_SDSS_%s'%b][imi]=len(outcr[(outcr['Survey']=='SDSS')&(outcr['BAND']==b)])
            mastercr['med_SDSS_%s'%b][imi]=np.median(outcr['MAG'][(outcr['Survey']=='SDSS')&(outcr['BAND']==b)])
        for b in np.unique(outcr['BAND'][outcr['Survey']=='POSS']):
            mastercr['med_POSS_%s'%b][imi]=np.median(outcr['MAG'][(outcr['Survey']=='POSS')&(outcr['BAND']==b)])
    sdsscr,sdssind=np.zeros(0),-1
    if 'SDSS' in outcr['Survey']:
        tidcr=np.array(outcr['SurveyCoaddID'][(outcr['Survey']=='SDSS')&(outcr['SurveyObjectID']!='0')&(outcr['TAG']!='MACLEOD')],dtype='i8')
        if len(tidcr)>0:
            mastercr['DR13_thingid'][imi]=np.max(tidcr)
            try:
                sdsscr=cram[gam_dict[mastercr['DR13_thingid'][imi]]]
                sdsshdu=make_hdu(sdsscr)
                hdulistarr+=[sdsshdu]
                sdssind=curind
                curind+=1
            except KeyError:
                pass
        try:
            mastercr['RA_SDSS'][imi],mastercr['DEC_SDSS'][imi]=tid_radec_dict[mastercr['DR13_thingid'][imi]]['ra'],tid_radec_dict[mastercr['DR13_thingid'][imi]]['dec']
        except KeyError:
            pass
    if 'POSS' in outcr['Survey']:mastercr['sdr7id'][imi]=crsp['SDR7ID'][SPrn]
    mastercr['DatabaseID'][imi],mastercr['OldDatabaseID'][imi],mastercr['Y3A1_CoaddObjectsID'][imi],mastercr['SDSSNAME'][imi],mastercr['SP_ROWNUM'][imi],mastercr['Y3A1TILE'][imi]=DBID,oldDBID,cid,SDSSNAME,SPrn,TILENAME
    try:
        mastercr['RA_DES'][imi],mastercr['DEC_DES'][imi]=cid_radec_dict[mastercr['Y3A1_CoaddObjectsID'][imi]]['ra'],cid_radec_dict[mastercr['Y3A1_CoaddObjectsID'][imi]]['dec']
    except KeyError:
        pass
    if 'S82' in outcr['TAG']: mastercr['S82'][imi]=1

    thdulist = py.HDUList(hdulistarr)
    thdulist[1].header['LIGHTCURVE']='MERGED'
    
    if desind<99:
        thdulist[desind].header['COADD_OBJECT_ID']=cid
        thdulist[desind].header['LIGHTCURVE']='DES'
    if mac:
        thdulist[macind].header['LIGHTCURVE']='MACLEOD'
    if sdssind!=-1:
        thdulist[sdssind].header['THINGID']=mastercr['DR13_thingid'][imi]
        thdulist[sdssind].header['LIGHTCURVE']='SDSS'
    try:
        thdulist.writeto('%s/%s/LC.fits'%(DB_path,DBID),clobber=True)
    except IOError:
        print 'IOError for %s,%s'%(DBID,oldDBID)

masterhdu=make_hdu(mastercr)

prihdu = py.PrimaryHDU()
hdulistarr=[prihdu,masterhdu,mihdu]
thdulist = py.HDUList(hdulistarr)
thdulist.writeto('%s/masterfile.fits'%(DB_path),clobber=True)
