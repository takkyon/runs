execfile("/home/rumbaugh/StructureFunction.py")
execfile("/home/rumbaugh/LoadVLA_2001.py")
execfile("/home/rumbaugh/LoadEVLA_2011.py")
execfile("/home/rumbaugh/LinReg.py")

import matplotlib.pyplot as plt

date = '6.10.14'

def calcXr(X,Xerr):
    Xerr *= 0.6
    Xr = np.sum((X/Xerr)**2)/len(X)
    return Xr



for lens in ['0414','0712','1030','1127','1152']:
    ltime,flux_arr,flux_err_arr = LoadVLA_2001(lens)
    Aflux,Bflux = flux_arr[0],flux_arr[1]
    Aerr,Berr = flux_err_arr[0],flux_err_arr[1]
    if lens in ['0414','B0712']:
        A1flux,Bflux = flux_arr[1],flux_arr[2]
        A1err,Berr = flux_err_arr[1],flux_err_arr[2]
        Aflux,Aerr = Aflux+A1flux,np.sqrt(Aerr**2+A1err**2)
    ltime = (ltime-ltime[0])#/86400
    g = np.arange(len(ltime))[:len(ltime)-10]
    Aerr /= np.mean(Aflux[g])
    Aflux /= np.mean(Aflux[g])
    Berr /= np.mean(Bflux[g])
    Bflux /= np.mean(Bflux[g])
    X,Y = (Aflux[g]-Bflux[g])/np.sqrt(2),(Aflux[g]+Bflux[g])/np.sqrt(2)
    Xerr = np.sqrt((Aerr[g]**2+Berr[g]*2)/2)
    Xr = calcXr(X,Xerr)
    print '%s - %f'%(lens,Xr)
lens = '1938'
crS = LoadEVLA_2011(source='B1938',normalize=True)
C1flux,C2flux,Bflux = crS['fluxC1'],crS['fluxC2'],crS['fluxB']
C1err,C2err,Berr = crS['errC1'],crS['errC2'],crS['errB']
Cflux,Cerr = C1flux+C2flux,np.sqrt(C1err**2+C2err**2)
g = np.where((C1flux > 0) & (C2flux > 0) & (Bflux>0))[0]
Cerr /= np.mean(Cflux[g])
Cflux /= np.mean(Cflux[g])
Berr /= np.mean(Bflux[g])
Bflux /= np.mean(Bflux[g])
X,Y = (Cflux[g]-Bflux[g])/np.sqrt(2),(Cflux[g]+Bflux[g])/np.sqrt(2)
Xerr = np.sqrt((Cerr[g]**2+Berr[g]*2)/2)
Xr = calcXr(X,Xerr)
print '%s - %f'%(lens,Xr)
