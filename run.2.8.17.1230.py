import numpy as np
import matplotlib.pyplot as plt
execfile('/home/rumbaugh/set_spec_dict.py')
fig=plt.figure(1)
plt.clf()

execfile('/home/rumbaugh/pythonscripts/set_plt_params.py')

cr=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.clus_sigs.dat',dtype={'names':('field','cluster','sigall','saerr','Nsa','sigcut','scerr','Nsc','sigblue','sberr','Nsb','sigred','srerr','Nsr'),'formats':('|S20','|S20','f8','f8','i8','f8','f8','i8','f8','f8','i8','f8','f8','i8')})
cr=cr[cr['field']!='cl0849']

crv=np.loadtxt('/home/rumbaugh/Chandra/ORELSE.veldiffs.dat',dtype={'names':('field','cluster','blueVC','redVC','perc','percBS'),'formats':('|S12','|S20','f8','f8','f8','f8')})
crv=crv[crv['field']!='cl0849']
veldiffs=(crv['redVC']-crv['blueVC'])*3.0*10.**5/(1.+crv['redVC'])

Tarr=np.zeros((len(cr),9),dtype='object')
namedict={'Cluster_A': 'SC1604A','Cluster_B':'SC1604B','Cluster_D':'SC1604D','Cluster_I':'SC1324I'}
for i in range(0,len(cr)):
    clus=cr['cluster'][i]
    try:
        Tarr[:,0][i]=namedict[clus]
    except KeyError:
        Tarr[:,0][i]=clus
    Tarr[i][1]='%.0f+/-%.0f'%(cr['sigall'][i],cr['saerr'][i])
    Tarr[i][2]=cr['Nsa'][i]
    if ((cr['Nsb'][i]>=10)&(cr['Nsr'][i]>=10)):
        Tarr[i][3:]=np.array(['%.0f+/-%.0f'%(cr['sigblue'][i],cr['sberr'][i]),cr['Nsb'][i],'%.0f+/-%.0f'%(cr['sigred'][i],cr['srerr'][i]),cr['Nsr'][i],veldiffs[i],crv['perc'][i]*100])
    else:
        Tarr[i][3:]='-'
    

ax=fig.add_subplot(111)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
colwidrat=0.4
wcol=1./(5.5+3*colwidrat)
scol=colwidrat*wcol
ax.table(cellText=Tarr,loc='center',colLabels=('Cluster','Full Disp.','N','Blue Disp.','N','Red Disp.','N','Vel. Diff.','P'),colWidths=(wcol,wcol,scol,wcol,scol,wcol,scol,wcol,wcol/2))
plt.savefig('/home/rumbaugh/Chandra/plots/veldisp_table.2.8.17.png')
