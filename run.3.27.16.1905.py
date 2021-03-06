import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/SphDist.py')
execfile('/home/rumbaugh/cosmocalc.py')
execfile('/home/rumbaugh/KStest.py')
date='3.27.16'

rbounds=(-0.5,10)
nbins=(rbounds[1]-rbounds[0])*2

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

cr2=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters.dat',dtype={'names':('field','cluster','ra','dec','z','sig0.5mpc','sig0.5mpcerr','n0.5mpc','sig1mpc','sig1mpcerr','n1mpc','logMvir','LMVerr','nh'),'formats':('|S24','|S24','f8','f8','f8','f8','f8','i8','f8','f8','i8','f8','f8','f8')})
cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clusters_Xray.dat',dtype={'names':('field','cluster','ra','dec','z','nh'),'formats':('|S24','|S24','f8','f8','f8','f8')})
testfield,testclus=np.zeros(np.shape(cr)[0],dtype='|S24'),np.zeros(np.shape(cr)[0],dtype='|S24')
for i in range(0,len(testclus)):
    testfield[i]=cr['field'][i].lower()
    testclus[i]=cr['cluster'][i].lower()
testfield2,testclus2=np.zeros(np.shape(cr2)[0],dtype='|S24'),np.zeros(np.shape(cr2)[0],dtype='|S24')
for i in range(0,len(testclus2)):
    testfield2[i]=cr2['field'][i].lower()
    testclus2[i]=cr2['cluster'][i].lower()

cfields,ras,decs,zs,clus_sig=np.append(testfield2,testfield[-4:]),np.append(cr2['ra'],cr['ra'][-4:]),np.append(cr2['dec'],cr['dec'][-4:]),np.append(cr2['z'],cr['z'][-4:]),np.append(cr2['sig0.5mpc'],np.ones(4)*1000.)
#gcs=np.where(clus_sig==0)[0]
#clus_sig[gcs]=cr2['sig0.5mpc'][gcs]


infile='/home/rumbaugh/combined_match_catalog.1.19.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','bcnts_soft','bcnts_hard','bcnts_full'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

cosmocalc(zs,outfile='/home/rumbaugh/cc_out_clus.2.9.16.dat',ids=cfields)

crcc=np.loadtxt('/home/rumbaugh/cc_out_clus.2.9.16.dat',usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
kpc = crcc[:,12]
Hz = crcc[:,16]*70.
Mpc = kpc/1000.

legposdict={"rcs0224":'upper left',"cl0849":'upper left',"rxj0910":'lower right',"rxj1221":'upper left',"cl1350":'lower right',"rxj1757":'upper right',"cl0023":'upper right',"cl1324_north":'upper left',"cl1324_south":'upper left',"rxj1821":'upper left',"cl1137":'lower left',"rxj1716":'lower left',"rxj1053":'lower center',"cl1604":'upper left'}

clusdist=np.ones(len(crx['RA']))*-1
veldist=np.ones(len(crx['RA']))*-1
PSdist=np.ones(len(crx['RA']))*-1
for i in range(0,len(crx['RA'])):
    gnoz=np.where(((cfields==crx['field'][i].lower())|(cfields==crx['field'][i][:6].lower())))[0]
    zx=crx['redshift'][i]
    tmpzdist=np.abs(((1+zx)**2-(1+zs[gnoz])**2)/((1+zx)**2+(1+zs[gnoz])**2))*3.*10.**5/clus_sig[gnoz]
    tmpdistnoz=60*SphDist(crx['RA'][i],crx['Dec'][i],ras[gnoz],decs[gnoz])
    tmpr500 = 2*clus_sig[gnoz]/(np.sqrt(500)*Hz[gnoz])
    tmpclusdistnoz=tmpdistnoz*Mpc[gnoz]/tmpr500
    tmpPSdist=tmpzdist*tmpclusdistnoz
    gPS=np.argsort(tmpPSdist)[0]
    clusdist[i],veldist[i],PSdist[i]=tmpclusdistnoz[gPS],tmpzdist[gPS],tmpPSdist[gPS]
crd=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists_r500.dat',usecols=(1,2,3,4,5,6))
crdf=np.loadtxt('/home/rumbaugh/Chandra/clustocentric_dists.dat',usecols=(0,),dtype='|S24')

ccd=crd[:,3]
vd=crd[:,4]
psd=crd[:,5]

fig=plt.figure(2)
targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl0023","cl1324_north","cl1324_south","rxj1821","cl1137","rxj1716","rxj1053","cl1604"])
specloaddict={'names':('ID','mask','slit','ra','dec','magR','magI','magZ','z','zerr','Q'),'formats':('|S16','|S16','|S8','f8','f8','f8','f8','f8','f8','f16','i8')}
allclusdist=np.zeros(0)
allveldist=np.zeros(0)
allPSdist=np.zeros(0)

coeff=[0.1,0.4,2]
for field in ['rxj1053']: 
    crs=np.loadtxt('/home/rumbaugh/Chandra/speccats/%s_spec.cat'%field,dtype=specloaddict)
    g=np.where(((cfields==field)|(cfields==field[:6].lower())))[0]
    gq=np.where((crs['Q']>2.5))#&(crs['z']>spec_dict[field]['z'][1]))#&(crs['z']<spec_dict[field]['z'][2]))[0]
    g1,g2,g3,g4,g5=np.where(crs['z'][gq]<1.1)[0],np.where((crs['z'][gq]>=1.1)&(crs['z'][gq]<=1.15))[0],np.where((crs['z'][gq]>1.15)&(crs['z'][gq]<1.2))[0],np.where((crs['z'][gq]>1.2)&(crs['z'][gq]<1.3))[0],np.where(crs['z'][gq]>1.3)[0]
    r200 = 2*clus_sig/(np.sqrt(200)*Hz)
    r500 = 2*clus_sig/(np.sqrt(500)*Hz)
    fig.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    ax=fig.add_subplot(1,1,1)
    #tmpallclusdist[tmpIRflag==0]=-0.24
    ax.scatter(crs['ra'][gq][g1],crs['dec'][gq][g1],color='magenta',label='z<1.1')
    ax.scatter(crs['ra'][gq][g2],crs['dec'][gq][g2],color='orange',label='1.1<z<1.15')
    ax.scatter(crs['ra'][gq][g3],crs['dec'][gq][g3],color='green',label='1.15<z<1.2')
    ax.scatter(crs['ra'][gq][g4],crs['dec'][gq][g4],color='blue',label='1.2<z<1.3')
    ax.scatter(crs['ra'][gq][g5],crs['dec'][gq][g5],color='cyan',label='z>1.3')
    #ax.scatter(crd[:,1][crdf==field],crd[:,2][crdf==field],marker='s',facecolors='none',edgecolors='red')
    phidummy=np.linspace(0,2*np.pi,1000)
    xdummy,ydummy=np.cos(phidummy),np.sin(phidummy)
    for ic in g:
        xcen,ycen=ras[ic],decs[ic]
        ax.plot(xdummy*0.5/Mpc[ic]/3600.+xcen,ydummy*0.5/Mpc[ic]/3600.+ycen,lw=2,ls='--',color='k')
        ax.plot(xdummy*r200[ic]/Mpc[ic]/3600.+xcen,ydummy*r200[ic]/Mpc[ic]/3600.+ycen,lw=2,ls='dotted',color='k')
        ax.plot(xdummy*r500[ic]/Mpc[ic]/3600.+xcen,ydummy*r500[ic]/Mpc[ic]/3600.+ycen,lw=2,ls='dotted',color='k')
    ax.set_xlabel('RA')
    ax.set_ylabel('Dec')
    ax.set_title('%s'%field)
    plt.legend(loc=legposdict[field])
    xlim=plt.xlim()
    ylim=plt.ylim()
    ax.set_ylim(ylim[1],ylim[0])
    #ax.set_ylim(0,10)
    #ax.set_xlim(-0.5,10)
    fig.savefig('/home/rumbaugh/Chandra/plots/spatial_plot_zranges.%s.%s.png'%(field,date))


