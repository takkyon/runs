import numpy as np
import pyfits as py
import healpy as hp

hdu=py.open('/home/rumbaugh/dr7_bh_Nov19_2013.fits')
data=hdu[1].data
names,ra,dec=data['SDSS_NAME'],data['RA'],data['DEC']

hpix=hp.ang2pix(16384,(90-dec)*np.pi/180.,ra*np.pi/180,nest=True)
outcr=np.zeros((len(data),),dtype={'names':('SDSS_NAME','RA','DEC','HPIX'),'formats':('|S24','f8','f8','i8')})
outcr['SDSS_NAME'],outcr['RA'],outcr['DEC'],outcr['HPIX']=names,ra,dec,hpix
np.savetxt('/home/rumbaugh/dr7_bh_hpix.tab',outcr,fmt='%24s %f %f %i',header='SDSS_NAME RA DEC HPIX',comments='')
