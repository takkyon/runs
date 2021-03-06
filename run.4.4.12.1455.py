execfile("/home/rumbaugh/FindCloseSources.py")
execfile("/home/rumbaugh/scale_estimators.py")
execfile("/home/rumbaugh/DStest.py")
execfile('/home/rumbaugh/angconvert.py')
import matplotlib
import matplotlib.pylab as pylab
import random as rand
c = 3.0*10**5

def sigclip(data,mean,sig,sigthresh=3.0):
    gsc = np.where((data < mean + sigthresh*sig) & (data > mean - sigthresh*sig))
    gsc = gsc[0]
    #if ccnt == 6:
    #    print mean,sig,data[gsc]
    return gsc

degree_symbol = unichr(176)
html_purp = '#9933FF'
html_teal = '#33FFFF'
html_brwn = '#996600'
html_orng = '#FFCC00'
html_pink = '#FF00FF'

#zlb = [0.82,0.65,0.68,0.80,0.84,0.84,1.0]
#zub = [0.87,0.79,0.71,0.84,0.96,0.96,1.2]
zlb = [0.82,0.65,0.68,0.805,0.84,0.84,1.0]
zub = [0.87,0.79,0.71,0.83,0.96,0.96,1.2]

try:
    skipMC
except NameError:
    skipMC = 1
try:
    writeMC
except NameError:
    writeMC = 1

strucs = np.array(['Cl1324','Cl1324','Cl1324','RXJ1757','NEP5281','Cl1604','Cl1604','0910','0910'])
chandraIDs = np.array(['9404+9836','9404+9836','9403+9840','10443+11999','10444+10924','6932','6932','2227+2452','2227+2452'])
names = np.array(['Cl1324+3011','Cl1324+3013','Cl1324+3059','RXJ1757','RXJ1821','Cl1604A','Cl1604B','RXJ0910+5419','RXJ0910+5422'])

#files = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat','FINAL.nep5281.deimos.gioia.feb2010.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.nh.cat','FINAL.spectroscopic.autocompile.blemaux.0910.notsofinal.plusT08.cat']
files = ['FINAL.SG0023.deimos.lris.feb2012.nodups.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.spectroscopic.autocompile.N200.blemaux.feb2012.nh.cat','FINAL.nep5281.deimos.gioia.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectra.sc1604.wcompletenessmasks.feb2012.nodups.nh.cat','FINAL.spectroscopic.autocompile.blemaux.sc0910.mar2012.T08needstoberedone.nodups.cat']
#RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.3801,241.08946,241.09890,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
#RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.4651,43.07613,43.23550,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])
RGalPeakRA = np.array([201.20353640,201.09003360,201.20748930,(17+(57+18.769/60)/60)*360/24.0,275.38377060,241.089458,241.0988952,(360.0/24)*(9+(10+(4.168/60))/60.0),(360.0/24)*(9+(10+(47.686/60))/60.0)])
RGalPeakDec = np.array([30.19424680,30.21497820,30.97371310,66+(31+37.46/60)/60.0,68.47118870,43.076133,43.2355028,(54+(18+(54.21/60))/60.0),(54+(22+(13.82/60))/60.0)])
names2 = np.array(['RXJ1757','RXJ1821','Cl0910+5422'])
#names = np.array(['nep200','nep5281','cl0910'])

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
BCGzs = copy_colvals(crBCG,'col7')
srchdist = np.array([3.23,3.23,3.36,3.36,3.12,3.06,3.09,2.92,2.92])*0.7
ccnt = 0

rsb = np.array([1.777,1.325,1.84,1.203,1.305,3.182,1.7563])
rsm = np.array([0.0229,0.0084,0.0319,0.0012,0.00485,0.063,0.02392])
rsSTD = np.array([0.0625,0.0735,0.0576,0.0413,0.0813,0.0907,0.0455])
rsNSTD = np.array([3.0,2.0,3.0,3.0,2.0,2.0,3.0])
ymaxes = np.array([20,20,20,20,20,20,20,20,20]) 
#ccnt = np.array([2,3,6])
ccnt=0
#FILEo = open('/home/rumbaugh/DStest_output.3.16.12.dat','w')
#FILE3 = open('/home/rumbaugh/veldisp_output.3.20.12.dat','w')
for i in range(0,len(names)):
    #cr = read_file('/home/rumbaugh/%s.info.1Mpc.withvels'%(names[i]))
    #royID = copy_colvals(cr,'col1')
    #RA = copy_colvals(cr,'col2')
    #Dec = copy_colvals(cr,'col3')
    #z = copy_colvals(cr,'col4')
    #vels = copy_colvals(cr,'col5')
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
        sig,sige = biweight_scale(velstemp[gRGPtemp],ConfInv=1)
        #if ccnt == 6: print meanRGP,sig,velstemp[gRGPtemp]
    #print sID[g[gRGP[gRGPtemp]]]
    print '%s sig = %f +/- %f using %i gals\n'%(names[i],sig,sige,len(gRGPtemp))
    gq = np.where(sq > 2.2)
    gq = gq[0]
    dists2 = np.zeros(len(gq))
    for j in range(0,len(gq)): dists2[j] = SphDist(sRA[gq[j]],sDec[gq[j]],RGalPeakRA[i],RGalPeakDec[i])
    gd2 = np.where(dists2 < srchdist[i])
    velstemp2 =  (z[gq]-biweight_loc(sz[g[gRGP[gRGPtemp]]]))*(3.0*10**5)/(1+sz[gq])
    pylab.hist(velstemp2[gd2],bins=30,range=[-4000,4000])
    #pylab.savefig('/home/rumbaugh/zhist.temp.%s.4.2.12.png'%(names[i]))
    pylab.close('all')

    #print 'a'
    gRGP2 = np.where((velstemp2 < 3000) & (velstemp2 > -3000) & (dists2 < srchdist[i]))
    gRGP2 = gRGP2[0]
    gRGPtemp = np.arange(len(gRGP2))
    meanRGP = biweight_loc(velstemp2[gRGP2])
    velstemp2 = velstemp2[gRGP2]
    sig = biweight_scale(velstemp2)
    prevRGP=9999
    #print 'a'
    while len(gRGPtemp) < prevRGP:
        prevRGP = len(gRGPtemp)
        gRGPtemp = sigclip(velstemp2,meanRGP,sig)
        velstemp = (z[gq[gRGP2]]-biweight_loc(sz[gq[gRGP2[gRGPtemp]]]))*(3.0*10**5)/(1+sz[gq[gRGP2]])
        meanRGP = biweight_loc(velstemp2[gRGPtemp])
        sig,sige = biweight_scale(velstemp2[gRGPtemp],ConfInv=1)
    FILEz = open('/home/rumbaugh/rostat/redshifts.%s.rostat_input.4.8.12.dat','w')
    for iz in range(0,len(gRGPtemp)): FILEz.write(sz[gq[gRGP2[gRGPtemp[iz]]]] + '\n')
    FILEz.close()
    print '%s newsig = %f +/- %f using %i gals\n'%(names[i],sig,sige,len(gRGPtemp))
