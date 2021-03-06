execfile('/home/rumbaugh/optical_matching.py')
#refcat='/home/rumbaugh/git/Chandra/Catalogs/Photometric/rxj1716.radecIDnmags.cat'
refcat='/home/rumbaugh/Chandra/photcats/rxj1716_rizdata.corr.gz'
catin='/home/rumbaugh/Chandra/548/photometry/548.xray_phot.soft_hard_full.dat'
outcat='/home/rumbaugh/Chandra/548/newtest_optmatch.548.dat'
outreg='/home/rumbaugh/Chandra/548/newtest_optmatch.548.reg'
raaim,decaim=259.25281405807,67.195019460966
refdict={'names':('ID','dum1','dum2','ra','dec','magR','dmagR','magI','dmagI','magZ','dmagZ'),'formats':('|S8','f8','f8','f8','f8','f8','f8','f8','f8','f8','f8')}

MatchCat(catin,refcat,outcat,outreg,raaim,decaim,ref_load_dict=refdict)
