import numpy as np
import pyfits as py
import copy
import os
os.chdir('/home/rumbaugh/KAST/Science')
crls = np.loadtxt('/home/rumbaugh/KAST/Science/sci_fits_list.txt',dtype='string')

for i in range(0,len(crls)):
    if len(crls[i]) == 13:
        color=crls[i][4]
        num = crls[i][5:8]
        infile='sci-%s%s.skysub.fits'%(color,num)
        outfile='transpose_sci-%s%s.skysub.fits'%(color,num)
        cr=py.open(infile)
        data=cr[0].data.copy()
        dataT=np.transpose(data)
        hdr=py.getheader(infile)
        temphdr=copy.deepcopy(hdr)
        if ((color=='b')&(num=='198')):py.PrimaryHDU(dataT,temphdr).writeto(outfile)
