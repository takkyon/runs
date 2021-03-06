import numpy as np
import math as m
import time
import sys
import matplotlib
import matplotlib.pylab as pylab
execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/scale_estimators.py")
execfile("/home/rumbaugh/DStest.py")
execfile("/home/rumbaugh/angconvert.py")
c = 3.0*10**5

def sigclip(data,mean,sig,sigthresh=3.0):
    gsc = np.where((data < mean + sigthresh*sig) & (data > mean - sigthresh*sig))
    gsc = gsc[0]
    #if ccnt == 6:
    #    print mean,sig,data[gsc]
    return gsc


zlb = [0.82,0.65,0.68,0.80,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.84,0.96,0.96,1.2]
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7

html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FF9900'
html_pink = '#FF00FF'
  
ccnt = 0
files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.T08needstoberedone.nodups.cat']

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.3837706,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.4711887,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])

cRAh = np.array([13,13,13,17,18,16,16,9,9])
cRAm = np.array([24,24,24,57,21,4,4,10,10])
cRAs = np.array([48.9,20.3,49.2,19.3,32.3,23.5,26.5,8.5,45.0])
cDd = np.array([30,30,30,66,68,43,43,54,54])
cDm = np.array([11,12,58,31,27,4,14,18,22])
cDs = np.array([26,52,35,29,57,39,22,56,7])
centerRAs = (cRAh + (cRAm + (cRAs/60.0))/60.0)*360.0/24
centerDecs = cDd + (cDm + (cDs/60.0))/60.0
centerzs = np.array([0.76,0.76,0.69,0.69,0.82,0.89861,0.86531,1.1,1.1])

BCGfile = '/home/rumbaugh/BCGpositions.2.15.12.dat'
crBCG = read_file(BCGfile)
BCGRA = copy_colvals(crBCG,'col2')
BCGDec = copy_colvals(crBCG,'col3')

distBCG,distRGP,distgalmean = np.zeros(9),np.zeros(9),np.zeros(9)
distLW = distgalmean

FILE = open('paper.centers_table.4.30.12.dat','w')
for i in range(0,9):
    if ((i != 1) & (i != 2) & (i != 6) & (i != 8)): ccnt += 1
    if i == 5: ccnt += 1
    sfile = '/home/rumbaugh/%s'%(files[ccnt])
    crs = read_file(sfile)
    sID = copy_colvals(crs,'col1')
    sslit = copy_colvals(crs,'col3')
    smask = copy_colvals(crs,'col2')
    sRA = copy_colvals(crs,'col4')
    sDec = copy_colvals(crs,'col5')
    sLFCrB = copy_colvals(crs,'col6')
    sLFCiB = copy_colvals(crs,'col7')
    RA,Dec = np.copy(sRA),np.copy(sDec)
    if ((i == 5) | (i == 6)):
        ACSRA = copy_colvals(crs,'col14')
        ACSDec = copy_colvals(crs,'col15')
        sf606 = copy_colvals(crs,'col17')
        sf814 = copy_colvals(crs,'col18')
        srB,siB = np.copy(sf606),np.copy(sf814)
    else:
        srB,siB = np.copy(sLFCrB),np.copy(sLFCiB)
    szB = copy_colvals(crs,'col8')
    z = copy_colvals(crs,'col9')
    sz = np.copy(z)
    #vels = sz*3*10**5
    sq = copy_colvals(crs,'col11')
    q = np.copy(sq)
    g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]))
    if names[i] == "RXJ1757": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((smask != 'N200M1') | (sslit != 64)) & ((smask != 'N200M1') | (sslit != 67)) & ((smask != 'N200M1') | (sslit != 80)) & ((smask != 'N200M1') | (sslit != 83)))
    if names[i] == "RXJ1821": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((z < 0.80721891) | (z > 0.80721901)))
    if names[i] == "Cl1604A": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC2_06516") | (z > 0.9)))
    if names[i] == "Cl1604B": g = np.where((sq > 2.2) & (z > zlb[ccnt]) & (z < zub[ccnt]) & ((sID != "LFC_SC1_01472") | (z < 0.87)))
    g = g[0]
    dists = np.zeros(len(g))
    for j in range(0,len(g)): dists[j] = SphDist(sRA[g[j]],sDec[g[j]],RGalPeakRA[i],RGalPeakDec[i])
    gRGP = np.where(dists < srchdist[i])
    gRGP = gRGP[0]
    vels = (z[g[gRGP]]-biweight_loc(z[g[gRGP]]))*c/(1+z[g[gRGP]])
    avg_v = biweight_loc(vels)
    #sig = np.std(vels)
    #print 'a'
    sig = biweight_scale(vels)
    prevRGP = 9999
    gRGPtemp = np.arange(len(gRGP))
    meanRGP = biweight_loc(vels)
    velstemp = np.copy(vels)
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velstemp,meanRGP,sig)
        velstemp = (z[g[gRGP]]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[g[gRGP]])
        meanRGP = biweight_loc(velstemp[gRGPtemp])
        sig = biweight_scale(velstemp[gRGPtemp])
        #if ccnt == 6: print meanRGP,sig,velstemp[gRGPtemp]
    #print sID[g[gRGP[gRGPtemp]]]
    if ccnt == 6:
        lumweight = 10.0**(szB/(-2.5))
    elif ccnt == 5:
        lumweight = 10.0**(sf814/(-2.5))
    else:
        lumweight = 10.0**(siB/(-2.5))
    meanRA,meanDec,weighttot = 0.0,0.0,0.0
    for im in range(0,len(gRGPtemp)):
        meanRA += sRA[g[gRGP[gRGPtemp[im]]]]*lumweight[g[gRGP[gRGPtemp[im]]]]
        meanDec += sDec[g[gRGP[gRGPtemp[im]]]]*lumweight[g[gRGP[gRGPtemp[im]]]]
        weighttot += lumweight[g[gRGP[gRGPtemp[im]]]]
    meanRA /= weighttot
    meanDec /= weighttot
    FILEr = open('/home/rumbaugh/paper_marks.%s.6.27.12.reg'%(names[i]),'w')
    FILEr.write('global color=green font="helvetica 10 normal" select=1 highlite=1 edit=1 move=1 delete=1 include=1 fixed=0 width=2 source\nfk5\n')
    distLW[i] = 1000*SphDist(centerRAs[i],centerDecs[i],meanRA,meanDec)/srchdist[i]
    distBCG[i] = 1000*SphDist(centerRAs[i],centerDecs[i],BCGRA[i],BCGDec[i])/srchdist[i]
    distRGP[i] = 1000*SphDist(centerRAs[i],centerDecs[i],RGalPeakRA[i],RGalPeakDec[i])/srchdist[i]
    lwrah,lwram,lwras = dec2hms(meanRA)
    lwdecd,lwdecm,lwdecs = dec2dms(meanDec)
    bcgrah,bcgram,bcgras = dec2hms(BCGRA[i])
    bcgdecd,bcgdecm,bcgdecs = dec2dms(BCGDec[i])
    rgrah,rgram,rgras = dec2hms(RGalPeakRA[i])
    rgdecd,rgdecm,rgdecs = dec2dms(RGalPeakDec[i])
    lwdecdstr = '%i'%(lwdecd)
    if lwdecd < 10: lwdecdstr = '0%i'%(lwdecd)
    lwrahstr = '%i'%(lwrah)
    if lwrah < 10: lwrahstr = '0%i'%(lwrah)
    lwramstr = '%i'%(lwram)
    if lwram < 10: lwramstr = '0%i'%(lwram)
    lwrasstr = '%4.1f'%(lwras)
    if lwras < 10: lwrasstr = '0%3.1f'%(lwras)
    lwdecmstr = '%i'%(lwdecm)
    if lwdecm < 10: lwdecmstr = '0%i'%(lwdecm)
    lwdecsstr = '%4.1f'%(lwdecs)
    if lwdecs < 10: lwdecsstr = '0%3.1f'%(lwdecs)
    bcgdecdstr = '%i'%(bcgdecd)
    if bcgdecd < 10: bcgdecdstr = '0%i'%(bcgdecd)
    rgdecdstr = '%i'%(rgdecd)
    if rgdecd < 10: rgdecdstr = '0%i'%(rgdecd)
    bcgrahstr = '%i'%(bcgrah)
    if bcgrah < 10: bcgrahstr = '0%i'%(bcgrah)
    rgrahstr = '%i'%(rgrah)
    if rgrah < 10: rgrahstr = '0%i'%(rgrah)
    bcgramstr = '%i'%(bcgram)
    if bcgram < 10: bcgramstr = '0%i'%(bcgram)
    bcgrasstr = '%4.1f'%(bcgras)
    if bcgras < 10: bcgrasstr = '0%3.1f'%(bcgras)
    rgramstr = '%i'%(rgram)
    if rgram < 10: rgramstr = '0%i'%(rgram)
    rgrasstr = '%4.1f'%(rgras)
    if rgras < 10: rgrasstr = '0%3.1f'%(rgras)
    bcgdecmstr = '%i'%(bcgdecm)
    if bcgdecm < 10: bcgdecmstr = '0%i'%(bcgdecm)
    bcgdecsstr = '%4.1f'%(bcgdecs)
    if bcgdecs < 10: bcgdecsstr = '0%3.1f'%(bcgdecs)
    rgdecmstr = '%i'%(rgdecm)
    if rgdecm < 10: rgdecmstr = '0%i'%(rgdecm)
    rgdecsstr = '%4.1f'%(rgdecs)
    if rgdecs < 10: rgdecsstr = '0%3.1f'%(rgdecs)
    FILEr.write('point(%f,%f) # point=box color=cyan\n'%(BCGRA[i],BCGDec[i]))
    FILEr.write('point(%f,%f) # point=x color=blue\n'%(meanRA,meanDec))
    FILEr.write('point(%f,%f) # point=diamond color=magenta\n'%(RGalPeakRA[i],RGalPeakDec[i]))
    dBCGstr,dRGPstr,dLWstr = '%.0f'%(distBCG[i]),'%.0f'%(distRGP[i]),'%.0f'%(distLW[i])
    if distBCG[i] < 100: dBCGstr = '\phm{1}%s'%(dBCGstr)
    if distRGP[i] < 100: dRGPstr = '\phm{1}%s'%(dRGPstr)
    if distLW[i] < 100: dLWstr = '\phm{1}%s'%(dLWstr)
    FILE.write('%13s & %3s %s %s & %2s %s %s & %s & %3s %s %s & %2s %s %s & %s & %3s %s %s & %2s %s %s & %s'%(names[i],bcgrahstr,bcgramstr,bcgrasstr,bcgdecdstr,bcgdecmstr,bcgdecsstr,dBCGstr,rgrahstr,rgramstr,rgrasstr,rgdecdstr,rgdecmstr,rgdecsstr,dRGPstr,lwrahstr,lwramstr,lwrasstr,lwdecdstr,lwdecmstr,lwdecsstr,dLWstr))
    if i < 8: FILE.write(' \\\\\n')
    FILEr.close()
FILE.close()
