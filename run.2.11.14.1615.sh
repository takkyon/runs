obs ../data/af377_10.25.00.1030+074.uvfits
select I
mapunits arcsec
mapsize 1024,0.05
rmod ../models/prelim_fit.1030+074.5.28.01.mod
modelfit 5
selfcal false,false,60
modelfit 5
selfcal false,false,60
modelfit 10
gscale
modelfit 5
selfcal false,false,20
modelfit 5
cmul = imstat(rms)
print cmul
mapsize 256,0.05
shift -0.878,1.143
levs = 2,4,8,16,32,64,128
mapl cln

!0414
!shift 0.472,1.277
!0712
!shift -0.793,-0.156
!1030
!shift -0.878,1.143
!1127
!shift -0.276,0.048
!1152
!shift -0.549,0.978
