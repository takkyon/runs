#!/bin/csh
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001008
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.08.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001010
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.10.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001015
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.15.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001017
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.17.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001021
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.21.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001022
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.22.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001025
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.25.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001028
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.28.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001031
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.10.31.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001102
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.02.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001104
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.04.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.07.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001109
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.09.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.18.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001120
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.20.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.11.30.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.07.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001210
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.10.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001215
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.15.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.21.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001227
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.27.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20001229
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.12.29.00_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010103
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.03.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010105
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.05.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010107
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.07.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010110
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.10.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010113
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.13.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010115
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.15.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010118
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.18.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010123
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.23.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010127
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.27.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010130
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.1.30.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010201
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.01.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010205
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.05.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010207
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.07.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010208
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.08.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010212
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.12.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010214
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.14.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010216
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.16.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010218
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.18.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010221
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.21.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010222
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.22.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010226
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.2.26.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010301
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.01.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010304
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.04.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010306
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.06.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010310
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.10.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010314
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.14.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010318
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.18.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010321
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.21.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010323
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.23.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010326
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.26.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010328
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.28.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010330
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.30.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010331
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.3.31.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010402
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.02.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010405
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.05.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010409
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.09.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010414
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.14.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010417
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.17.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010419
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.19.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010424
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.24.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010426
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.26.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010430
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.4.30.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010505
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.05.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010508
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.08.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010512
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.12.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010514
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.14.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010517
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.17.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010520
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.20.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010525
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.25.01_wrms.mod
quit
EOF
difmap << EOF
integer mfitniter
mfitniter = 7
logical varpos
varpos = false
obs /mnt/data2/rumbaugh/AIPS/FITS/AF377_0414+573_20010528
select I
mapunits arcsec
mapsize 256,0.05
rmod /mnt/data2/rumbaugh/VLA/AF377/models/20010212_0414_g_varpos.mod
uvrange 0,300
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
selfcal false,false,60
modelfit mfitniter
selfcal false,false, 60
modelfit mfitniter
cmul = imstat(rms)
addcmp cmul,false,0,0
wmod /mnt/data2/rumbaugh/VLA/AF377/difmap_results/fit_aipsredux_UVR_0_300_6.1.14.0414+573.varpos.5.28.01_wrms.mod
quit
EOF
