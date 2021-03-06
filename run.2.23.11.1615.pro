set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/FP.spat.plot.2.23.11.ps',/color

readcol,"/home/rumbaugh/COSMOS/full.spat.anal.2.2.11.dat",ann,SB,format="I,D"
readcol,"/home/rumbaugh/ChandraData/4199/psSB.2.23.11.dat",annps,SBps,format="I,D"

r = ann

cnt = SB*3.141592637
cnt[0] *= r[0]*r[0]
for i=1,n_elements(SB)-1 do cnt[i] *= (r[i]*r[i]-r[i-1]*r[i-1])


SB2 = sqrt(cnt)/3.141592637
SB2[0] /= r[0]*r[0]
for i=1,n_elements(SB)-1 do SB2[i] /= (r[i]*r[i]-r[i-1]*r[i-1])

plot,[0-1],[0-1],/nodata,XTHICK=2,YTHICK=2,CHARTHICK=1.8,XTITLE="Radius(arcseconds)",YTITLE="Surface Brightness(counts arcseconds!E-2)",ystyle=1,xstyle=1,yrange=[0,0.32],xrange=[0,43]

oploterror,r,SB,SB2,PSYM=6,SYMSIZE=1,THICK=2,color=80,errcolor=80

g = where((r ge 50) and (r le 60))
bg = total(SB[g])/n_elements(g)
bgx = [0,10,50,62]
bgy = [1,1,1,1]*bg
oplot,bgx,bgy,linestyle=2,THICK=2


r = annps

cnt = SBps*3.141592637
cnt[0] *= r[0]*r[0]
for i=1,n_elements(SBps)-1 do cnt[i] *= (r[i]*r[i]-r[i-1]*r[i-1])

r = r/2.0

SB2 = sqrt(cnt)/3.141592637
SB2[0] /= r[0]*r[0]
SB[0] = cnt[0]/r[0]*r[0]
for i=1,n_elements(SBps)-1 do SB2[i] /= (r[i]*r[i]-r[i-1]*r[i-1])
for i=1,n_elements(SBps)-1 do SB[i] = cnt[i]/(r[i]*r[i]-r[i-1]*r[i-1])
for i=7,18 do SBps[i] = 0.5*SBps[i] + 0.25*(SBps[i-1]+SBps[i+1])
for i=7,18 do SBps[i] = 0.5*SBps[i] + 0.25*(SBps[i-1]+SBps[i+1])
oplot,r,SBps,THICK=2,LINESTYLE=1,color=160
print,SB[0]

end
