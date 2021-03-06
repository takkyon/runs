import numpy as np
import math as m
import sys
import os
import time
import matplotlib
import matplotlib.pylab as plt
execfile("/home/rumbaugh/arrconv.py")
execfile("/home/rumbaugh/Dispersion.py")

try:
    ALAG
except NameError:
    ALAG = 31.5
try:
    CLAG
except NameError:
    CLAG = 36.5
try:
    DLAG
except NameError:
    DLAG = 80.5
try:
    justone
except NameError:
    justone = False
try:
    timestep
except NameError:
    timestep = 0.5
try:
    mustep
except NameError:
    mustep = 0.001
try:
    maxtimestep
except NameError:
    maxtimestep = 60
try:
    maxmu
except NameError:
    maxmu = 1.1
try:
    minmu
except NameError:
    minmu = 0.9

try:
    lens
except NameError:
    lens = '1030'

execfile("/home/rumbaugh/LoadVLA_2001.py")
ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)

Aflux,Bflux = flux_arr[0],flux_arr[1]
Aerr,Berr = flux_err_arr[0],flux_err_arr[1]

if lens == '0712': 
    Aflux += Bflux
    Aerr = np.sqrt(Aerr**2+Berr**2)
    Bflux,Berr = flux_arr[2],flux_err_arr[2]

st = time.time()
ltime = (ltime-ltime[0])#/86400
#find time delays
BA_disp_mat = np.zeros(1000)
delta = 17.5
g = np.arange(len(ltime))[:len(ltime)-10]
if lens == '1938':
    maxtimestep = 60.
else:
    maxtimestep = 105.
ttmp,mtmp,BA_disp = calc_disp_delay(Aflux[g],Bflux[g],ltime[g],ltime[g],Aerr[g],Berr[g],maxtimestep,timestep,minmu,maxmu,mustep,'D_4_2b',delta,output=2,simplemuerr=True,outfile='/home/rumbaugh/EVLA/light_curves/Dispersions/Disp_grid_out.%s.10.23.13.dat'%lens)
