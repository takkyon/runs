import numpy as np
import pyfits as py
hdu=py.open('/home/rumbaugh/Downloads/psftable.fits')
df=hdu[3].data
fields=['cl0023','rxj1716']
carr=['magenta','cyan']

for s in [1,2]:
    for field in fields:
        cro=np.loadtxt('/home/rumbaugh/sample%i_%s.image_cut.w_PSF.reg'%(s,field),skiprows=3,dtype='|S256')
        print len(cro)
        crpnc=np.loadtxt('/home/rumbaugh/sample%i_%s.phys_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
        crinc=np.loadtxt('/home/rumbaugh/sample%i_%s.image_nocut.reg'%(s,field),skiprows=3,dtype='|S256')
        FILEp=open('/home/rumbaugh/sample%i_%s.phys_nocut.w_PSF.reg'%(s,field),'w')
        FILEp.write('physical\n')
        FILEi=open('/home/rumbaugh/sample%i_%s.image_nocut.w_PSF.reg'%(s,field),'w')
        FILEi.write('physical\n')
        #FILE=open('/home/rumbaugh/sample%i_%s.image_bkg.w_PSF.reg'%(s,field),'w')
        #FILE.write('physical\n')
        print len(crpnc)
        for i in range(0,len(crpnc)):
            tmpstr=crpnc[i].split(',')
            tmpX,tmpR=tmpstr[0].split('('),tmpstr[0].split(')')
            X,Y=float(tmpX[1]),float(tmpstr[1])
            tmpstri=crinc[i].split(',')
            tmpXi=tmpstri[0].split('(')
            Xi,Yi=float(tmpXi[1]),float(tmpstri[1])
            g=np.where((np.abs(df['X']-X)<100)&(np.abs(df['Y']-Y)<100))[0]
            tmpdist=np.sqrt((df['X'][g]-X)**2+(df['Y'][g]-Y)**2)
            gas=np.argsort(tmpdist)[0]
            #FILE.write('circle(%f,%f,%f) #color=%s\n'%(X,Y,df['PSF90'][g][gas],carr[s-1]))
            FILEp.write('ellipse(%f,%f,%f,%f,%f) #color=%s\n'%(X,Y,df['PSF90'][g][gas][0],df['PSF90'][g][gas][1]/0.492,df['PSF90'][g][gas][2]/0.492,carr[s-1]))
            FILEi.write('ellipse(%f,%f,%f,%f,%f) #color=%s\n'%(Xi,Yi,df['PSF90'][g][gas][0],df['PSF90'][g][gas][1]/0.492,df['PSF90'][g][gas][2]/0.492,carr[s-1]))
        FILEp.close()
        FILEi.close()
