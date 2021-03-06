import numpy as np
import os
os.chdir('/mnt/data3/rumbaugh/VLA/AF377/data')

dates = ['2.01.01','2.05.01','2.07.01','2.08.01','2.12.01','2.14.01','2.16.01','2.18.01','2.21.01','2.22.01','2.26.01','3.06.01','3.14.01','3.16.01','3.18.01','3.21.01','3.23.01','3.26.01','3.28.01','3.30.01','4.02.01','4.05.01','4.09.01','4.10.01','4.14.01','4.17.01','4.19.01','4.24.01','4.26.01','4.30.01','5.05.01','5.08.01','5.12.01','5.14.01','5.17.01','5.20.01','5.25.01','5.28.01']

ant_dict = {'2.01.01': 'VA04,VA13,VA17','2.05.01': 'VA13,VA15','2.07.01': 'VA09,VA18,VA28','2.08.01': 'VA09, VA17, VA18, VA20, VA28','2.12.01': 'VA09, V10, VA12, VA19, VA22, VA23','2.14.01': 'VA02, VA10, VA12, VA19, VA22, VA28','2.16.01': 'VA02, VA10, VA12, VA14','2.18.01': 'VA02, VA10, VA12, VA13, VA22, VA26','2.21.01': 'VA02, VA10, VA12, VA18, VA19, VA22, VA27','2.22.01': 'VA04, VA06, VA09, VA19, VA27','2.26.01': 'VA01, VA05, VA13, VA25, VA27','3.06.01': 'VA02, VA05, VA10, VA18, VA19, VA20, VA27','3.14.01': 'VA05','3.18.01': 'VA03, VA05, VA10, VA20, VA25, VA28','3.21.01': 'VA04, VA05, VA07, VA10, VA13, VA20, VA25','3.23.01': 'VA01, VA05, VA10, VA12, VA14, VA18, VA20, VA25','3.26.01': 'VA01, VA05, VA10, VA12, VA14, VA18, VA20, VA25, VA26, VA27','3.28.01': 'VA01, VA05, VA10, VA12, VA14, VA18, VA20, VA25','3.30.01': 'VA01, VA05, VA10, VA12, VA14, VA18, VA20, VA25','4.02.01': 'VA05, VA14, VA16, VA18, VA25','4.05.01': 'VA01, VA04, VA10, VA12, VA18, VA20, VA23','4.09.01': 'VA01, VA04, VA10, VA12, VA14, VA18, VA20, VA23','4.10.01': 'VA04, VA05, VA10, VA18, VA20, VA21, VA24','4.14.01': 'VA04, VA18, VA20','4.17.01': 'VA04, VA10, VA18, VA20, VA23','4.19.01': 'VA04, VA18, VA20, VA23, VA25','4.24.01': 'VA04, VA09, VA14, VA18, VA25','4.26.01': 'VA04, VA25','4.30.01': 'VA04, VA16, VA25','5.05.01': 'VA04','5.08.01': 'VA02, VA04, VA25','5.12.01': 'VA09, VA25','5.14.01': 'VA22, VA25, VA26','5.17.01': 'VA22','5.20.01': 'VA09, VA22, VA25','5.25.01': 'VA05, VA14, VA18','5.28.01': 'VA14'}

calibrators = ['1035+564','0424+020','1041+061','1130+382','1150+242','0710+475']
sources = ['0414+573','1030+074','1127+385','1152+199','0712+472']
CSOs = ['1244+408','1400+621']

calDict = {'0414+573':'0424+020','1030+074':'1041+061','1152+199':'1150+242','1127+385':'1130+382','0712+472':'0710+475'}

applyind = True
for date in dates:
    spwstr = ''
    os.system("rm -rf *%s*"%date)
    os.system("rm -rf *cal")
    vis = 'af377_%s.ms'%date
    curvis = vis
    tflagdata(vis=curvis,antenna=ant_dict[date])
    antenna = ''
    execfile('/mnt/data3/rumbaugh/VLA/scripts/calib_VLA.py')
for date in dates:
    vis = 'af377_%s.ms'%date
    curvis = vis
    for source in sources:
        outbase = 'af377_%s'%date
        lensname = source
        fieldnum = source
        execfile("/mnt/data3/rumbaugh/VLA/scripts/export_lens.py")
    for source in CSOs:
        outbase = 'af377_%s'%date
        lensname = source
        fieldnum = source
        execfile("/mnt/data3/rumbaugh/VLA/scripts/export_lens.py")
