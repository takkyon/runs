from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *

indir = '/local3/rumbaugh/LRISdata/2011oct25/'
bgroups,rgroups=7,7
obsdata = numpy.loadtxt('/local3/rumbaugh/LRISdata/2011oct25/obslog.dat',dtype='string')
obsshape = numpy.shape(obsdata)
obs_rows = obsshape[0]
obs_nums = numpy.zeros(obs_rows,dtype='int16')
for i in range(0,obs_rows): obs_nums[i] = int(obsdata[i,1])
for i in range(5,5):
    mslit = 0
    if i == 0:
        arc = 6
        flat = 5
        images = [3,8]
        #didn't work
    if i == 1:
        #done
        arc = 11
        flat = 10
        images = [13,12,9]
    if i == 2:
        #didn't work
        arc = 18
        flat = 17
        images = [16,19,14]
    if i == 3:
        #didn't work
        arc = 25
        flat = 24
        images = [23]
    if i == 4:
        #didn't work
        arc = 25
        flat = 28
        images = [26,27]
    if i == 5:
        arc = 39
        flat = 35
        images = [33,34,37,38,41]
        mslit = 1
    if i == 6:
        #didnt work
        arc = 44
        flat = 43
        images = [42]
    images_num = numpy.zeros(len(images),dtype='int16')
    for j in range(0,len(images)): images_num[j] = int(obsdata[images[j],1])
    flat_num = int(obsdata[flat,1])
    arc_num = int(obsdata[arc,1])
    pref = obsdata[images[0],0]
    outname = '%s_b_noCRsub.3.30.12'%(obsdata[images[0],2])
    #slitID(indir,pref,[flat,arc,110],outname,side='top',slits=[[50,100]])
    print flat_num,arc_num,images_num
    if mslit == 0:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top',slits=[[100,200]])
        #slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='bottom',slits=[[0,500]])
    else:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top')
    oldName = None
    sf = True
    for img in images_num:
        newName = '%s_%2d'%(outname,img)
        XSolve(outname,newName,indir,pref,[flat_num,arc_num,img])
        SlitCross(newName)
        WaveSolve(newName,oldName,showFit=sf)
        resample(newName,nobgsub=True,doCR=False,clobber=True)
        oldName = newName
for i in range(1,2):
    mslit = 0
    if i == 0:
        #done
        arc = 71
        flat = 72
        #images = [68,73]
        images = [73]
    if i == 1:
        #done
        arc = 76
        flat = 75
        images = [74,77]
    if i == 2:
        #done
        arc = 88
        flat = 82
        images = [78,79,80,81,83]
    if i == 3:
        #did it work?
        arc = 88
        flat = 87
        images = [86]
    if i == 4:
        #i think its done
        arc = 91
        flat = 90
        images = [89]
    if i == 5:
        #there's no arc for it
        mslit = 1
        arc = 102
        flat = 98
        images = [96,97,100,101,104]
    if i == 6:
        #done
        arc = 101
        flat = 100
        images = [99,98]
    images_num = numpy.zeros(len(images),dtype='int16')
    for j in range(0,len(images)): images_num[j] = int(obsdata[images[j],1])
    flat_num = int(obsdata[flat,1])
    arc_num = int(obsdata[arc,1])
    print arc_num,flat_num,images_num
    pref = obsdata[images[0],0]
    outname = '%s_r.5.18.12_200-400'%(obsdata[images[0],2])
    #slitID(indir,pref,[flat,arc,110],outname,side='top',slits=[[50,100]])
    if mslit == 0:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top',slits=[[200,400]])
        #slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top',slits=[[50,400]])
    else:
        slitID(indir,pref,[flat_num,arc_num,images_num[0]],outname,side='top')
    oldName = None
    sf = True
    for img in images_num:
        newName = '%s_%2d'%(outname,img)
        XSolve(outname,newName,indir,pref,[flat_num,arc_num,img])
        SlitCross(newName)
        WaveSolve(newName,oldName,showFit=sf)
        #resample(newName,nobgsub=True,doCR=False,clobber=True)
        resample(newName,nobgsub=True,clobber=True)
        oldName = newName

