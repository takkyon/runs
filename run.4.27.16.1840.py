import numpy as np
import os
import matplotlib.pyplot as plt
import pyfits as py
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/SphDist.py')
ldate='1.19.16'
date='4.27.16'

crclus=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','name','RA','Dec'),'formats':('|S24','|S24','f8','f8')})
crclusfield=crclus['field']
for i in range(0,len(crclusfield)): crclusfield[i]=crclusfield[i].lower()

outfile='/home/rumbaugh/match_catalog.cl0023+rxj1716.%s.dat'%date
FILE=open(outfile,'w')
FILE.write('# field Xray_ID RA Dec flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit bcnts_soft bcnts_hard bcnts_full sig_soft sig_hard sig_full\n')

stol=1./3600.
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f8','i8')}
ACSspecloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q','OLDIDs','PHOT_FLAGS','ACS_RA','ACS_DEC','ACS_ID','F606W','F814W'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f8','i8','|S24','|S24','f8','f8','f8','f8','f8')}
zfull=np.zeros(0)

spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.feb2016.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9404,9836,9840]}, \
             'cl1324_north': {'file': 'FINAL.cl1322.lrisplusdeimos.feb2016.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9840]}, \
             'cl1324_south': {'file': 'FINAL.cl1322.lrisplusdeimos.feb2016.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9404,9836]}, \
             'rxj1821': {'file': 'FINAL.nep5281.deimos.gioia.aug2013.nodups.cat', 'loaddict': '','z':[0.818,0.8,0.83], 'obsids': [10444,10924]}, \
             'cl0849': {'file': 'FINAL.onlysemifinal.autocompile.blemaux.0849.feb2013.nodups.cat', 'loaddict': '','z':[1.261,1.25,1.28], 'obsids': [927,1708]}, \
             'X3': {'file': 'FINAL.semifinal.spectroscopic.autocompile.blemaux.XL005.targetsonly.apr2014.cat', 'loaddict': '','z':[1.050,1,1.1], 'obsids': []}, \
             'cl0023': {'file': 'FINAL.SG0023.deimos.lris.feb2012.nodups.cat', 'loaddict': '','z':[0.845,0.82,0.87], 'obsids': [7914]}, \
             'X5': {'file': 'FINAL.spectra.Cl0023.edit.cat', 'loaddict': '','z':[0.845,0.82,0.87], 'obsids': []}, \
             'cl1604': {'file': 'FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.cat', 'loaddict': '','z':[0.900,0.84,0.96], 'obsids': [6932,6933,7343]}, \
             'cl1350': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1350.dec2015.nodups.cat', 'loaddict': '','z':[0.804,0.79,0.81], 'obsids': [2229]}, \
             'X7': {'file': 'FINAL.spectroscopic.autocompile.blemaux.1429.may2015.nodups.cat', 'loaddict': '','z':[0.985,0.97,1.], 'obsids': []}, \
             'X8': {'file': 'FINAL.spectroscopic.autocompile.blemaux.N2560.apr2012.nodups.cat', 'loaddict': '','z':[0,0,0], 'obsids': []}, \
             'rcs0224': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RCS0224.apr2012.nodups.cat', 'loaddict': '','z':[0.772,0.76,0.79], 'obsids': [3181,4987]}, \
             'rxj1221': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1221.dec2015.nodups.cat', 'loaddict': '','z':[0.700,0.69,0.71], 'obsids': [1662]}, \
             'rxj1716': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1716.jul2015.nodups.cat', 'loaddict': '','z':[0.813,0.8,0.83], 'obsids': [548]}, \
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.feb2016.plusT08.nodups.cat', 'loaddict': '','z':[1.110,1.08,1.15], 'obsids': [2227,2452]}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':[0.691,0.68,0.71], 'obsids': [10443,11999]}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':[0,0,0], 'obsids': []}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':[0.959,0.94,0.97], 'obsids': [4161]}, \
             'rxj1053': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1053.feb2016.nodups.cat', 'loaddict': '','z':[1.140,1.1,1.15], 'obsids': [4936]}}

optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])

tol=0.2

#for field in ['cl1604']: 
for field in ['cl0023','rxj1716']: 
    gcrc=np.where(field==crclusfield)[0]
    if field != 'cl1604':
        try:
            cr_op=np.loadtxt('/home/rumbaugh/Chandra/%s/photometry/%s.xray_phot.soft_hard_full.dat'%(obsid_dict[field],obsid_dict[field]))
        except:
            cr_op=[]
    else:
        crtmp1,crtmp2=np.loadtxt('/home/rumbaugh/Chandra/6932/photometry/6932.xray_phot.soft_hard_full.dat'),np.loadtxt('/home/rumbaugh/Chandra/6933+7343/photometry/6933+7343.xray_phot.soft_hard_full.dat')
        cr_op=np.append(crtmp1,crtmp2,axis=0)
    try:
        oldra,olddec,oldfluxS,oldfluxH,oldfluxF,oldncntsS,oldncntsH,oldncntsF=cr_op[:,0],cr_op[:,1],cr_op[:,2],cr_op[:,3],cr_op[:,4],cr_op[:,5],cr_op[:,6],cr_op[:,7]
    except:
        oldra,olddec,oldfluxS,oldfluxH,oldfluxF,oldncntsS,oldncntsH,oldncntsF=np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0),np.zeros(0)
    crp=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/%s_srclist_v1.fits'%(field,field,field))
    pdata=crp[1].data
    if field=='rxj1221':
        crs=np.loadtxt('/home/rumbaugh/Chandra/speccats/tmpfix.%s'%spec_dict[field]['file'],dtype=specloaddict)
    elif field=='cl1604':
        crs=np.loadtxt('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file'],dtype=ACSspecloaddict)
    else:
        crs=np.loadtxt('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file'],dtype=specloaddict)
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
    numX=len(crm['indX'])
    mras,mdecs=crm['raopt1'],crm['decopt1']
    nummatch=crm['nummatch']
    zcur,magrcur,magicur,magzcur,zerrcur,qcur=-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99.*np.ones(numX),-99*np.ones(numX,dtype='i8')
    maskcur,slitcur=np.zeros(numX,dtype='|S64'),np.zeros(numX,dtype='|S64')
    all_ra,all_decs=crs['ra'][crs['Q']>2.5],crs['dec'][crs['Q']>2.5]
    matched_ncntsS,matched_ncntsH,matched_ncntsF,matched_fluxS,matched_fluxH,matched_fluxF = np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX),np.zeros(numX)
    for j in range(0,len(crm['indX'])):
        g_old=np.where((np.abs(mras[j]-oldra)/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-olddec)<stol))[0]
        if len(g_old)!=0: 
            disttmp=SphDist(mras[j],mdecs[j],oldra[g_old],olddec[g_old])
            gas=np.argsort(disttmp)
            g_old=g_old[gas[:1]]
            matched_ncntsS[j],matched_ncntsH[j],matched_ncntsF[j],matched_fluxS[j],matched_fluxH[j],matched_fluxF[j]=oldncntsS[g_old],oldncntsH[g_old],oldncntsF[g_old],oldfluxS[g_old],oldfluxH[g_old],oldfluxF[g_old]
        gz=np.where((crs['ID']==crm['optID1'][j]))[0]
        if field=='cl1604':
            if usedACS[j]: gz=np.where((crs['ACS_ID']==crm['optID1'][j]))[0]
        if len(gz)==0:
            try:
                if field=='rxj1757':
                    gz=np.where(crs['ID']=='F%05i'%(int(crm['optID1'][j])-1))[0]
                else:
                    gz=np.where(crs['ID']=='F%05i'%int(crm['optID1'][j]))[0]
            except:
                pass
        if field[:6]=='cl1324':
            gtmp=np.where((np.abs(mras[j]-crs['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crs['dec'])<stol))[0]
            print len(gtmp)
            if len(gtmp)!=0: 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if nummatch[j]<1: gz=np.zeros(0)
        if (((field=='cl1324_southno')|(field=='cl1604no'))&(len(gz)==0)):
            gtmp=np.where((np.abs(mras2[j]-crs['ra'])/np.cos(mdecs2[j])<stol)&(np.abs(mdecs2[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch2[j]>0)): 
                disttmp=SphDist(mras2[j],mdecs2[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras[j]-crs['ra'])/np.cos(mdecs[j])<stol)&(np.abs(mdecs[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch[j]>0)): 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604no')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras4[j]-crs['ra'])/np.cos(mdecs4[j])<stol)&(np.abs(mdecs4[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch4[j]>0)): 
                disttmp=SphDist(mras4[j],mdecs4[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if len(gz)>0:
            if len(gz)>1: 
                print 'More than 1 entry for %s matched to %s - %s: '%(crm['optID1'][j],field,crm['indX'][j])
                print crs['z'][gz]
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j],maskcur[j],slitcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]],crs['mask'][gz[0]],crs['slit'][gz[0]]
            else:
                zcur[j],magrcur[j],magicur[j],magzcur[j],zerrcur[j],qcur[j],maskcur[j],slitcur[j]=crs['z'][gz[0]],crs['magR'][gz[0]],crs['magI'][gz[0]],crs['magZ'][gz[0]],crs['zerr'][gz[0]],crs['Q'][gz[0]],crs['mask'][gz[0]],crs['slit'][gz[0]]
    all_zs=crs['z'][crs['Q']>2.5]
    g_az=np.arange(len(all_zs))[np.abs(all_zs-0.5*(spec_dict[field]['z'][1]+spec_dict[field]['z'][2]))<0.5*(spec_dict[field]['z'][2]-spec_dict[field]['z'][1])]
    zoom_zs=all_zs[g_az]
    zoom_ras,zoom_decs=all_ra[g_az],all_decs[g_az]
    gqcur=np.where(qcur>2.5)[0]
    x_zs=zcur[gqcur]
    g_zs=np.arange(len(x_zs))[np.abs(x_zs-0.5*(spec_dict[field]['z'][1]+spec_dict[field]['z'][2]))<0.5*(spec_dict[field]['z'][2]-spec_dict[field]['z'][1])]
    x_zoom_zs=x_zs[g_zs]
    ra_zs,dec_zs = crm['raX'][gqcur],crm['decX'][gqcur]
    mask_zs,slit_zs=maskcur[gqcur],slitcur[gqcur]
    print '\nMatches for %s:'%field
    nncF,nfF,nncS,nfS,nncH,nfH= pdata['Full_net_cts'][gqcur],pdata['Full_flux'][gqcur],pdata['Soft_net_cts'][gqcur],pdata['Soft_flux'][gqcur],pdata['Hard_net_cts'][gqcur],pdata['Hard_flux'][gqcur]
    nbcF,nbcS,nbcH=pdata['Full_bkg_cts'][gqcur],pdata['Soft_bkg_cts'][gqcur],pdata['Hard_bkg_cts'][gqcur]
    
    for k,ik in zip(gqcur,np.arange(0,len(gqcur))):
        FILE.write('%10s %3i %9.5f %9.5f %E %E %E %6.1f %6.1f %6.1f %5.3f %10s %8s %6.1f %6.1f %6.1f %8.2f %8.2f %8.2f %s\n'%(field,crm['indX'][k],ra_zs[ik],dec_zs[ik],nfS[ik],nfH[ik],nfF[ik],nncS[ik],nncH[ik],nncF[ik],zcur[k],mask_zs[ik],slit_zs[ik],nbcS[ik],nbcH[ik],nbcF[ik],nncS[ik]/(1.+np.sqrt(0.75+nbcS[ik])),nncH[ik]/(1.+np.sqrt(0.75+nbcH[ik])),nncF[ik]/(1.+np.sqrt(0.75+nbcF[ik])),crm['optID1'][k]))
FILE.close()
