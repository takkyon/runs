import numpy as np
#import matplotlib
#import matplotlib.pylab as pylab
import math as m

try:
    t3013
except NameError:
    t3013 = 3

#5281,1757,1324+3059,1324+3011,1604A,1604B
names = np.array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B'])
namespec = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/spec_10444+10924.pi","/home/rumbaugh/ChandraData/RXJ1757/master/spec_RXJ1757_grp.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9403+9840.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9836.pi","/home/rumbaugh/ChandraData/Cl1324/master/spec_9404+9826_3013.4.24.11.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932a.3.28.pi","/home/rumbaugh/diffuse/diffuse_stuff/cluster.6932b.3.28.pi"])
namef = np.array(["/home/rumbaugh/ChandraData/NEP5281/master/acis10444+10924.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/RXJ1757/master/RXJ1757.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9403+9840.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.nops.fits","/home/rumbaugh/ChandraData/Cl1324/master/acis9404+9836.img.500-2000.nops.fits","/scratch/rumbaugh/ciaotesting/Cl1604/6932/acis6932.img.500-2000.nops.fits","/scratch/rumbaugh/ciaotesting/Cl1604/6932/acis6932.img.500-2000.nops.fits"])

xcens = np.array([3884.513,4097.7827,4093.65,3912.3173,4636.0706,4007.0272,3945.6178])
ycens = np.array([4112.3424,4351.7991,4920.9909,3445.9129,3657.7822,3412.1968,4605.2017])

ncnts = np.array([670,298,96,212,108,219,69])


Temps = np.array([4.95,3.75,4.71,3.71,t3013,3.50,1.64])
TerrU = np.array([0.99,1.00,10,1.44,10,1.82,0.65])
TerrD = np.array([0.74,0.68,2.95,0.94,2.99,1.08,0.45])
sigma = np.array([921,652,880,914,819,619,811])
sigerr = np.array([76,123,124,137,242,96,76])

lineslope = (m.log(2146)-m.log(308))/(m.log(20))
lineb = m.log(308)
expb = 308.0
lineX = (np.arange(10000)+5)*(10.0/10000)
lineY = expb*lineX**lineslope

anninner = np.array([120,100,160,100,160,150,100])

#nharr = np.array([5.66,4.07,1.15,1.16,1.23,1.23])
#I need to use Dale's value forit to be compatible
nharr = np.array([5.66,4.07,1.15,1.16,1.16,7.57,7.57])/100.0
rsarr = np.array([0.84,0.69,0.69,0.76,0.76,0.898,0.866])
times = np.array([49548.501183658,46451.792387024,48391.890220549,50399.00069391,50399.00069391,49478.092354796,49478.092354796])
cnt2flux = np.zeros(len(nharr))

crc = read_file("/home/rumbaugh/cosmocalc_out.4.24.11.nh.dat")
Hz = get_colvals(crc,'col5')*0.7
Ez = Hz/70.0
mpc = get_colvals(crc,'col12')*0.7
mpccm = get_colvals(crc,'col13')*0.7
lumdists = get_colvals(crc,'col9')/0.7
lumdistcm = lumdists*3.09e24
lumdistmod = lumdists*3.09
tcnts = np.zeros(len(nharr))
lums = np.zeros(len(nharr))
lumerr = np.zeros(len(nharr))

for i in range(0,len(sigma)):
    load_pha(str(namespec[i]))
    notice()
    subtract()
    set_model(xsraymond.rs*xswabs.abs1)
    rs.kT = Temps[i]
    rs.redshift = rsarr[i]
    rs.Abundanc = 0.3
    rs.norm = 1.0
    abs1.nh = nharr[i]
    freeze(abs1.nh)
    thaw(rs.norm)
    time = times[i]
    fake_pha(1,get_arf(),get_rmf(),time)
    mcnt = calc_model_sum(0.5,8)
    rs.norm = 1.0/mcnt
    freeze(rs.norm)
    eflx = calc_energy_flux(0.5,8.0)
    mcnt2 = calc_model_sum(0.5,8.0)
    abs1.nh = 0.0
    fake_pha(1,get_arf(),get_rmf(),time)
    eflx2 = calc_energy_flux(2.0/rsarr[i],8.0/rsarr[i])
    cnt2flux[i] = time*eflx2
    load_data(str(namef[i]))
    set_coord('physical')
    set_model(beta2d.b)
    r200 = 2*(mpc[i]*60)*2*sigma[i]/(m.sqrt(200)*Hz[i])
    b.xpos = xcens[i]
    b.ypos = ycens[i]
    b.r0 = 2*0.18*(mpc[i]*60)
    b.alpha = 1.5
    cperc = calc_source_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,anninner[i]))/calc_source_sum2d('circle(%f,%f,%f)'%(b.xpos.val,b.ypos.val,r200))
    tcnts[i] = ncnts[i]/cperc
    tcerr = m.sqrt(ncnts[i])/cperc
    flux = tcnts[i]*cnt2flux[i]/time
    ferr = tcerr*cnt2flux[i]/time
    lums[i] = flux*4*m.pi*lumdistmod[i]**2*10**5*Ez[i]
    lumerr[i] = ferr*4*m.pi*lumdistmod[i]**2*10**5*Ez[i]
    #lums in units of 10^43 ergs/s
FILE=open('/home/rumbaugh/paperstuff/clus.lums.hard.6.20.11.dat','w')
for i in range(0,len(cnt2flux)):
    FILE.write('%s %f %f %e\n'%(names[i],lums[i],lumerr[i],cnt2flux[i]))
    print '%s - count rate to flux conversion: %e\n'%(names[i],cnt2flux[i])
    print 'Total soft-band luminosity (10^43 ergs/s): %f\n'%(lums[i])
    
FILE.close()

    
