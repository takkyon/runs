#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.B1938+666.uvfits
select I
mapunits arcsec
mapsize 256,0.03125
shift -1.221864,-0.110719
addcmp 0.0717458,true,-0.664,0.574,varpos
addcmp 0.0307923,true,-0.053,0.869,varpos
addcmp 0.0809120,true,-0.581,0.695,varpos
addcmp 0.0112803,true,0.0,0,varpos
addcmp 0.00985509,true,-0.310,0.973,varpos
addcmp 0.00985509,true,-0.098,0.077,varpos
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
shift 0.1,-0.3
wmap  /mnt/data2/rumbaugh/EVLA/11A-138/data/LateSB1/data/LateSB1_10.7.21.11.11A-138.B1938+666.fits
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/EVLA/11A-138/difmap_results/fit_wrms.B1938+666.LateSB1_10.fixpos.7.21.11.mod
quit
EOF
