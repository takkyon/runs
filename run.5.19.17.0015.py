import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import healpy as hp
import pyfits as py
#nside=16384
nside=64
sdict={16:16,64:16}
execfile('/home/rumbaugh/pythonscripts/aitoff.py')

def covplot(ras,decs,pcol,nside=16):
    hpix=hp.ang2pix(nside,(90-decs)*np.pi/180.,ras*np.pi/180)
    b=np.bincount(hpix)
    hpixb=np.nonzero(b)
    b,hpixb=b[b>0],hpixb[0]
    HPang=np.array(hp.pix2ang(nside,hpixb))
    HPra,HPdec=HPang[1]*180/np.pi,90-HPang[0]*180/np.pi
    opacs=b*0.7/np.max(b)
    HPpsi,HPlam=HPdec*np.pi/180,(HPra-180)*np.pi/180
    HPx,HPy=(2*np.cos(HPpsi)*np.sin(HPlam*0.5))/(np.sinc(np.arccos(np.cos(HPpsi)*np.cos(0.5*HPlam))/np.pi)),np.sin(HPpsi)/(np.sinc(np.arccos(np.cos(HPpsi)*np.cos(0.5*HPlam))/np.pi))
    for ra,dec,op in zip(HPx,HPy,opacs): ax.scatter(ra,dec,color=pcol,marker='h',s=sdict[nside],alpha=op)
    ax.set_xlabel('RA')
    ax.set_ylabel('Dec.')
    ax.set_xlim(-1.1*np.pi,1.1*np.pi)
    ax.set_ylim(-1.1*np.pi/2,1.1*np.pi/2)
def do_plots(ras,decs,pcol,i,fname=None,nside=16):
    execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')
    covplot(ras,decs,pcol,nside=nside)
        
try:
    cr2
except NameError:
    cr2=np.loadtxt('TID_randsamp2_rumbaugh.csv',dtype={'names':('ra','dec','id'),'formats':('f8','f8','i8')},delimiter=',',skiprows=1) 
try:
    cr3
except NameError:
    cr3=np.loadtxt('sdss-poss+healpix.txt',dtype={'names':('n','ra','dec','id'),'formats':('i8','f8','f8','i8')})
crs,cols,fnames=cr2,'magenta','/home/rumbaugh/coverage_plot.SDSS.png'
fig=plt.figure(1)
plt.clf()
ax=fig.add_subplot(1,1,1)
ax.axis('off')
rastmp=crs['ra']+90
rastmp[rastmp>360]-=360
do_plots(rastmp,crs['dec'],cols,0,fnames,nside)
cry=np.loadtxt('Y3A1_TILE_CORNERS.tab',usecols=(1,2,3,4,5,6,7,8),skiprows=1)
for i in range(0,np.shape(cry)[0]):
    ras,decs=cry[i][:4]+90,cry[i][4:]
    ras[ras>360]-=360
    psi,lam=decs*np.pi/180,(ras-180)*np.pi/180
    x,y=(2*np.cos(psi)*np.sin(lam*0.5))/(np.sinc(np.arccos(np.cos(psi)*np.cos(0.5*lam))/np.pi)),np.sin(psi)/(np.sinc(np.arccos(np.cos(psi)*np.cos(0.5*lam))/np.pi))
    if np.max(ras)-np.min(ras)>200:
        ghi,glo=np.where(ras>200)[0],np.where(ras<100)[0]
        rahi,ralo=np.copy(x),np.copy(x)
        dechi,declo=np.copy(y),np.copy(y)
        rahi[glo],dechi[glo],ralo[ghi],declo[glo]=(2*np.cos(decs[glo]*np.pi/180)*np.sin(np.pi*0.5))/(np.sinc(np.arccos(np.cos(decs[glo]*np.pi/180)*np.cos(0.5*np.pi))/np.pi)),np.sin(decs[glo]*np.pi/180)/(np.sinc(np.arccos(np.cos(decs[glo]*np.pi/180)*np.cos(0.5*np.pi))/np.pi)),(2*np.cos(decs[glo]*np.pi/180)*np.sin(-np.pi*0.5))/(np.sinc(np.arccos(np.cos(decs[glo]*np.pi/180)*np.cos(0.5*-np.pi))/np.pi)),np.sin(decs[glo]*np.pi/180)/(np.sinc(np.arccos(np.cos(decs[glo]*np.pi/180)*np.cos(0.5*-np.pi))/np.pi))
        ax.fill(rahi,dechi,color='orange',alpha=0.3,edgecolor='orange')
        ax.fill(ralo,declo,color='orange',alpha=0.3,edgecolor='orange')
    else:
        ax.fill(x,y,color='orange',alpha=0.4,edgecolor='orange')
xdummy,ydummy=aitoff(360.,np.linspace(0,90,1000))
ax.plot(xdummy,ydummy,color='k')
ax.plot(-xdummy,ydummy,color='k')
ax.plot(-xdummy,-ydummy,color='k')
ax.plot(xdummy,-ydummy,color='k')
for psi in np.arange(-75,90,15):
    xdummy,ydummy=aitoff(np.linspace(0,360,5000),psi)
    ax.plot(xdummy,ydummy,color='k',alpha=0.3)
for lam in np.arange(0,360,45):
    xdummy,ydummy=aitoff(lam,np.linspace(-90,90,5000))
    ax.plot(xdummy,ydummy,color='k',alpha=0.3)
for psi in np.arange(-60,90,30):
    x,y=aitoff(0,psi*1.05)
    ax.text(x-np.pi*0.01,y,'%+i'%(psi)+r'$^\circ$',horizontalalignment='right',verticalalignment='center')
for lam,ra in zip(np.arange(45,360,45),np.arange(3,24,3)):
    x,y=aitoff(lam,5)
    ax.text(x,y,' %i'%((ra-6)%24)+r'$^h$',horizontalalignment='center',verticalalignment='center')

plt.savefig('coverage_plot_SDSS+Y3A1.shift.png')
