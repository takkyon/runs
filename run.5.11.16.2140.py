import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile("/home/rumbaugh/makeCMD.py")
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
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}

cmloaddict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigs','sigh','sigf'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S24','|S24','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S64','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}
date='3.9.16'

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])

zlist=np.zeros(len(targets))
for i in range(0,len(targets)): zlist[i]=spec_dict[targets[i]]['z'][0]

crRS=np.loadtxt('/home/rumbaugh/Chandra/RS_fits.composite_colors.nofit.%s.dat'%date,dtype={'names':('field','y0','m','sig','numsig'),'formats':('|S32','f8','f8','f8','i8')})
fig=figure(1)
zarr=np.linspace(0.1,2,191)

#ARed,ABlue=0.43*(1-1.81*(zarr-0.63)),0.45*(1-1.825*(zarr-0.7))
#BRed,BBlue=0.57*(1.81*(zarr-0.63)),0.55*(1.825*(zarr-0.7))
ARed,ABlue=0.424*(1-1.794*(zarr-0.628)),0.45*(1-1.824*(zarr-0.679))
BRed,BBlue=0.576*(1.794*(zarr-0.628)),0.55*(1.824*(zarr-0.679))
ARed[zarr>1/1.794+0.628]=0
BRed[zarr<0.628]=0
ABlue[zarr>1/1.824+0.679]=0
BBlue[zarr<0.679]=0

FILE=open('/home/rumbaugh/Chandra/Blue_fracs.5.11.16.dat','w')
FILE.write('# field blue_frac numgal blue_frac_cut numgal_cut\n')

cols=()
for i in range(0,len(zarr)): cols=cols+(i+2,)
for field in targets[np.argsort(zlist)]:
    pcat = '/home/rumbaugh/Chandra/photcats/%s_rizdata.corr.gz'%field
    crp=np.loadtxt(pcat,dtype=refdict)
    scat='/home/rumbaugh/Chandra/speccats/%s_spec.cat'%field
    crs=np.loadtxt(scat,dtype=specloaddict)
    cmcat='/home/rumbaugh/combined_match_catalog.2.9.16.dat'
    crcm=np.loadtxt(cmcat,cmloaddict)
    testfield=np.zeros(np.shape(crcm)[0],dtype='|S24')
    for i in range(0,len(testfield)):
        testfield[i]=crcm['field'][i].lower()
    testfield[((testfield=='cl1324_south')|(testfield=='cl1324_north'))]='cl1324'
    #if field[:6] in ['cl1604','cl1324']:
    if field[:6] in ['aaacl1604','aaacl1324']:
        numsig=2
    else: 
        numsig=3
    rerr,ierr,zerr=np.zeros(len(crs['magR'])),np.zeros(len(crs['magR'])),np.zeros(len(crs['magR']))
    for ipr in range(0,np.shape(crs)[0]):
        gp=np.where(((np.abs(crs['ra'][ipr]-crp['ra'])<0.2/3600)&(np.abs(crs['dec'][ipr]-crp['dec'])<0.2/3600)&(np.abs(crs['magR'][ipr]-crp['magR'])<0.1)&(np.abs(crs['magI'][ipr]-crp['magI'])<0.1)))[0]
        if len(gp)==0:
            rerr[ipr],ierr[ipr]=99,99
        else:            
            gp=gp[0]
            rerr[ipr],ierr[ipr],zerr[ipr]=crp['dmagR'][gp],crp['dmagI'][gp],crp['dmagZ'][gp]
    curdir='/home/rumbaugh/Chandra/ImperialPipeline/ORELSE/%s/proc/%s'%(field,field)
    outfile='%s/%s_clus_CMD_nofit.%s.dat'%(curdir,field,date)
    cr=np.loadtxt(outfile,dtype={'names':('ID','mask','slit','RA','Dec','redshift','magR','magI','dmagR','dmagI','isXray'),'formats':('|S32','|S32','|S32','f8','f8','f8','f8','f8','f8','f8','bool')})
    plotfile='/home/rumbaugh/Chandra/plots/CMD_comp_color.nofit.%s_clus.%s.png'%(field,date)
    gf=np.where(crRS['field']==field)[0][0]
    y0,m,sig=crRS['y0'][gf],crRS['m'][gf],crRS['sig'][gf]
    width=2*numsig*sig
    r,i=cr['magR'][0==cr['isXray']],cr['magI'][0==cr['isXray']]

    
    rso=(y0+m*i-(r-i))/(0.5*width)
    gblue=np.where(rso>1)[0]
    gblue2=np.where(rso[i<-20.9]>1)[0]
    bluefrac,bluefrac2=len(gblue)*1./len(rso),len(gblue2)*1./len(rso)
    FILE.write('%12s %.4f %3i %.4f %i\n'%(field,bluefrac,len(rso),bluefrac2,len(rso[i<-20.9])))
    print '%12s %.4f %3i %.4f %i\n'%(field,bluefrac,len(rso),bluefrac2,len(rso[i<-20.9]))
FILE.close()
