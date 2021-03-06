import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as bpdf
execfile('/home/rumbaugh/LFC_color_param.py')
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

zarr=np.linspace(0.1,2,191)

targets=np.array(["rcs0224","cl0849","rxj0910","rxj1221","cl1350","rxj1757","cl1604","cl0023","cl1324","rxj1821","cl1137","rxj1716","rxj1053"])
zlist,gzl=np.zeros(len(targets)),np.zeros(len(targets),dtype='i8')
for i in range(0,len(targets)): 
    zlist[i]=spec_dict[targets[i]]['z'][0]
    gzl[i]=np.argsort(zarr-zlist[i])[0]
gasz=np.argsort(zlist)
zlist,gzl,targets=zlist[gasz],gzl[gasz],targets[gasz]

psfpdf=bpdf.PdfPages('/home/rumbaugh/LFC_color_param/template_colors.per_z.graz10.2.24.16.pdf')


cols=()
for i in range(0,len(zarr)): cols=cols+(i+2,)
crcp=np.loadtxt('/home/rumbaugh/LFC_color_param/comb_LFC_param_UVs.graz13.2.23.16.dat',usecols=cols)
Acomb=crcp[-1]
param_dict={'Acomb':Acomb,'z':zarr}
F_Acomb=interp1d(param_dict['z'],param_dict['Acomb'],kind='linear',bounds_error=False,fill_value=0)

crf=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S32')
crpre=np.loadtxt('/home/rumbaugh/git/eazy-photoz/templates/PEGASE2.0/graz_file.lis',dtype='|S6')

gz=np.arange(40,141)
z=np.linspace(0.5,1.5,101)
A_z=F_Acomb(z)
B_z=1-A_z
year = 10
gy=np.where(crpre=='graz%02i'%year)[0]
plt.figure(1)
plt.clf()
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
safeLB=950
safeUB=32000
crcc=np.loadtxt('/home/rumbaugh/cc_out.2.19.16.dat')
D_L=crcc[:,13][gz]*3.086E22
cc_z=crcc[:,0][gz]


obsrs,obsis,obszs=np.zeros((len(zlist),len(gy))),np.zeros((len(zlist),len(gy))),np.zeros((len(zlist),len(gy)))
for SED,iSED in zip(crf[gy],np.arange(len(gy))):
    curcr=np.loadtxt(SED)
    w,S=np.copy(curcr[:,0]),np.copy(curcr[:,1])
    #mblue,mred=np.zeros(len(z)),np.zeros(len(z))
    for i in range(0,len(zlist)): 
        #A,B=A_z[i],B_z[i]
        gdl=np.argsort(np.abs(z-cc_z))[0]
        obs_r,obs_i,obs_z=calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='r',D_L=D_L[gdl]),calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='i',D_L=D_L[gdl]),calc_obs_flux(w,S,z[i],safeLB,safeUB,filt='z',D_L=D_L[gdl])
        m_r=-2.5*np.log10(obs_r)-48.6
        m_i=-2.5*np.log10(obs_i)-48.6
        m_z=-2.5*np.log10(obs_z)-48.6
        obsrs[i][iSED],obsis[i][iSED],obszs[i][iSED]=m_r,m_i,m_z
        #m_b=-2.5*np.log10(A*obs_r+B*(obs_i))-48.6
        #m_r=-2.5*np.log10(A*obs_i+B*obs_z)-48.6
        #mblue[i],mred[i]=m_b,m_r
for i in range(0,len(zlist)): 
    fig.clf()
    ax=fig.add_subplot(1,1,1)
    ax.plot(obsrs[i]-obsis[i])
    ax.scatter([0],[obsrs[i][0]-obsis[i][0]],color='r',marker='x')
    ax.set_xlabel("Template")
    ax.set_ylabel("r'-i'")
    ax.set_title("%s - Redshift = %.2f"%(targets[i],zlist[i]))
    #ax.set_xlim(19,25)
    #ax.set_ylim(0,1.6)
    fig.savefig(psfpdf,format='pdf')
for i in range(0,len(zlist)): 
    fig.clf()
    ax=fig.add_subplot(1,1,1)
    ax.plot(obsis[i]-obszs[i])
    ax.scatter([0],[obsis[i][0]-obszs[i][0]],color='r',marker='x')
    ax.set_xlabel("Template")
    ax.set_ylabel("i'-z'")
    ax.set_title("%s - Redshift = %.2f"%(targets[i],zlist[i]))
    #ax.set_title("%s (i' err. < 0.05)"%field)
    #ax.set_xlim(19,25)
    #ax.set_ylim(0,1.6)
    fig.savefig(psfpdf,format='pdf')

psfpdf.close()
