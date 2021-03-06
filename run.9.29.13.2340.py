import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

dates = ['2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.06.01','3.14.01','3.16.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

days4months_dict  = {5: 28, 4: 28+30, 3: 28+30+31, 2: 28+30+31+28, 1: 28+30+31+28+31}

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

for source in sources:
    FILE = open('/home/rumbaugh/EVLA/light_curves/VLA_lc_2001_%s.dat'%source,'w')
    for date in dates:
        if date[1] == '.':
            month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
        else:
            month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
        daytot = 2058-days4months_dict[month]+day
        if date not in ['3.06.01','3.16.01','4.10.01']:
            FILE.write('%f'%daytot)
            cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!')
            num_img = np.shape(cr)[0]
            for img in range(0,num_img):
                fluxstr = cr[img][0]
                FILE.write(' ' + fluxstr[:len(fluxstr)-1])
            FILE.write('\n')
    FILE.close()
for source in CSOs:
    FILE = open('/home/rumbaugh/EVLA/light_curves/VLA_lc_2001_%s.dat'%source,'w')
    for date in dates:
        if date[1] == '.':
            month,day,year = int(date[0]),int(date[2:4]),int(date[5:])+2000
        else:
            month,day,year = int(date[0:2]),int(date[3:5]),int(date[6:])+2000
        daytot = 2058-days4months_dict[month]+day
        if date not in ['3.06.01','3.16.01','4.10.01']:
            FILE.write('%f'%daytot)
            cr = np.loadtxt('/mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit.%s.fixpos.%s.mod'%(source,date),dtype='string',comments='!')
            fluxstr = cr[0]
            FILE.write(' ' + fluxstr[:len(fluxstr)-1])
            FILE.write('\n')
    FILE.close()
            
            
