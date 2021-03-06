execfile('/home/rumbaugh/LoadEVLA_2011.py')

try:
    defsize
except NameError:
    defsize = 50

CSOmask = (['Late',1,'18'],['Early',2,'16'])

CSOs_dict = LoadEVLA_2011('CSOs')
import matplotlib.pyplot as plt

t0 = CSOs_dict['time']['Late'][0]

CSOs_dict['time']['Early'] -= t0
CSOs_dict['time']['Late'] -= t0

date = '2.14.15'

CSOs_means = {'Late': dict(zip(CSOs_dict['Late'],np.zeros(len(CSOs_dict['Late'])))), 'Early': dict(zip(CSOs_dict['Early'],np.zeros(len(CSOs_dict['Late']))))}

markers = np.array(["o","<",">","D","s","p","*","h","x"])
colors = np.array(['b','r','c','m','k','b','r','c','m'])
lsarr = np.array(['','','','','','solid','dashed','','dotted'])
sizes = np.array([1.,1.,1.,1.,1.,1.,1.,1.,1.])*defsize


for EorL in ['Late','Early']:
    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)

    if EorL == 'Late':
        for CSO,i in zip(['J1816+3457','J1823+7938','J1945+7055'],[5,6,8]):
            g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
            CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
            plt.plot(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO],color=colors[i],ls=lsarr[i],lw=2)
            print CSO,len(g)
    for CSO,i in zip(np.sort(CSOs_dict[EorL].keys()),np.arange(len(CSOs_dict[EorL]))):
        g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
        CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
        plt.scatter(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Normalized Flux',fontsize=14)
    plt.legend(loc=2)
    plt.xlim(100-t0,260-t0)
    if EorL == 'Late':
        plt.ylim(0.973,1.023)
    plt.axhline(y=1.0,lw=2,ls='dashed',color='k',label=None)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.%s_block.fluxplot.%s.png'%(EorL,date))
    plt.clf()

    plt.figure(1)
    plt.clf()
    plt.rc('axes',linewidth=2)
    plt.fontsize = 14
    plt.tick_params(which='major',length=8,width=2,labelsize=14)
    plt.tick_params(which='minor',length=4,width=1.5,labelsize=14)
    CSO_meds = np.zeros(len(CSOs_dict['time'][EorL]))
    gts = np.argsort(CSOs_dict['time'])
    for i in range(0,len(CSO_meds)):
        CSOntemp = np.zeros(len(CSOs_dict[EorL].keys()))
        for j in range(0,len(CSOntemp)):
            CSO = CSOs_dict[EorL].keys()[j]
            gCSOtmp = np.where(CSOs_dict[EorL][CSO] > 0)[0]
            CSOntemp[j] = CSOs_dict[EorL][CSO][i]/np.mean(CSOs_dict[EorL][CSO][gCSOtmp])
        if len(CSOntemp[CSOntemp > 0]) > 0: CSO_meds[i] = np.median(CSOntemp[CSOntemp > 0])
    #g = np.where(CSO_meds > 0)[0]
    if EorL == 'Late':
        for CSO,i in zip(['J1816+3457','J1823+7938','J1945+7055'],[5,6,8]):
            g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
            CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
            plt.plot(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO]/CSO_meds[g],color=colors[i],ls=lsarr[i],lw=2)
    for CSO,i in zip(np.sort(CSOs_dict[EorL].keys()),np.arange(len(CSOs_dict[EorL]))):
        g = np.where(CSOs_dict[EorL][CSO] > 0)[0]
        CSOs_means[EorL][CSO] = np.mean(CSOs_dict[EorL][CSO][g])
        plt.scatter(CSOs_dict['time'][EorL][g],CSOs_dict[EorL][CSO][g]/CSOs_means[EorL][CSO]/CSO_meds[g],marker=markers[i],color=colors[i],label=CSO,s=sizes[i])
    plt.xlabel('Days',fontsize=14)
    plt.ylabel('Relative Flux',fontsize=14)
    plt.legend(loc=2)
    plt.xlim(100-t0,260-t0)
    if EorL == 'Late':
        plt.ylim(0.983,1.0165)
    else:
        plt.ylim(0.988,1.012)
    plt.axhline(y=1.0,lw=2,ls='dashed',color='k',label=None)
    plt.savefig('/home/rumbaugh/EVLA/light_curves/plots/CSOs_EVLA_2011.%s_block.normplot.%s.png'%(EorL,date))
    plt.clf()

    
