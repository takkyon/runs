import numpy as np
import os
import matplotlib.pyplot as plt
import pyfits as py
execfile('/home/rumbaugh/angconvert.py')
execfile('/home/rumbaugh/SphDist.py')
ldate='1.5.16'
date='1.19.16'

outfile='/home/rumbaugh/combined_match_catalog.%s.dat'%date
FILE=open(outfile,'w')
FILE.write('# field number RA Dec flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit bcnts_soft bcnts_hard bcnts_full\n')

stol=1./3600.
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

obsdict={'RCS0224-0002': {'obsID': '3181+4987','photcatname': 'rcs0224'},'CL 0848.6+4453': {'obsID': '927+1708','photcatname': 'cl0849'},'RX J0910+5422': {'obsID': '2227+2452','photcatname': 'cl0910'},'RX J105343+5735': {'obsID': '4936','photcatname': 'rxj1053'},'V 1221+4918': {'obsID': '1662','photcatname': 'rxj1221'},'RX J1350.0+6007': {'obsID': '2229','photcatname': 'cl1350'},'RX J1716.9+6708': {'obsID': '548','photcatname': 'rxj1716'}}

namedict = {obsdict[x]['obsID']: x for x in obsdict.keys()}

band_dict={'soft': {'erange': '0.5-2.0','LB':0.5,'UB':2.0},'hard': {'erange': '2.0-8.0','LB':2.0,'UB':8.0},'full': {'erange': '0.5-8.0','LB':0.5,'UB':8.0}}

times=np.array([51730.160737324,125146.86866667,79084.755891771,61469.789688443,105735.52582365,58307.676632384,65311.025181476,14370.453707409,92237.849235535,88973.209339125])
nh = np.array([3.71,2.73,1.44,2.73,1.98,1.76,1.98,2.86,0.58,2.86])
obs = np.array(['548','927','1662','1708','2227','2229','2452','3181','4936','4987'])
obs_dict={obs[x]: {'exp': times[x], 'nh': nh[x]} for x in range(0,10)}

zfull=np.zeros(0)

spec_dict= { \
             'cl1324': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9404,9836,9840]}, \
             'cl1324_north': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9403,9840]}, \
             'cl1324_south': {'file': 'FINAL.cl1322.lrisplusdeimos.jul2015.1322Ptmp.nodups.cat', 'loaddict': '','z':[0.756,0.65,0.79], 'obsids': [9404,9836]}, \
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
             'rxj0910': {'file': 'FINAL.spectroscopic.autocompile.blemaux.sc0910.may2015.plusT08.nodups.cat', 'loaddict': '','z':[1.110,1.08,1.15], 'obsids': [2227,2452]}, \
             'rxj1757': {'file': 'FINAL.spectroscopic.autocompile.N200.blemaux.aug2013.nodups.cat', 'loaddict': '','z':[0.691,0.68,0.71], 'obsids': [10443,11999]}, \
             'X10': {'file': 'spectroscopic.autocompile.blemaux.0943A.targetsonly.cat', 'loaddict': '','z':[0,0,0], 'obsids': []}, \
             'cl1137': {'file': 'spectroscopic.autocompile.blemaux.1137.1137Ctmp.may2015.cat', 'loaddict': '','z':[0.959,0.94,0.97], 'obsids': [4161]}, \
             'rxj1053': {'file': 'FINAL.spectroscopic.autocompile.blemaux.RXJ1053.dec2015.BCDXtargetsonly.nodups.cat', 'loaddict': '','z':[1.140,1.1,1.15], 'obsids': [4936]}}

fullcat=np.loadtxt('/home/rumbaugh/Chandra/full_Xray_catalog.dat',dtype={'names':('obsID','xrayID','RAX','DecX','Xflux_soft','Xflux_hard','Xflux_full','Xnetcnts_soft','Xnetcnts_hard','Xnetcnts_full','Xsig_soft','Xsig_hard','Xsig_full','Xwd_sig_soft','Xwd_sig_hard','Xwd_sig_full','Xdetcode','Xerr','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone','ci','redshift','zerr','magR','magI','magZ','Q'),'formats':('|S16','i8','f8','f8','e8','e8','e8','e8','e8','e8','f8','f8','f8','f8','f8','f8','f8','f8','i8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','|S16','f8','f8','f8','f8','f8','f8','f8','f8','e8','i8')})

optmatchloaddict={'names':('indX','raX','decX','errX','nummatch','raopt1','decopt1','optID1','Popt1','likeopt1','raopt2','decopt2','optID2','Popt2','likeopt2','raopt3','decopt3','optID3','Popt3','likeopt3','probnone'),'formats':('i8','f8','f8','f8','i8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8','f8','|S32','f8','f8','f8')}

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053"])

obj_dict=dict(zip(np.array(["548","1662","2229","4936","927+1708","2227+2452","3181+4987"]),np.zeros(7)))
names=obj_dict.keys()

#FILE=open('/home/rumbaugh/Chandra/full_Xray_catalog.dat','w')

tol=0.2

obsid_dict={'cl0023': '7914', 'cl1324_north': '9403+9840', 'cl1324_south': '9404+9836', 'rxj1757': '10443+11999', 'rxj1821': '10444+10924', 'cl1604': '6932+6933+7343'}

for field in targets: 
    if field != 'cl164':
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
    crp=py.open('/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/SRCv1/bkup_1.19.16_%s_srclist_v1.fits'%(field,field,field))
    pdata=crp[1].data
    crs=np.loadtxt('/home/rumbaugh/git/ORELSE/Catalogs/Spec_z/%s'%spec_dict[field]['file'],dtype=specloaddict)
    matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.dat'%(field,field,field,ldate)
    if field=='cl1604':matchcat='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch.%s.dat'%(field,field,field,'1.11.16')
    crm=np.loadtxt(matchcat,dtype=optmatchloaddict)
    numX=len(crm['indX'])
    mras,mdecs=crm['raopt1'],crm['decopt1']
    nummatch=crm['nummatch']
    try:
        matchcat2='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_min5.%s.dat'%(field,field,field,ldate)
        crm2=np.loadtxt(matchcat2,dtype=optmatchloaddict)
        numX2=len(crm2['indX'])
        mras2,mdecs2=crm2['raopt1'],crm2['decopt1']
        nummatch2=crm2['nummatch']
    except:
        crm2=np.zeros(0)
    try:
        matchcat3='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_specmatch.%s.dat'%(field,field,field,ldate)
        crm3=np.loadtxt(matchcat3,dtype=optmatchloaddict)
        numX3=len(crm3['indX'])
        mras3,mdecs3=crm3['raopt1'],crm3['decopt1']
        nummatch3=crm3['nummatch']
    except:
        crm3=np.zeros(0)
    try:
        matchcat4='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s/%s_optmatch_specmatch_min5.%s.dat'%(field,field,field,ldate)
        crm4=np.loadtxt(matchcat4,dtype=optmatchloaddict)
        numX4=len(crm4['indX'])
        mras4,mdecs4=crm4['raopt1'],crm4['decopt1']
        nummatch4=crm4['nummatch']
    except:
        crm4=np.zeros(0)
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
            if len(gtmp)!=0: 
                disttmp=SphDist(mras[j],mdecs[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if nummatch[j]<1: gz=np.zeros(0)
        if (((field=='cl1324_south')|(field=='cl1604'))&(len(gz)==0)):
            gtmp=np.where((np.abs(mras2[j]-crs['ra'])/np.cos(mdecs2[j])<stol)&(np.abs(mdecs2[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch2[j]>0)): 
                disttmp=SphDist(mras2[j],mdecs2[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604')&(len(gz)==0)):
            gtmp=np.where((np.abs(mras3[j]-crs['ra'])/np.cos(mdecs3[j])<stol)&(np.abs(mdecs3[j]-crs['dec'])<stol))[0]
            if ((len(gtmp)!=0)&(nummatch3[j]>0)): 
                disttmp=SphDist(mras3[j],mdecs3[j],crs['ra'][gtmp],crs['dec'][gtmp])
                gas=np.argsort(disttmp)
                gz=gtmp[gas[:1]]
        if ((field=='cl1604')&(len(gz)==0)):
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
    x_zs=zcur[qcur>2.5]
    g_zs=np.arange(len(x_zs))[np.abs(x_zs-0.5*(spec_dict[field]['z'][1]+spec_dict[field]['z'][2]))<0.5*(spec_dict[field]['z'][2]-spec_dict[field]['z'][1])]
    x_zoom_zs=x_zs[g_zs]
    ra_zs,dec_zs = crm['raX'][qcur>2.5][g_zs],crm['decX'][qcur>2.5][g_zs]
    mask_zs,slit_zs=maskcur[qcur>2.5][g_zs],slitcur[qcur>2.5][g_zs]
    print '\nMatches for %s:'%field
    nncF,nfF,nncS,nfS,nncH,nfH= pdata['Full_net_cts'][qcur>2.5][g_zs],pdata['Full_flux'][qcur>2.5][g_zs],pdata['Soft_net_cts'][qcur>2.5][g_zs],pdata['Soft_flux'][qcur>2.5][g_zs],pdata['Hard_net_cts'][qcur>2.5][g_zs],pdata['Hard_flux'][qcur>2.5][g_zs]
    nbcF,nbcS,nbcH=pdata['Full_bkg_cts'][qcur>2.5][g_zs],pdata['Soft_bkg_cts'][qcur>2.5][g_zs],pdata['Hard_bkg_cts'][qcur>2.5][g_zs]
    #oncF,ofF,oncS,ofS,oncH,ofH= matched_ncntsF[qcur>2.5][g_zs],matched_fluxF[qcur>2.5][g_zs],matched_ncntsS[qcur>2.5][g_zs],matched_fluxS[qcur>2.5][g_zs],matched_ncntsH[qcur>2.5][g_zs],matched_fluxH[qcur>2.5][g_zs]
    #pdncF,pdfF,pdncS,pdfS,pdncH,pdfH= (oncF-nncF)*100./nncF,(ofF-nfF)*100./nfF,(oncS-nncS)*100./nncS,(ofS-nfS)*100./nfS,(oncH-nncH)*100./nncH,(ofH-nfH)*100./nfH
    
    for k in np.argsort(x_zoom_zs):
        #rah,ram,ras=deg2hms(ra_zs[k])
        #decd,decm,decs=deg2dms(dec_zs[k])
        #print '%5.3f  %02i:%02i:%05.2f %02i:%02i:%05.2f - mask: %s slit: %s\n'%(x_zoom_zs[k],rah,ram,ras,decd,decm,decs,mask_zs[k],slit_zs[k])
        #print "Photometry comparison - new, old, % diff."
        #print 'Full - net counts: %6.1f, %6.1f %6.1f  flux: %E, %E, %6.1f\nSoft - net counts: %6.1f, %6.1f %6.1f  flux: %E, %E, %6.1f\nHard - net counts: %6.1f, %6.1f %6.1f  flux: %E, %E, %6.1f\n'%(nncF[k],oncF[k],pdncF[k],nfF[k],ofF[k],pdfF[k],nncS[k],oncS[k],pdncS[k],nfS[k],ofS[k],pdfS[k],nncH[k],oncH[k],pdncH[k],nfH[k],ofH[k],pdfH[k])
        #print ra_zs[k],dec_zs[k]
        FILE.write('%10s %2i %9.5f %9.5f %E %E %E %6.1f %6.1f %6.1f %5.3f %10s %8s %6.1f %6.1f %6.1f %8.2f %8.2f %8.2f\n'%(field,k,ra_zs[k],dec_zs[k],nfS[k],nfH[k],nfF[k],nncS[k],nncH[k],nncF[k],x_zoom_zs[k],mask_zs[k],slit_zs[k],nbcS[k],nbcH[k],nbcF[k],nncS[k]/(1.+np.sqrt(0.75+nbcS[k])),nncH[k]/(1.+np.sqrt(0.75+nbcH[k])),nncF[k]/(1.+np.sqrt(0.75+nbcF[k]))))
        #zfull=np.append(zfull,x_zoom_zs[k])
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.hist(zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='k')
    plt.hist(x_zoom_zs,bins=80,range=(spec_dict[field]['z'][1],spec_dict[field]['z'][2]),color='r')
    plt.xlabel('Redshift')
    plt.ylabel('Number of sources')
    plt.title(field)
    #plt.savefig('/home/rumbaugh/Chandra/plots/z_hist_zoom.%s.%s.png'%(field,date))
    plt.figure(2)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    plt.hist(all_zs,bins=200,range=(0,2),color='k')
    plt.hist(x_zs,bins=200,range=(0,2),color='r')
    plt.xlabel('Redshift')
    plt.ylabel('Number of sources')
    plt.title(field)
    #plt.savefig('/home/rumbaugh/Chandra/plots/z_hist.%s.%s.png'%(field,date))
    plt.figure(3)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    for obs in spec_dict[field]['obsids']:
        crobs=np.loadtxt('/home/rumbaugh/Chandra/%s/chips_wcs.%s.reg'%(obs,obs),dtype='string',skiprows=3)
        for chip in range(0,len(crobs)):
            tmpcoords=crobs[chip].split(',')
            tmpcoords[0]=tmpcoords[0][8:]
            tmpcoords[-1]=tmpcoords[-1][:-1]
            cra,cdec=np.array([float(tmpcoords[x]) for x in np.arange(0,len(tmpcoords),2)]),np.array([float(tmpcoords[x]) for x in np.arange(1,len(tmpcoords),2)])
            cra,cdec=np.append(cra,cra[0]),np.append(cdec,cdec[0])
            plt.plot(cra,cdec,color='k')
    plt.scatter(zoom_ras,zoom_decs,s=4,color='k')
    plt.scatter(crm['raX'],crm['decX'],s=14,color='b')
    plt.scatter(crm['raX'][crm['nummatch']>0],crm['decX'][crm['nummatch']>0],s=1,color='cyan')
    plt.scatter(ra_zs,dec_zs,s=16,color='r')
    xlims=plt.xlim()
    plt.xlim(xlims[1],xlims[0])
    plt.xlabel('RA')
    plt.ylabel('Dec')
    plt.savefig('/home/rumbaugh/Chandra/plots/spatial_plot.xray_matches.%s.%s.png'%(field,date))
FILE.close()
#execfile('/home/rumbaugh/cosmocalc.py')
#cosmocalcin='/home/rumbaugh/cc_out.1.7.16.dat'
#cosmocalc(zfull,outfile=cosmocalcin)
