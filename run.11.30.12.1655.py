import matplotlib
from numpy import *
from scipy import *
from pylab import *
import scipy.optimize
import leastsq
import fitmodel
import arrconv
import matplotlib.pylab as pylab

try:
    rewrite
except NameError:
    rewrite = False


cr2 = loadtxt("SBfits.10.26.12.dat",dtype='string')
r0fitarr = arrconv.str2float(cr2[:,1])
r0fiterruarr = arrconv.str2float(cr2[:,2])
r0fiterrlarr = arrconv.str2float(cr2[:,3])
bkgfitarr = arrconv.str2float(cr2[:,7])
bkgfiterruarr = arrconv.str2float(cr2[:,8])
bkgfiterrlarr = arrconv.str2float(cr2[:,9])

ymax = array([0.35,0.25,0.1,0.16,0.09,0.12,0.12,0.5,0.35])

anninner = array([120,100,160,100,160,150,100,100,100])*0.5
ai = arrconv.float2int(anninner/2.5-1)
names = array(['RXJ1821','RXJ1757','Cl1324+3059','Cl1324+3011','Cl1324+3013','Cl1604A','Cl1604B','0910+5422','0910+5419'])
crb = loadtxt('/home/rumbaugh/DE_counts.bkg_data.10.13.12.dat',dtype='string')
bgcnts = arrconv.str2float(crb[:,1])
bgSBas = arrconv.str2float(crb[:,3])
bgann1,bgann2 = arrconv.str2float(crb[:,6]),arrconv.str2float(crb[:,7])
bgSBas_err = zeros(len(bgSBas))

sigma = np.array([921,652,880,914,819,619,811,675,1028])
crc = loadtxt("/home/rumbaugh/cc_out.6.29.12.nh.dat")
mpc = crc[:,11]*0.7
Hz = crc[:,4]*0.7

FILEfit = open('/home/rumbaugh/SBfits.10.30.12.dat','w')

for i in range(0,len(bgSBas)): 
    if ((names[i] != '0910+5419') & (names[i] != 'Cl1324+3013')):
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i]**2-bgann1[i]**2))
    else:
        bgSBas_err[i] = sqrt(bgcnts[i])/(pi*(bgann2[i-1]**2-bgann1[i-1]**2))
for i in range(0,len(names)):
    r0 = 0.18*(mpc[i]*60)
    r500 = (mpc[i]*60)*2*sigma[i]/(sqrt(500)*Hz[i])
    print names[i], r0
    cr = loadtxt('/home/rumbaugh/DE_counts_profile.%s.9.25.12.dat'%names[i])
    cnts_arr = cr[:,2]
    C = cnts_arr[ai[i]]
    NC = C-bgSBas[i]*pi*anninner[i]**2
    NCerr = sqrt(C+bgSBas_err[i]**2*pi**2*anninner[i]**2)
    cum_cnts = zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): cum_cnts[j] = sum(cnts_arr[0:j])
    SB_arr = cr[:,4]
    SB_err_arr = cr[:,6]
    ann_arr = cr[:,1]
    #if ((i == 0) | (i == 1) | (i == 2) | (i == 3) | (i == 6) | (i == 7) | (i == 8)):
    if i <= 77:
        ann_step = 10
        ann_arr = arange(12)*10+10
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    #elif ((i == 4)):
    elif ((i == 44)):
        ann_step = 10
        ann_arr = arange(12)*10+10
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[4*j+3]
    else:
        ann_step = 15
        ann_arr = arange(8)*15+15
        cnts_arrt = copy(cnts_arr)
        cnts_arr,SB_arr,SB_err_arr = zeros(len(ann_arr)),zeros(len(ann_arr)),zeros(len(ann_arr))
        for j in range(0,len(ann_arr)):
            cnts_arr[j] = cnts_arrt[6*j+5]
    cum_ncnts = zeros(len(cnts_arr))
    cum_ncnts_err = zeros(len(cnts_arr))
    for j in range(0,len(cnts_arr)): 
        cum_ncnts[j] = cnts_arr[j]-bgSBas[i]*pi*ann_arr[j]**2
        cum_ncnts_err[j] = sqrt(cum_cnts[j]+pi*pi*ann_arr[j]**4*bgSBas_err[i]**2)
    area_arr = zeros(len(ann_arr))
    area_arr[0] = pi*ann_arr[0]*ann_arr[0]
    for j in range(1,len(ann_arr)): area_arr[j] = pi*(ann_arr[j]*ann_arr[j]-ann_arr[j-1]*ann_arr[j-1])
    cnts2 = append(zeros(1),cnts_arr[0:len(cnts_arr)-1])
    SB_arr = (cnts_arr-cnts2)/area_arr
    for j in range(0,len(ann_arr)):
        SB_err_arr[j] = (sqrt(cnts_arr[j])+sqrt(cnts2[j]))/area_arr[j]
    if rewrite:
        FILE = open('/home/rumbaugh/DE_counts_profile.%s.10.16.12.dat'%names[i],'w')
        for j in range(0,len(ann_arr)): FILE.write('%3i %4.1f %f %f %f %f %f\n'%(ann_arr[j]*2,ann_arr[j],cnts_arr[j],0.25*SB_arr[j],SB_arr[j],0.25*SB_err_arr[j],SB_err_arr[j]))
        FILE.close()
    r0fit3 = r0fitarr[i]
    r0fit3erru = r0fiterruarr[i]
    r0fit3errl = r0fiterrlarr[i]
    bkgfit4par = bkgfitarr[i]
    bkginit = average(SB_arr[len(SB_arr)-3:len(SB_arr)])
    def model4par(x,a1,bkg):
        return (NC/(2*pi*a1**2))/(1.0-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1+x**2/(a1**2))**(-1.5)+bkg
    tcnts4 = 2*pi*(NC/(2*pi*r0fit3**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*r0fit3**2
    r500cnts = 2*pi*(NC/(2*pi*r0fit3**2))/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*r0fit3**2*(1-1.0/sqrt(1+r500**2*r0fit3**(-2)))
    #r500cnts = NC/(1.0-1.0/sqrt(1+anninner[i]**2*r0fit3**(-2)))*(1-1.0/sqrt(1+r500**2*r0fit3**(-2)))
    #NCcnts = 2*pi*Afit2par*r0fit**2*(1-1.0/sqrt(1+anninner[i]**2*r0fit**(-2)))
    Re = anninner[i]
    r0err = 0.5*(r0fit3erru+r0fit3errl)
    tcntserr = tcnts4*sqrt((NCerr/NC)**2+(Re**2*r0fit3**(-4)*(1+Re**2*r0fit3**(-2))**(-1.5)*(1-1.0/sqrt(1+Re**2*r0fit3**(-2)))**(-2)*r0err)**2)
    r500cntserr = r500cnts*sqrt((tcntserr/tcnts4)**2+(r500**2*r0fit3**(-4)*(1+r500**2*r0fit3**(-2))**(-1.5)*r0err)**2)
    r500cnts_nofit = NC*(1-1.0/sqrt(1+r500**2*r0**(-2)))/(1-1.0/sqrt(1+Re**2*r0**(-2)))
    r500cntserr_nofit = NCerr*(1-1.0/sqrt(1+r500**2*r0**(-2)))/(1-1.0/sqrt(1+Re**2*r0**(-2)))
    tcnts_nofit = NC/(1-1.0/sqrt(1+Re**2*r0**(-2)))
    tcntserr_nofit = NCerr/(1-1.0/sqrt(1+Re**2*r0**(-2)))

    def modelCr_fixNC(x,a1):
        return NC*1.0/(1-1.0/sqrt(1+anninner[i]**2*a1**(-2)))*(1-1.0/sqrt(1+x**2*a1**(-2)))
    def modelCr_2par(x,a0,a1):
        return 2*pi*a0*a1**2*(1-1.0/sqrt(1+x**2*a1**(-2)))

    #FILEfit.write('%13s %f %f %f %f %f %f %f %f %f %f %f %4.1f %f\n'%(names[i],Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,chisq1par,chisq2par,ann_step,r0))
    FILEfit.write('%13s %f %f  %f %f %f %f\n'%(names[i],NC,NCerr,r500cnts_nofit,r500cntserr_nofit,tcnts_nofit,tcntserr_nofit))
    #print '%12s:\n1-par: A: %f %f +%f \n2-par, fix. bkg: A: %f %f +%f r0: %f %f +%f NCcnt: %f NC: %f\n2-par, fix. cnts: A: %f %f +%f r0: %f %f +%f\n2-par, fc2: bkg: %f %f +%f r0: %f %f +%f\n1-par, fc3: r0: %f %f +%f\n1-par, fc4: r0: %f %f +%f\nchisq 1par: %f 2par, fix. bkg: %f 2par, fix. cnts: %f 2par, fc2: %f 1par, fc3: %f 1par, fc4: %f\ntcnts 1par: %f 2par, fix. bkg: %f 2par, fix. cnts: %f 2par, fc2: %f 1par, fc3: %f 1par, fc4: %f\n step: %4.1f r0: %f bkginit: %f bgSB: %f\n'%(names[i],Afit1par,Aerr1parl,Aerr1paru,Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,NCcnts,NC,Afit3par,Aerr3parl,Aerr3paru,r0fit2,r0fit2errl,r0fit2erru,bkgfit4par,bkgerr4parl,bkgerr4paru,r0fit3,r0fit3errl,r0fit3erru,r0fit4,r0fit4errl,r0fit4erru,r0fit5,r0fit5errl,r0fit5erru,chisq1par,chisq2par,chisq3par,chisq4par,chisq5par,chisq6par,tcnts1,tcnts2,tcnts3,tcnts4,tcnts5,tcnts6,ann_step,r0,bkginit,bgSBas[i])
    #print '%12s:\n2-par, fix. bkg: A: %f %f +%f r0: %f %f +%f NCcnt: %f NC: %f\n2-par, fc2: r0: %f %f +%f\ntcnts 1par: %f 2par, fix. bkg: %f 2par, fc2: %f\n step: %4.1f r0: %f bkginit: %f bgSB: %f\n'%(names[i],Afit2par,Aerr2parl,Aerr2paru,r0fit,r0fiterrl,r0fiterru,NCcnts,NC,bkgfit4par,bkgerr4parl,bkgerr4paru,r0fit3,r0fit3errl,r0fit3erru,tcnts1,tcnts2,tcnts4,ann_step,r0,bkginit,bgSBas[i])


    xdummy = linspace(0,500,600)

    rc('axes',linewidth=2)
    rc('font',size=16)
    #tick_params(which='major',length=8,width=2,labelsize=16)
    #tick_params(which='minor',length=4,width=1.5,labelsize=16)
    xlim(0,118)
    xlabel('Radius (arcseconds)',fontsize=25)
    if i < 4: 
        ylabel('Surface Brightness',fontsize=25)
    else:
        ylabel('(counts per sq. arcsecond)',fontsize=25)
    #plot(xdummy,model1par(xdummy,Afit1par),"y-",label='1-par Fit')
    #plot(xdummy,model2par(xdummy,Afit2par,r0fit),"r-",label='2-par Fit, fix. bkg')
    #plot(xdummy,model3par(xdummy,Afit3par,r0fit2),"g-",label='2-par Fit, fix. cnts')
    plot([anninner[i],anninner[i]],[-100,10000],linestyle='dashed',color='black')
    plot(xdummy,model4par(xdummy,r0fit3,bkgfit4par),"b-",label='2-par Fit, fc2')
    #plot(xdummy,model5par(xdummy,r0fit4),color="b",label='2-par Fit, bkginit')
    #plot(xdummy,model6par(xdummy,r0fit5),color='g',label='2-par Fit, bgSB')
    #legend()
    errorbar(ann_arr-0.5*ann_step,SB_arr,SB_err_arr,fmt='ro',lw=2,capsize=3,mew=1,ms=8)
    scatter(ann_arr-0.5*ann_step,SB_arr,s=5)
    xlim(0,118)
    ylim(0,ymax[i])
    if names[i] == 'Cl1324+3013':  ylim(0.01,ymax[i])
    savefig('/home/rumbaugh/fitted.DE_counts_profile.%s.11.30.12.png'%names[i])
    close()
    rc('axes',linewidth=2)
    rc('font',size=16)
    plot(xdummy,modelCr_fixNC(xdummy,r0),"b-",label='r0 = 180 kpc')
    plot(xdummy,modelCr_fixNC(xdummy,r0fit3),"r-",label='r0 fit (%3.0f kpc)'%(1000*r0fit3/(mpc[i]*60.)))
    plot([-10,500],[NC,NC],color='black',linestyle="dashed")
    legend(loc=4)
    xlim(0,400)
    #savefig('/home/rumbaugh/ncnts.fitted.DE_counts_profile.%s.10.22.12.png'%names[i])
    close()
FILEfit.close()
