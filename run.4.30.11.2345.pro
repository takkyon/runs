set_dirs
set_plot,'PS'
loadct,13

device,file="/home/rumbaugh/paperstuff/Cl1604.rsoffsets.full.4.30.11.ps",/color

bndX = [-2*0.0907,-2*0.0907,2*0.0907,2*0.0907]
bndY = [0,1000,1000,0]


readcol,"/home/rumbaugh/LFC/FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat",newid,mask,slit,raLFC,decLFC,rprime,iprime,zprime,rs,rserr,Q,oldid,pflags,raACS,decACS,idACS,f606,f814,format="A,A,A,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D"
g = where((0.96 ge rs) and (rs ge 0.84))
rsfit = 3.182-0.063*f814
rsoffset = f606-f814-rsfit
rsoNorm = rsoffset/(4.0*0.0907)
plot,[0-1],[0-1],XRANGE=[-2,0.5],YRANGE=[0,42],xstyle=1,ystyle=1,XTITLE='RS Offset (F606W-F814W)',YTITLE='Num. of galaxies',CHARSIZE=1.1,CHARTHICK=1.5,XTHICK=1.5,YTHICK=1.5
histoplot,rsoffset[g],BINSIZE=0.05,MINVALUE=-1.85,MAXVALUE=0.5,THICK=2,/oplot
oplot,bndX,bndY,linestyle=1,THICK=3


end
