set_dirs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+57,1.987e+57,1.310e+57,1.580e+57,1.034e+57]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.660,0.808,0.68]

pfilenames = ["FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat","FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.nov2010.cat","FINAL.cl1322.lrisplusdeimos.cat","FINAL.nep5281.deimos.gioia.feb2010.cat","FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.cat"]

mfilenames = ["/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat"]

set_plot,'PS'
loadct,'13'
device,file="/home/rumbaugh/XrayLums_RS.5.7.11.ps",/color
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

gvstd = [4.,4.,4.,4.,4.]
 
rsfitb = [1.777,3.182,1.325,1.48,1.84]
rsfitm = [0.0229,0.063,0.0084,0.012,0.0319]
rsSTD = [0.0625,0.0907,0.0735,0.0636,0.0576]
rsnstd = [3.,2.,3.,3.,3.]
mx = (43.2104078-43.348505)/(240.9472-241.28263)

for i=0,4 do begin &$
   pfile = "/home/rumbaugh/LFC/" + pfilenames[i] &$
   readcol,pfile,oID,mask,slit,RA,DEC,rp,ip,zp,rs,rserr,qf,format="A,A,I,D,D,D,D,D,D,D,I",/silent  &$
   if i eq 1 then readcol,pfile,oID,mask,slit,RA,DEC,rp,ip,zp,rs,rserr,qf,oids,pf,aRa,aDec,aID,rp,ip,format="A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D",/silent  &$
   readcol,mfilenames[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,format='A,A,I,D,D,D,D,D,D,D,I,A',/silent &$
   if i eq 1 then readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,qqrB,qqiB,zB,z,zerr,q,oldid,mskACA,raACA,decACA,idACA,rB,iB,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D' &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.soft.dat' &$
   readcol,fileroot,slum,sflux,sncnts,sz,sra,sdec,/silent &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.hard.dat' &$
   readcol,fileroot,hlum,hflux,hncnts,hz,hra,hdec,/silent &$
   iinds = make_array(n_elements(sz)) &$
   for ii=0,n_elements(sz)-1 do iinds[ii] = where((sz[ii] lt z+0.00001) and (sz[ii] gt z-0.00001)) &$
   iinds = where(qf gt 2.3)
   rbtemp = rp[iinds] &$
   ibtemp = ip[iinds] &$
   ;ors = where((rp-ip gt rsfitb[i]-rsfitm[i]*ip-rsnstd[i]*rsSTD[i]) and (rp-ip lt rsfitb[i]-rsfitm[i]*ip+rsnstd[i]*rsSTD[i])) &$
   ;nors = where((rp-ip lt rsfitb[i]-rsfitm[i]*ip-rsnstd[i]*rsSTD[i])) &$
   ors = where((rbtemp-ibtemp gt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i]) and (rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp+rsnstd[i]*rsSTD[i])) &$
   nors = where((rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i])) &$
   igv = where((rbtemp-ibtemp gt rsfitb[i]-rsfitm[i]*ibtemp-(gvstd[i]+rsnstd[i])*rsSTD[i]) and (rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i])) &$
   ictemp = make_array(n_elements(sz),value=0) &$
   gic = where((rs[iinds[ors]] ge zlb[i]) and (rs[iinds[ors]] le zhb[i])) &$
   gic2 = where((rs[iinds[nors]] ge zlb[i]) and (rs[iinds[nors]] le zhb[i])) &$
   gic3 = where((rs[iinds[igv]] ge zlb[i]) and (rs[iinds[igv]] le zhb[i])) &$
   ;ictemp[gic] = 1 &$
   ;ic = [ic,ictemp] &$
   ;flum = slum+hlum &$
   ;slum += 0.0000000001
   ;hlum += 0.0000000001
   ;slum = alog10(slum)+42
   ;hlum = alog10(hlum)+42
   ;totalslum = [totalslum,slum] &$
   ;totalhlum = [totalhlum,hlum] &$
   ;rsslum = [rsslum,slum[ors[gic]]] &$
   ;rshlum = [rshlum,hlum[ors[gic]]] &$
   ;nrsslum = [nrsslum,slum[nors[gic2]]] &$
   ;nrshlum = [nrshlum,hlum[nors[gic2]]] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
   print, ids[i] &$
   print, "Number of sources in cluster: ",n_elements(gic)+n_elements(gic2) &$
   print, "Number of sources on RS:      ",n_elements(gic) &$
   print, "Proportion on red sequence:   ",n_elements(gic)/(1.0*n_elements(gic)+n_elements(gic2)) &$
   print, "Number in green valley:       ",n_elements(gic3)
   print," " &$
endfor

;totalflum = alog10(10^(totalslum-42)+10^(totalhlum-42))+42
;rsflum=alog10(10^(rsslum-42)+10^(rshlum-42))+42
;nrsflum=alog10(10^(nrsslum-42)+10^(nrshlum-42))+42
;plot,totalslum
;Histoplot,totalslum,TITLE="Total Soft Band"
;Histoplot,totalhlum,TITLE="Total Hard Band"
;Histoplot,totalflum,TITLE="Total Full Band"

;!p.position = square()
;plot,[0,1],[0,1],/nodata,XTHICK=2,YTHICK=2,CHARTHICK=2,CHARSIZE=1,XTITLE='Log Luminosity',YTITLE='Num. of AGN',XRANGE=[41.5,44.5],YRANGE=[0,5.2],XSTYLE=1,YSTYLE=1;Histoplot,yslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",THICK=4
;Histoplot,oslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,yhlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",THICK=4
;Histoplot,ohlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,rsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",THICK=4,/oplot
;Histoplot,nrsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['On RS','Not on RS'],color=['255','70'],PSYM=[6,6],SYMSIZE=[0.8,0.8],CHARTHICK=2,CHARSIZE=1,THICK=18,/right
end
