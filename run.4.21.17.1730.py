import numpy as np
import matplotlib.pyplot as plt
cry=np.loadtxt('/home/rumbaugh/DR7_BH_Y3A1_MATCH_COADD_PARAMS.tab',dtype={'names':('SDSSNAME','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y','magerr_g','magerr_r','magerr_i','magerr_z','magerr_y','class_star'),'formats':('|S24','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)
try:
    crs
except NameError:
    crs=np.loadtxt('/home/rumbaugh/Y3A1_star_magsample.tab',dtype={'names':('class_star','CID','RA','DEC','mag_g','mag_r','mag_i','mag_z','mag_y'),'formats':('f8','i8','f8','f8','f8','f8','f8','f8','f8')},skiprows=1)


matplotlib.rcParams['axes.linewidth']=3
matplotlib.rcParams['font.size']=14

plt.figure(1)
plt.clf()
a=plt.hist(cry['mag_g'],range=(15,25),bins=20)
evqhist,bins=a[0],a[1]
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_DR7.hist.4.21.17.png')

bin_midpoints = bins[:-1] + np.diff(bins)/2
cdf = np.cumsum(evqhist)
cdf = cdf / cdf[-1]
values = np.random.rand(10000)
value_bins = np.searchsorted(cdf, values)
random_from_cdf = bin_midpoints[value_bins]
gcontrol=np.searchsorted(crs['mag_g'],random_from_cdf)

plt.figure(1)
plt.clf()
plt.hist(crs['mag_g'],range=(15,25),bins=20)
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_Y3A1_stars.hist.4.21.17.png')


plt.figure(1)
plt.clf()
plt.hist(cry['mag_g'],range=(15,25),bins=20,color='b',normed=True)
plt.hist(crs['mag_g'][gcontrol],range=(15,25),bins=20,color='r',edgecolor='k',facecolor='None',lw=3,normed=True)
plt.xlim(15,25)
plt.xlabel('g-band Magnitude')
plt.ylabel('Number of Object')
plt.savefig('/home/rumbaugh/var_database/Y3A1/plots/magdist_Y3A1_control_comp.hist.4.21.17.png')

outcr=crs[gcontrol]
np.savetxt('Y3A1_star_control_sample.dat',outcr,header='class_star CID RA DEC mag_g mag_r mag_i mag_z mag_y',fmt='%f %i %f %f %f %f %f %f %f',comments='')
