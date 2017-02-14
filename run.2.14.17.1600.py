import numpy as np
import shapely.geometry as geometry
import easyaccess as ea

con=ea.connect()

q2='SELECT f.RA_CENT,f.DEC_CENT,f.RAC1,f.RAC2,f.RAC3,f.RAC4,f.DECC1,f.DECC2,f.DECC3,f.DECC4,f.ID,d.TILENAME FROM RUMBAUGH.Y3A1_TILENAMES_LIST d,DES_ADMIN.Y3A1_COADDTILE_GEOM f WHERE d.tilename=f.tilename'

TDF=con.query_to_pandas(q2)

boxes={TDF['TILENAME'][i]: geometry.MultiPoint(list(np.array([[TDF['RAC1'][i],TDF['DECC1'][i]],[TDF['RAC2'][i],TDF['DECC2'][i]],[TDF['RAC3'][i],TDF['DECC3'][i]],[TDF['RAC4'][i],TDF['DECC4'][i]]]))).convex_hull for i in np.arange(0,np.shape(TDF)[0])}

TDFtilenames,TDFrac,TDFdecc=np.array(TDF['TILENAME']),np.array(TDF['RA_CENT']),np.array(TDF['DEC_CENT'])

qm='SELECT * from RUMBAUGH.DR7_BH_HPIX'
MDF=con.query_to_pandas(qm)

outcr=np.zeros((np.shape(MDF)[0],np.shape(MDF)[1]),dtype='|S20')
outcr[:,0],outcr[:,1],outcr[:,2]=np.array(MDF['SDSS_NAME']),np.array(MDF['RA']),np.array(MDF['DEC'])

for i in range(0,np.shape(MDF)[0]):
    curmra,curmdec=MDF['RA'][i],MDF['DEC'][i]
    gclose=np.where(np.sqrt((TDFrac-curmra)**2+(TDFdecc-curmdec)**2)<1.5)[0]
    gs=np.argsort(np.sqrt((TDFrac[gclose]-curmra)**2+(TDFdecc[gclose]-curmdec)**2))
    foundbox,cnt=False,-1
    while ((not(foundbox))&(cnt<len(gs)-1)):
        cnt+=1
        foundbox=boxes[TDFtilenames[gclose][gs][cnt]].contains(geometry.Point(curmra,curmdec))
    #if not(foundbox): 
    #    print 'Found no box for',MDF['MQ_ROWNUM'][i],curmra,curmdec
    if foundbox:
        outcr[:,3][i]=TDFtilenames[gclose][gs][cnt]
    else:
        outcr[:,3][i]='None'

np.savetxt('/home/rumbaugh/DR7_BH_Y3A1_tilenames.csv',outcr,fmt='%s,%s,%s,%s',header='SDSS_NAME,RA,DEC,TILENAME',comments='')
