import numpy as np
execfile('/home/rumbaugh/pythonscripts/SphDist.py')

outlier_window,outlier_thresh,mac_thresh=100,0.5,5

DB_path='/home/rumbaugh/var_database/Y3A1'
outputdir=DB_path
DBdir=DB_path
#crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/database_index.dat',dtype={'names':('DatabaseID','Y3A1_COADD_OBJECTS_ID','SDSSNAME'),'formats':('|S64','|S64','|S64')},usecols=(0,1,6))
crmcm=np.loadtxt('/home/rumbaugh/var_database/Y3A1/DR7_Macleod_S82_match.dat',dtype={'names':('DBID','MCID'),'formats':('|S24','i8')},skiprows=1)


crmcm=crmcm[crmcm['MCID']>-1]

#name_prefs=np.array(crdb['DatabaseID'],dtype='|S2')
#crdb=crdb[name_prefs=='DR']

crdb=np.loadtxt('/home/rumbaugh/var_database/Y3A1/databaseIDs.dat',dtype={'names':('DatabaseID','DBIDS','MQrownum','SP_rownum','sdr7id','thingid','SDSSNAME','CID','TILENAME'),'formats':('|S32','|S128','i8','i8','|S24','i8','|S64','i8','|S32')},skiprows=1)
gdbids=np.array(['MQ206171','MQ208717','MQ213230','MQ209259','MQ212075','MQ211918','MQ214934','MQ214802','MQ214532','MQ215548','MQ216346'])
crdb=crdb[np.in1d(crdb['DatabaseID'],gdbids)]
maxdrop=np.zeros(len(crdb))
s82flag=np.zeros(len(crdb))
surveys_max=np.zeros((len(crdb),2),dtype='|S8')
baseline_max=np.zeros(len(crdb))

crdb=np.loadtxt('/home/rumbaugh/radecname_forSDSScutouts_fardbid.4.18.17.csv',dtype={'names':('ra','dec','DatabaseID'),'formats':('f8','f8','|S36')},delimiter=',')

for DBIDtmp in crdb['DatabaseID']:
    DBID=DBIDtmp[:-11]
    cr=np.loadtxt('%s/%s/LC.tab'%(outputdir,DBID),dtype={'names':('DatabaseID','Survey','SurveyCoaddID','SurveyObjectID','RA','DEC','MJD','TAG','BAND','MAGTYPE','MAG','MAGERR','FLAG'),'formats':('|S64','|S20','|S20','|S20','f8','f8','f8','|S20','|S12','|S12','f8','f8','i8')},skiprows=1)
    if np.shape(cr)==(0,): 
        print 'No LC.tab for %s'%DBID
        continue
    elif np.shape(cr)==():
        outlier_arr=np.zeros(1,dtype='bool')
        gorig=np.zeros(1,dtype='i8')[(np.array([cr['MAG']])>14)&(np.array([cr['MAG']])<30)&(np.array([cr['MAGERR']])<5)&(np.array([cr['Survey']])!='POSS')]
    else:
        outlier_arr=np.zeros(len(cr),dtype='bool')
        gorig=np.arange(len(cr))[(cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)&(cr['Survey']!='POSS')]
    ggood=np.where((cr['MAG']>14)&(cr['MAG']<30)&(cr['MAGERR']<5)&(cr['Survey']!='POSS'))[0]#&(cr['FLAG']<16))[0]
    gmc=np.where(DBID==crmcm['DBID'])[0]
    if len(gmc)>0:
        crmac=np.loadtxt('%s/%s/Macleod_LC.tab'%(DBdir,DBID),dtype={'names':('DatabaseID','RA','DEC','MJD','BAND','MAG','MAGERR','FLAG'),'formats':('i8','f8','f8','f8','|S4','f8','f8','i8')})
        outlier_mac_arr=-np.ones(len(crmac),dtype='i8')
        gorigmac=np.arange(len(crmac))[(crmac['MAG']>14)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
        crmac=crmac[(crmac['MAG']>14)&(crmac['MAG']<30)&(crmac['MAGERR']<5)]
        gbmac=np.where(crmac['BAND']=='g')[0]
        if len(gbmac)<=0: 
            maclen=0
            gmac2=np.arange(0)
    else:
        maclen=0
        gmac2,gbmac,gorigmac=np.arange(0),np.arange(0),np.arange(0)
        outlier_mac_arr=np.zeros(0,dtype='bool')
    #SNflag=False
    if np.shape(cr)==():
        if len(ggood)<1:
            mydblen=0
            gb0=np.zeros(0,dtype='i8')
            if len(gmc)>0:
                if len(gbmac)>0:
                    cr=crmac[gbmac]
                    gmac2=np.arange(len(gbmac))
                    maclen=len(cr)
                    mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.full(len(cr),'SDSS')
                    gb=np.where(bands=='g')[0]
                else:
                    gb=np.zeros(0,dtype='i8')
            else:
                gb=np.zeros(0,dtype='i8')
        else:
            mjd,mag,magerr,bands,survey=np.array([cr['MJD']]),np.array([cr['MAG']]),np.array([cr['MAGERR']]),np.array([cr['BAND']]),np.array([cr['Survey']])
            gb=np.where(bands=='g')[0]
            if len(gb)==0:
                mjd,mag,magerr,bands,survey=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0,dtype='|S4'),np.zeros(0,dtype='|S4')
                mydblen=0
            else:
                mydblen=1
            if ((len(gmc)>0)&(len(gb)>0)):
                gb0=np.where((mjd>np.min(crmac['MJD'])-30)&(mjd<np.max(crmac['MJD'])+30))[0]    
                if ((len(gb0)>0)&(len(gbmac)>0)):
                    mjd0,mjdmac=mjd[gb0],mjd[gbmac]
                    mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                    mindists=np.min(mjddists,axis=1)
                    gmac2=np.where(mindists>mac_thresh)[0]
                else:
                    gmac2=np.arange(len(gbmac))
                surveymac=np.zeros(len(gmac2),dtype='|S8')
                surveymac[:]='SDSS'
                mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
                maclen=len(gmac2)
            elif ((len(gmc)>0)&(len(gb)==0)):
                gmac2=np.arange(len(gbmac))
                mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
                maclen=len(mjd)
            gb=np.where(bands=='g')[0]
    else:
        cr=cr[ggood]
        gb=np.where(cr['BAND']=='g')[0]
        cr=cr[gb]
        gorig=gorig[gb]
        mydblen=len(gb)    
        mjd,mag,magerr,bands,survey=cr['MJD'],cr['MAG'],cr['MAGERR'],cr['BAND'],cr['Survey']
        if len(gmc)>0:
            gb0=np.where((cr['BAND']=='g')&(cr['MJD']>np.min(crmac['MJD'])-30)&(cr['MJD']<np.max(crmac['MJD'])+30))[0]    
            if ((len(gb0)>0)&(len(gbmac)>0)):
                mjd0,mjdmac=cr['MJD'][gb0],crmac['MJD'][gbmac]
                mjddists=np.abs(mjdmac.reshape((len(mjdmac),1))-mjd0.reshape((1,len(mjd0)))*np.ones((len(mjdmac),1)))
                mindists=np.min(mjddists,axis=1)
                gmac2=np.where(mindists>mac_thresh)[0]
            else:
                gmac2=np.arange(len(gbmac))
            surveymac=np.zeros(len(gmac2),dtype='|S8')
            surveymac[:]='SDSS'
            mjd,mag,magerr,bands,survey=np.append(mjd,crmac['MJD'][gbmac[gmac2]]),np.append(mag,crmac['MAG'][gbmac[gmac2]]),np.append(magerr,crmac['MAGERR'][gbmac[gmac2]]),np.append(bands,crmac['BAND'][gbmac[gmac2]]),np.append(survey,surveymac)
            maclen=len(gmac2)
        gb=np.where(bands=='g')[0]
        #if len(cr)>1:
        #    initdists=SphDist(cr['RA'][0],cr['DEC'][0],cr['RA'][1:],cr['DEC'][1:])
        #    if np.max(initdists)>0.3: SNflag=True
    if maclen>0:outlier_mac_arr[gorigmac[gbmac[gmac2]]]=0
    print 'len(gb)=%i'%len(gb)
    if len(gb)>0:
        for ipt in np.arange(len(gb)):
            gthresh=np.where(np.abs(mjd[gb]-mjd[gb[ipt]])<outlier_window)[0]
            if len(gthresh)>1:
                if ipt<mydblen:
                    outlier_arr[gorig[gb[ipt]]]= np.abs(np.median(mag[gb[gthresh]])-mag[gb[ipt]]) > outlier_thresh
                else:
                    outlier_mac_arr[gorigmac[gbmac[gmac2[ipt-mydblen]]]]= np.abs(np.median(mag[gb[gthresh]])-mag[gb[ipt]]) > outlier_thresh
        print 'Saving outlier.tab for %s'%DBID
        np.savetxt('%s/%s/outliers.tab'%(DBdir,DBID),outlier_arr,fmt='%2i')
        if maclen>0:np.savetxt('%s/%s/outliers_Macleod.tab'%(DBdir,DBID),outlier_mac_arr,fmt='%2i')
