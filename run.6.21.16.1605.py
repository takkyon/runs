import numpy as np
execfile('/home/rumbaugh/calc_Xray_lums.py')


nh_dict={"rxj1757": 4.08,"cl1604": 1.22,"cl0023": 2.79,"cl1324_north": 1.15,"cl1324_south": 1.16, 'cl1324': 1.155,"rxj1821":5.67, 'rcs0224': 2.86, 'cl0849': 2.73, 'rxj0910': 1.98,'rxj1053': 0.58, 'rxj1221':1.44,'cl1350':1.76,'rxj1716':3.71,'cl1137':1.93}

infile='/home/rumbaugh/combined_match_catalog.6.21.16.dat'

indict={'names':('field','number','RA','Dec','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','ID','mask','slit','bcnts_soft','bcnts_hard','bcnts_full','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','|S32','f8','f8','f8','f8','f8','f8')}

cr=np.loadtxt(infile,dtype=indict)

#oldfile='/home/rumbaugh/X-ray_lum_cat.1.13.16.dat'
#olddict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32')}
#cro=np.loadtxt(oldfile,olddict)
gf=np.zeros(0,dtype='i8')
for i in range(0,np.shape(cr)[0]):
    if cr['field'][i] in nh_dict.keys():
        gf=np.append(gf,i)

nh_arr=np.zeros(len(cr['redshift']))
for field in nh_dict.keys():
    nh_arr[cr['field']==field]=nh_dict[field]

fluxes=np.zeros((len(nh_arr),3))
fluxes[:,0],fluxes[:,1],fluxes[:,2]=cr['flux_soft'],cr['flux_hard'],cr['flux_full']

calc_dict={'z': cr['redshift'], 'nh': nh_arr, 'bands':{ 'names': np.array(['soft','hard','full']), 'kev': np.array([[0.5,2.0],[2.0,7.0],[0.5,7.0]])}, 'flux':fluxes}

infile='/home/rumbaugh/X-ray_lum_cat.4.17.16.dat'

indict={'names':('field','number','RA','Dec','lum_soft','lum_hard','lum_full','flux_soft','flux_hard','flux_full','ncnts_soft','ncnts_hard','ncnts_full','redshift','mask','slit','sigS','sigH','sigF'),'formats':('|S32','i8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8','|S32','|S32','f8','f8','f8')}

crx=np.loadtxt(infile,dtype=indict)

FILE=open('/home/rumbaugh/X-ray_lum_cat.6.21.16.dat','w')
FILE.write('# field number RA Dec lum_soft lum_hard lum_full flux_soft flux_hard flux_full ncnts_soft ncnts_hard ncnts_full redshift mask slit sig_soft sig_hard sig_full\n')
for i in range(0,len(nh_arr)): 
    FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %7.5f %s %s %f %f %f\n'%(crx['field'][i],crx['number'][i],crx['RA'][i],crx['Dec'][i],crx['lum_soft'][i],crx['lum_hard'][i],crx['lum_full'][i],crx['flux_soft'][i],crx['flux_hard'][i],crx['flux_full'][i],crx['ncnts_soft'][i],crx['ncnts_hard'][i],crx['ncnts_full'][i],crl['redshift'][i],crx['mask'][i],crx['slit'][i],crx['sigS'][i],crx['sigH'][i],crx['sigF'][i]))#,crx['ncnts_soft'][i]/(1.+np.sqrt(0.75+crx['bcnts_soft'][i])),crx['ncnts_hard'][i]/(1.+np.sqrt(0.75+crx['bcnts_hard'][i])),crx['ncnts_full'][i]/(1.+np.sqrt(0.75+crx['bcnts_full'][i]))))
    #FILE.write('%10s %2i %7.5f %7.5f %E %E %E %E %E %E %6.1f %6.1f %6.1f %5.3f %s %s %6.1f %6.1f %6.1f \n'%(crx['field'][gf][i],crx['number'][gf][i],crx['RA'][gf][i],crx['Dec'][gf][i],cro['lum_soft'][i],cro['lum_hard'][i],cro['lum_full'][i],crx['flux_soft'][gf][i],crx['flux_hard'][gf][i],crx['flux_full'][gf][i],crx['ncnts_soft'][gf][i],crx['ncnts_hard'][gf][i],crx['ncnts_full'][gf][i],crx['redshift'][gf][i],crx['mask'][gf][i],crx['slit'][gf][i],crx['ncnts_soft'][gf][i]/(1.+np.sqrt(0.75+crx['bcnts_soft'][gf][i])),crx['ncnts_hard'][gf][i]/(1.+np.sqrt(0.75+crx['bcnts_hard'][gf][i])),crx['ncnts_full'][gf][i]/(1.+np.sqrt(0.75+crx['bcnts_full'][gf][i]))))
FILE.close()
