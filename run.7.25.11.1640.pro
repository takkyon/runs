
set_dirs
usersymfs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+57,1.987e+57,1.310e+57,1.580e+57,1.034e+57]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.6550,0.808,0.68]

mfilenames = ["/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat"]

set_plot,'PS'
loadct,'13'
device,file="/home/rumbaugh/XrayLums_RS.7.25.11.ps",/color
totalslum = []
totalhlum = []
yslum = []
yhlum = []
oslum = []
ohlum = []
yHR = []
oHR = []
ic = []
yIC = []
oIC = []
cl1324rac = 0.5*(30.86373172217+30.279328719557)
c2finds = [0,1,3,5,6]
rsslum = []
rshlum = []
nrsslum = []
nrshlum = []


rsfitb = [1.777,3.182,1.325,1.48,1.84]
rsfitm = [0.0229,0.063,0.0084,0.012,0.0319]
rsSTD = [0.0625,0.0907,0.0735,0.0636,0.0576]
rsnstd = [3.,2.,2.,3.,3.]
mx = (43.2104078-43.348505)/(240.9472-241.28263)

for i=0,4 do begin &$
   readcol,mfilenames[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,format='A,A,I,D,D,D,D,D,D,D,I,A' &$
   if i eq 1 then readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,qqrB,qqiB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,rB,iB,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D' &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.soft.dat' &$
   readcol,fileroot,slum,sflux,sncnts,sz,sra,sdec &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.hard.dat' &$
   readcol,fileroot,hlum,hflux,hncnts,hz,hra,hdec &$
   iinds = make_array(n_elements(sz)) &$
   for ii=0,n_elements(sz)-1 do iinds[ii] = where((sz[ii] lt z+0.00001) and (sz[ii] gt z-0.00001)) &$
   rbtemp = rB[iinds] &$
   ibtemp = iB[iinds] &$
   ors = where((rbtemp-ibtemp gt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i]) and (rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp+rsnstd[i]*rsSTD[i])) &$
   nors = where((rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i])) &$
   rsfitt = (rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i])/(rsnstd[i]*rsSTD[i]) &$
   ictemp = make_array(n_elements(sz),value=0) &$
   gic = where((sz[ors] ge zlb[i]) and (sz[ors] le zhb[i])) &$
   gic2 = where((sz[nors] ge zlb[i]) and (sz[nors] le zhb[i])) &$
   rsfit = [rsfit,rsfitt[nors[gic2]]] &$
   rsfit = [rsfit,rsfitt[ors[gic]]] &$
   ictemp[gic] = 1 &$
   ic = [ic,ictemp] &$
   flum = slum+hlum &$
   slum += 0.0000000001
   hlum += 0.0000000001
   slum = alog10(slum)+42
   hlum = alog10(hlum)+42
   totalslum = [totalslum,slum] &$
   totalhlum = [totalhlum,hlum] &$
   rsslum = [rsslum,slum[ors[gic]]] &$
   rshlum = [rshlum,hlum[ors[gic]]] &$
   nrsslum = [nrsslum,slum[nors[gic2]]] &$
   nrshlum = [nrshlum,hlum[nors[gic2]]] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
endfor

totalflum = alog10(10^(totalslum-42)+10^(totalhlum-42))+42
rsflum=alog10(10^(rsslum-42)+10^(rshlum-42))+42
nrsflum=alog10(10^(nrsslum-42)+10^(nrshlum-42))+42
;plot,totalslum
;Histoplot,totalslum,TITLE="Total Soft Band"
;Histoplot,totalhlum,TITLE="Total Hard Band"
;Histoplot,totalflum,TITLE="Total Full Band"

!p.position = square()
plot,[0,1],[0,1],/nodata,XTITLE='Log Luminosity',YTITLE='Num. of AGN',XRANGE=[41.5,44.5],YRANGE=[0,5.2],XSTYLE=1,YSTYLE=1,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
;Histoplot,yslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",THICK=4
;Histoplot,oslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,yhlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",THICK=4
;Histoplot,ohlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
Histoplot,nrsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",/LINE_FILL,datacolorname='Navy Blue',POLYCOLOR='Navy Blue',ORIENTATION=45,spacing=0.25,THICK=2,/oplot
Histoplot,rsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",THICK=10,datacolorname='Red',/oplot
legend,['On RS','Not on RS'],color=['255','50'],PSYM=[6,8],SYMSIZE=[1.5,1.5],CHARTHICK=4,CHARSIZE=1,THICK=[10,2],/right
end
