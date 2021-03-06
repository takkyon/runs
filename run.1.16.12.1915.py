import math as m
import numpy as np
import random as rand
import matplotlib
import matplotlib.pylab as pylab

try:
    numgals
except NameError:
    numgals = 20

try:
    Mpctoas
except NameError:
    Mpctoam = 3*0.7

try:
    maxr
except NameError:
    maxr = 1.0

diff_un = np.zeros(10000)
diff_gauss = np.zeros(10000)
x_gauss = np.zeros(10000)
x_uni = np.zeros(10000)
dist_un = np.zeros(10000)
dist_gauss = np.zeros(10000)
for i in range(0,10000):
    x = np.zeros(numgals)
    y = np.zeros(numgals)
    isblue = np.zeros(numgals)
    for j in range(0,numgals):
        phi = rand.random()*2*m.pi
        theta = rand.random()*m.pi
        r = rand.gauss(0,0.5*maxr)
        x[j] = r*m.cos(phi)*m.sin(theta)
        y[j] = r*m.sin(phi)*m.sin(theta)
        if j == 0: x_gauss[i] = x[j]
        color = rand.random()
        if color > 0.5: isblue[j] = 1
        if j == 0:
        #print np.sort(x),np.sort(y)
            dist_gauss[i] = m.sqrt(x[j]**2+y[j]**2)
    x_avg_b = np.sum(isblue*x)/np.sum(isblue)
    y_avg_b = np.sum(isblue*y)/np.sum(isblue)
    x_avg_r = np.sum((1-isblue)*x)/(numgals-np.sum(isblue))
    y_avg_r = np.sum((1-isblue)*y)/(numgals-np.sum(isblue))
    diff_gauss[i] = m.sqrt((x_avg_b-x_avg_r)**2+(y_avg_b-y_avg_r)**2)
for i in range(0,10000):
    x = np.zeros(numgals)
    y = np.zeros(numgals)
    isblue = np.zeros(numgals)
    for j in range(0,numgals):
        phi = rand.random()*2*m.pi
        theta = rand.random()*m.pi
        r = rand.random()*maxr
        x[j] = r*m.cos(phi)*m.sin(theta)
        y[j] = r*m.sin(phi)*m.sin(theta)
        if j == 0: x_uni[i] = x[j]
        color = rand.random()
        if color > 0.5: isblue[j] = 1
        if j == 0:
        #print np.sort(x),np.sort(y)
            dist_un[i] = m.sqrt(x[j]**2+y[j]**2)
    x_avg_b = np.sum(isblue*x)/np.sum(isblue)
    y_avg_b = np.sum(isblue*y)/np.sum(isblue)
    x_avg_r = np.sum((1-isblue)*x)/(numgals-np.sum(isblue))
    y_avg_r = np.sum((1-isblue)*y)/(numgals-np.sum(isblue))
    diff_un[i] = m.sqrt((x_avg_b-x_avg_r)**2+(y_avg_b-y_avg_r)**2)
sort_diff_gauss = np.sort(diff_gauss)*Mpctoam*60
sort_diff_un = np.sort(diff_un)*Mpctoam*60
print 'Gauss r: %f, %f, %f\n Uni. r: %f, %f, %f\n'%(sort_diff_gauss[4999],sort_diff_gauss[6666],sort_diff_gauss[9999],sort_diff_un[4999],sort_diff_un[6666],sort_diff_un[9999])
pylab.hist(x_gauss,bins=40,range=(-2,2),color='red')
pylab.hist(x_uni,bins=20,range=(-1,1),histtype='step',color='blue')
pylab.savefig('/home/rumbaugh/histtest_x.png')
pylab.close('all')
pylab.hist(sort_diff_gauss,bins=40,range=(0,100),color='red')
pylab.hist(sort_diff_un,bins=40,range=(0,100),histtype='step',color='blue')
pylab.savefig('/home/rumbaugh/diffhist_x.png')
pylab.close('all')
pylab.hist(dist_gauss*Mpctoam*60,bins=40,range=(0,200),color='red')
pylab.hist(dist_un*Mpctoam*60,bins=40,range=(0,200),histtype='step',color='blue')
pylab.savefig('/home/rumbaugh/disthist_test.png')
pylab.close('all')
