execfile('/home/rumbaugh/LoadVLA_2001.py')
execfile('/home/rumbaugh/Load1938.py')
import matplotlib.pyplot as plt

date = '4.6.14'

CSO1days,CSO1S,CSO2days,CSO2S = LoadVLA_2001(loadCSOs=True)

CSO1S /= np.mean(CSO1S)
CSO2S /= np.mean(CSO2S)

d0 = CSO1S[0]
CSO1S -= d0
CSO2S -= d0

plt.figure(1)
plt.rc('axes',linewidth=2)
plt.fontsize = 14
plt.tick_params(which='major',length=8,width=2,labelsize=14)
plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
plt.clf()
plt.plot(CSO1days,CSO1S,lw=2,color='r',label='CSO 1244')
plt.plot(CSO2days,CSO2S,lw=2,color='b',ls='dashed',label='CSO 1400')
plt.legend(loc=3)
plt.scatter(CSO1days,CSO1S,color='r')
plt.scatter(CSO2days,CSO2S,color='b')
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_VLA_2001.normfluxplot.3.17.14.png')

CSO_out_flux_dict,CSO_time_dict,CSO_norm_flux_dict = Load1938(returnCSOs=True)

CSOs = CSO_out_flux_dict.keys()

minday = np.zeros(len(CSOs))
for CSO,i in zip(CSOs,np.arange(len(CSOs))):
    minday[i] = np.min(CSO_time_dict[CSO])
    CSO_out_flux_dict[CSO] /= np.mean(CSO_out_flux_dict[CSO])
d0 = np.min(minday)

markers = np.array(["o","<",">","D","s","p","*","h","+","x"])
colors = np.array(['b','r','c','m','k','b','r','c','m','k'])
lsarr = np.array(['','','','','','solid','dashed','','','dotted'])
sizes = np.array([1.,1.,1.,1.,1.,1.,1.,1.,3.,1.])*25

plt.clf()

CSO_ind_dict = {x: np.zeros(len(CSO_time_dict[x])) for x in CSO_time_dict}
for CSO in CSO_ind_dict:
    for ti in range(0,len(CSO_ind_dict[CSO])):
        gi = np.where(np.fabs(CSO_time_dict[CSO][ti]-CSO_time_dict['J1816+3457']) < 5000)[0]
        if len(gi) > 1: print 'greater than 1'
        CSO_ind_dict[CSO][ti] = gi[0]
medians = np.zeros(19)
for ind in range(0,19):
    tmp_arr = np.array([])
    for CSO in CSO_ind_dict: 
        if ind in CSO_ind_dict[CSO]: tmp_arr = np.append(tmp_arr,CSO_out_flux_dict[CSO][np.where(CSO_ind_dict[CSO] == ind)[0][0]])
    medians[ind] = np.median(tmp_arr)

for CSO,i in zip(['J1816+3457','J1823+7938','J1945+7055'],[5,6,9]):
    g = np.where((CSO_time_dict[CSO] < CSO_time_dict['J1816+3457'][11]-86400) | (CSO_time_dict[CSO] > CSO_time_dict['J1816+3457'][11]+86400))[0]
    plt.plot((CSO_time_dict[CSO][g]-d0)/86400,CSO_out_flux_dict[CSO][g],color=colors[i],ls=lsarr[i],lw=2)
for CSO,i in zip(np.sort(CSOs),np.arange(len(CSOs))):
    g = np.where((CSO_time_dict[CSO] < CSO_time_dict['J1816+3457'][11]-86400) | (CSO_time_dict[CSO] > CSO_time_dict['J1816+3457'][11]+86400))[0]
    plt.scatter((CSO_time_dict[CSO][g]-d0)/86400,CSO_out_flux_dict[CSO][g],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
plt.ylim(0.95,1.03)
plt.xlim(-50,95)
plt.xlabel('Days')
plt.ylabel('Relative Flux')
plt.legend(loc=2)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.fluxplot.%s.png'%date)

plt.clf()


for CSO,i in zip(['J1816+3457','J1823+7938','J1945+7055'],[5,6,9]):
    g = np.where((CSO_time_dict[CSO] < CSO_time_dict['J1816+3457'][11]-86400) | (CSO_time_dict[CSO] > CSO_time_dict['J1816+3457'][11]+86400))[0]
    plt.plot((CSO_time_dict[CSO][g]-d0)/86400,CSO_out_flux_dict[CSO][g]/medians[g],color=colors[i],ls=lsarr[i],lw=2)
for CSO,i in zip(np.sort(CSOs),np.arange(len(CSOs))):
    g = np.where((CSO_time_dict[CSO] < CSO_time_dict['J1816+3457'][11]-86400) | (CSO_time_dict[CSO] > CSO_time_dict['J1816+3457'][11]+86400))[0]
    plt.scatter((CSO_time_dict[CSO][g]-d0)/86400,CSO_out_flux_dict[CSO][g]/medians[g],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
plt.ylim(0.93,1.1)
plt.xlim(-50,95)
plt.xlabel('Days')
plt.ylabel('Normalized Flux')
plt.legend(loc=2)
plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.normfluxplot.%s.png'%date)
