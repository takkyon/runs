import numpy as np
import matplotlib.pyplot as plt

cr=np.loadtxt('/home/rumbaugh/milliquas_lightcurve_entries_y1a1.tab',skiprows=1,dtype={'names':('mjd','imageid','cid','MGid','ra','dec','mag','magerr','band','exp'),'formats':('f8','i8','i8','i8','f8','f8','f8','f8','|S12','f8')})
mjd,mag,magerr,cID,bands=cr['mjd'],cr['mag'],cr['magerr'],cr['cid'],cr['band']
coldict={'g': 'green','r': 'red', 'i': 'magenta', 'z': 'blue', 'Y': 'cyan'}
SDSSbands=np.array(['u','g','r','i','z'])
SDSS_colnames={b:'cModelMag_%s'%b for b in SDSSbands}
def loadSDSS(filename):
    crSDSS=np.loadtxt(filename,skiprows=1,delimiter=',',dtype={'names':('objID','ra','dec','mjd','cModelMag_u','cModelMag_g','cModelMag_r','cModelMag_i','cModelMag_z'),'formats':('i8','f8','f8','i8','f8','f8','f8','f8','f8')})
    return crSDSS

def plot_SDSS(crS,band,bandname=None,connectpoints=True):
    SDSS_cols={'g': '#66ff66','u': 'purple', 'r': 'pink', 'i': 'brown', 'z': 'silver'}
    if bandname==None: bandname=band
    SDSSmag=crS[bandname]
    SDSSmjd=crS['mjd']
    curcol=SDSS_cols[band]
    if connectpoints:
        gsort=np.argsort(crS['mjd'])
        plt.plot(SDSSmjd[gsort],SDSSmag[gsort],color=curcol,lw=2)
    #plt.errorbar(mjd[gid][gband],mag[gid][gband],yerr=magerr[gid][gband],color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(SDSSmjd,SDSSmag,color=curcol,label='SDSS %s'%band,marker='d')
    

def plot_band(gid,band,maginp=None,maginperr=None,connectpoints=True):
    gband=np.where(bands[gid]==band)[0]
    if np.shape(maginp)!=():
        magplot=maginp
    else:
        magplot=mag[gid][gband]
    if np.shape(maginperr)!=():
        magploterr=maginperr
    else:
        magploterr=magerr[gid][gband]
    try:
        curcol=coldict[band]
    except KeyError:
        print '%s is not a valid band'%band
        return
    if connectpoints:
        gsort=np.argsort(mjd[gid][gband])
        plt.plot(mjd[gid][gband][gsort],magplot[gsort],color=curcol,lw=2)
    print mjd[gid][gband],magplot,magploterr
    plt.errorbar(mjd[gid][gband],magplot,yerr=magploterr,color=curcol,fmt='ro',lw=2,capsize=3,mew=1)
    plt.scatter(mjd[gid][gband],magplot,color=curcol,label=band)
    #return


def plot_lightcurve(cid,maginp=None,maginperr=None,band='all',plotSDSS=False,fname=None,connectpoints=True):
    band=band.lower()
    g=np.where(cID==cid)[0]
    if len(g)==0:
        print 'No matches for %i'%cid
        return
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    if band=='all':
        for b in coldict.keys():
            if np.shape(maginp)!=():
                gp=np.where(np.array(DF['BAND'])[np.array(DF['COADD_OBJECTS_ID'])==cid]==b)[0]
                magplot,magploterr=maginp[gp],maginperr[gp]
                plot_band(g,b,maginp=magplot,maginperr=magploterr,connectpoints=connectpoints)
            else:
                plot_band(g,b,maginp=maginp,maginperr=maginperr,connectpoints=connectpoints)
        if plotSDSS==True:
            crSDSS=loadSDSS('/home/rumbaugh/SDSS_table_%i.csv'%cid)
            for b in SDSSbands:
                plot_SDSS(crSDSS,b,bandname=SDSS_colnames[b],connectpoints=connectpoints)
        xlim=plt.xlim()
        plt.xlim(xlim[0],xlim[1]+0.12*(xlim[1]-xlim[0]))
        plt.legend()
    else:
        plot_band(g,band,connectpoints=connectpoints)
    plt.xlabel('MJD')
    if np.shape(maginp)!=():
        plt.ylabel('Mag_psf')
    else:
        plt.ylabel('Mag_auto')
    plt.title(cid)
    if fname!=None: plt.savefig(fname)
    return
        
            
