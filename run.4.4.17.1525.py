import numpy as np
import matplotlib
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/pythonscripts/KStest.py')

cro=np.loadtxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_90.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crno=np.loadtxt('/home/rumbaugh/DR7_notOVV_maxvar.thresh_90.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crob=np.loadtxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_90.buffer_10.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crnob=np.loadtxt('/home/rumbaugh/DR7_notOVV_maxvar.thresh_90.buffer_10.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})

crob45=np.loadtxt('/home/rumbaugh/DR7_OVV_maxvar.thresh_90.buffer_45.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})
crnob45=np.loadtxt('/home/rumbaugh/DR7_notOVV_maxvar.thresh_90.buffer_45.dat',dtype={'names':('SDSSNAME','maxvar','medvar'),'formats':('|S24','f8','f8')})


matplotlib.rcParams['font.size']=16
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=4)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(crno['medvar'],weights=np.full(len(crno),1./len(crno)),range=(0,0.6),bins=24,color='k',edgecolor='k',facecolor='None',lw=2)
b=ax.hist(cro['medvar'],weights=np.full(len(cro),1./len(cro)),range=(0,0.6),bins=24,color='r',edgecolor='r',facecolor='None',lw=2)
p=ax2.plot(np.sort(crno['medvar']),(np.arange(len(crno))+1.)/len(crno),lw=3,color='k',ls='dashed',label='FIRST_FR_TYPE=0')
q=ax2.plot(np.sort(cro['medvar']),(np.arange(len(cro))+1.)/len(cro),lw=3,color='r',label='FIRST_FR_TYPE>0')
leg=plt.legend(loc='center right',frameon=False)
for text in leg.get_texts():
    if text.properties()['text']=='FIRST_FR_TYPE>0': text.set_color('r')
ax.set_xlabel('Median Variation (magnitudes)')
ax.set_ylabel('Fraction of Objects')
ax2.set_ylabel('Cumulative Fraction')
plt.xlim(0,0.6)
ax.set_ylim(0.001,0.25)
ax2.set_ylim(0.0001,1)
ax2.set_yticks(ax2.get_yticks()[1:])
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/OVV_medvar_comp.thresh_90.4.4.17.png')
KStest(crno['medvar'],cro['medvar'])

fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=4)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(crnob['medvar'],weights=np.full(len(crnob),1./len(crnob)),range=(0,0.6),bins=24,color='k',edgecolor='k',facecolor='None')
b=ax.hist(crob['medvar'],weights=np.full(len(crob),1./len(crob)),range=(0,0.6),bins=24,color='r',edgecolor='r',facecolor='None')
p=ax2.plot(np.sort(crnob['medvar']),(np.arange(len(crnob))+1.)/len(crnob),lw=3,color='k',ls='dashed',label='FIRST_FR_TYPE=0')
q=ax2.plot(np.sort(crob['medvar']),(np.arange(len(crob))+1.)/len(crob),lw=3,color='r',label='FIRST_FR_TYPE>0')
plt.legend(loc='center right')
ax.set_xlabel('Median Variation (magnitudes)',fontsize=20)
ax.set_ylabel('Fraction of Objects',fontsize=20)
ax2.set_ylabel('Cumulative Fraction',fontsize=20)
plt.xlim(0,0.6)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/OVV_medvar_comp.thresh_90.buffer_10.4.4.17.png')

KStest(crnob['medvar'],crob['medvar'])
fig=plt.figure(1)
fig.clf()
plt.clf()
plt.rc('axes',linewidth=4)
ax=fig.add_subplot(1,1,1)
ax2=ax.twinx()
ax.tick_params(which='major',length=12,width=3,labelsize=17)
ax.tick_params(which='minor',length=6,width=2,labelsize=17)
ax2.tick_params(which='major',length=12,width=3,labelsize=17)
ax2.tick_params(which='minor',length=6,width=2,labelsize=17)
a=ax.hist(crnob45['medvar'],weights=np.full(len(crnob45),1./len(crnob45)),range=(0,0.6),bins=24,color='k',edgecolor='k',facecolor='None')
b=ax.hist(crob45['medvar'],weights=np.full(len(crob45),1./len(crob45)),range=(0,0.6),bins=24,color='r',edgecolor='r',facecolor='None')
p=ax2.plot(np.sort(crnob45['medvar']),(np.arange(len(crnob45))+1.)/len(crnob45),lw=3,color='k',ls='dashed',label='FIRST_FR_TYPE=0')
q=ax2.plot(np.sort(crob45['medvar']),(np.arange(len(crob45))+1.)/len(crob45),lw=3,color='r',label='FIRST_FR_TYPE>0')
plt.legend(loc='center right')
ax.set_xlabel('Median Variation (magnitudes)',fontsize=20)
ax.set_ylabel('Fraction of Objects',fontsize=20)
ax2.set_ylabel('Cumulative Fraction',fontsize=20)
plt.xlim(0,0.6)
fig.savefig('/home/rumbaugh/var_database/Y3A1/plots/OVV_medvar_comp.thresh_90.buffer_45.4.4.17.png')

KStest(crnob['medvar'],crob['medvar'])
