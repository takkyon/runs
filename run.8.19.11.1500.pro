
set_dirs
usersymfs
c2f = [[5.66306511542e-11,1.66681616965e-11,1.67083124157e-11,1.71226366747e-11,1.71288816213e-11,3.58103893313e-10,1.37889668047e-10],[2.15619390269e-11,1.76555669098e-11,1.76481547625e-11,1.83530000159e-11,1.83487592541e-11,2.86905834614e-11,2.58843094352e-11]]
nh = [2.79,1.22,1.155,5.66,4.07]
ids = ['Cl0023','Cl1604','Cl1324','NEP5281','RXJ1757']
mas = ['7914','master','master','master','master']
f2l = [1.676e+57,1.987e+57,1.310e+57,1.580e+57,1.034e+57]
zhb = [0.855,0.96,0.785,0.828,0.705]
zlb = [0.820,0.84,0.6550,0.808,0.68]

pcnames = ['cl0023','cl1604','cl1324','nep5281','nep200']

mfilenames = ["/home/rumbaugh/LFC/FINAL.matched.0023.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.1322.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N5281.specnXray.nov2010.rumbaugh.cat","/home/rumbaugh/LFC/FINAL.matched.N200.specnXray.nov2010.rumbaugh.cat"]
sfiles = ['FINAL.onlykindafinal.cl0023.deimos.lris.oct2010.cat','FINAL.spectra.sc1604.onlysemifinal.wcompletenessmasks.feb2011.cat','FINAL.cl1322.lrisplusdeimos.cat','FINAL.nep5281.deimos.gioia.feb2010.cat','FINAL.spectroscopic.autocompile.N200.blemaux.nov2010.wh.cat']
set_plot,'PS'
;loadct,'13'
device,file="/home/rumbaugh/LumvsRSplot.8.19.11.ps",/color
totalslum = []
totalhlum = []
kslum = []
khlum = []
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
rsfit = []
rsfitk = []
rsfity = []
rsfito = []
sigy = []
sigo = []
colerrsy = []
colerrso = []


rsfitb = [1.777,3.182,1.325,1.203,1.84]
rsfitm = [0.0229,0.063,0.0084,0.0012,0.0319]
rsSTD = [0.0625,0.0907,0.0735,0.0413,0.0576]
rsnstd = [3.,2.,2.,3.,3.]
mx = (43.2104078-43.348505)/(240.9472-241.28263)

for i=0,4 do begin &$
   if i eq 1 then readcol,'/home/rumbaugh/LFC/ACS_merged.F606W+F814W_deep.all.coll.dat',acsRA,acsDec,acs606,acs814,dmag606,dmag814,rh606,rh814,format='D,D,D,D,D,D,D,D',/SILENT &$
   rpfile = '/home/rumbaugh/LFC/' + pcnames[i] + '.photcat'
   readcol,rpfile,rpID,rpx,rpy,rpra,rpdec,rpr,rerr,rpi,ierr,rpz,zerr,format='A,D,D,D,D,D,D,D,D,D',/silent
   mfile = '/home/rumbaugh/temp/matched.' + ids[i] + '.Xray_opt_spec.bothmatches_serendips.8.9.11.cat' &$
   if i eq 1 then mfile = '/home/rumbaugh/temp/matched.' + ids[i] + '.Xray_opt_spec.bothmatches_serendips.8.15.11.cat' &$
   if i eq 1 then readcol,mfile,Xray_ID,Xray_RA,Xray_Dec,poserr,ncnts_soft,ncnts_hard,ncnts_full,flux_soft,flux_hard,flux_full,sig_soft,sig_hard,sig_full,num_opt_matches,opt_ID,mask,slit,opt_RA,opt_Dec,q,z,z_err,rB,iB,zB,f606,f814,format='I,D,D,D,D,D,D,D,D,D,D,D,D,I,A,A,A,D,D,I,D,D,D,D,D,D,D,D',/silent &$
   if i ne 1 then readcol,mfile,Xray_ID,Xray_RA,Xray_Dec,poserr,ncnts_soft,ncnts_hard,ncnts_full,flux_soft,flux_hard,flux_full,sig_soft,sig_hard,sig_full,num_opt_matches,opt_ID,mask,slit,opt_RA,opt_Dec,q,z,z_err,rB,iB,zB,format='I,D,D,D,D,D,D,D,D,D,D,D,D,I,A,A,A,D,D,I,D,D,D,D,D,D',/silent &$
   if i eq 1 then rB = f606 &$
   if i eq 1 then iB = f814 &$
   sigmax = DBLARR(n_elements(q)) &$
   for j=0,n_elements(sigmax)-1 do begin &$
   sigmax[j] = sig_soft[j] &$
   if sig_hard[j] gt sigmax[j] then sigmax[j] = sig_hard[j] &$
   if sig_full[j] gt sigmax[j] then sigmax[j] = sig_full[j] &$
   endfor &$
   ;readcol,mfilenames[i],LFCid,mask,slit,raopt,decopt,rB,iB,zB,z,zerr,q,oldid,format='A,A,I,D,D,D,D,D,D,D,I,A' &$
    sfile = '/home/rumbaugh/' + sfiles[i] &$
    if i ne 1 then readcol,sfile,sLFCID,mask,slit,spra,spdec,spr,spi,spz,sredshift,srerr,q,old_id,format='A,A,A,D,D,D,D,D,D,D,D,A,A',/silent &$
    if i eq 1 then readcol,sfile, sLFCID,mask,slit,spra,spdec,spr,spi,spz,sredshift,srerr,q,old_id,maskACS,sacsRA,sacsDec,acsID,s606,s814,format='A,A,A,D,D,D,D,D,D,D,D,A,A,D,D,A,D,D',/silent &$
    if i eq 1 then spr = s606 &$
    if i eq 1 then spi = s814 &$
   if i eq 1 then readcol,"/home/rumbaugh/LFC/FINAL.matched.1604.specnXray.nov2010.rumbaugh.cat",LFCid,mask,slit,raopt,decopt,qqrB,qqiB,zB,mz,mzerr,mq,oldid,mskACA,raACA,decACA,idACA,m606,m814,idX,raX,decX,errX,Rel,Sig,format='A,A,I,D,D,D,D,D,D,D,I,A,A,D,D,A,D,D,I,D,D,D,D,D' &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.soft.8.10.11.dat' &$
   readcol,fileroot,slum,sflux,sncnts,sz,sra,sdec &$
   fileroot = '/home/rumbaugh/LFC/XrayLums.' + ids[i] + '.hard.8.10.11.dat' &$
   readcol,fileroot,hlum,hflux,hncnts,hz,hra,hdec,q &$
   iinds = make_array(n_elements(sz)) &$
   for ii=0,n_elements(sz)-1 do iinds[ii] = where((sz[ii] lt z+0.00001) and (sz[ii] gt z-0.00001)) &$
   rbtemp = rB[iinds] &$
   ibtemp = iB[iinds] &$
   sigtemp = sigmax[iinds] &$
   ;ors = where((rbtemp-ibtemp7 gt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i]) and (rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp+(rsnstd[i]+0.1)*rsSTD[i])) &$
   ;nors = where((rbtemp-ibtemp lt rsfitb[i]-rsfitm[i]*ibtemp-rsnstd[i]*rsSTD[i])) &
   rsfitt = -1*(rsfitb[i]-rsfitm[i]*ibtemp-(rbtemp-ibtemp))/(rsnstd[i]*rsSTD[i]) &$
   colerrs = DBLARR(n_elements(rbtemp))
   for ri=0,n_elements(rbtemp)-1 do begin &$
  ; if i eq 1 then print,Xray_ID[iinds[ri]] &$
  ; if ((i eq 1) and (Xray_ID[iinds[ri]] eq 9)) then print,'bagel' &$
   if ((i eq 1) and (Xray_ID[iinds[ri]] eq 9)) then rbtemp[ri] = m606[1] &$
   if ((i eq 1) and (Xray_ID[iinds[ri]] eq 9)) then ibtemp[ri] = m814[1] &$
   gri = where(rpID eq opt_ID[iinds[ri]]) &$
   if i eq 1 then gri = where((acsRA gt opt_RA[iinds[ri]]-0.00001) and (acsRA lt opt_RA[iinds[ri]]+0.00001) and (acsDec gt opt_Dec[iinds[ri]]-0.00001) and (acsDec lt opt_Dec[iinds[ri]]+0.00001)) &$
   if ((i eq 2) or (i eq 4)) then gri = where((rpra gt opt_RA[iinds[ri]]-0.00001) and (rpra lt opt_RA[iinds[ri]]+0.00001) and (rpdec gt opt_Dec[iinds[ri]]-0.00001) and (rpdec lt opt_Dec[iinds[ri]]+0.00001)) &$
   if ((i ne -1) and (gri[0] lt -0.1)) then print, "No match to Roy's catalog - " + string(ri) + "," + string(opt_ID[iinds[ri]]) &$
   if ((i ne 1) and (gri[0] gt -0.1)) then colerrs[ri] = sqrt(rerr[gri[0]]*rerr[gri[0]] + ierr[gri[0]]*ierr[gri[0]]*(1+rsfitm[i]*rsfitm[i]))/(rsnstd[i]*rsSTD[i]) &$
   if ((i eq 1) and (gri[0] gt -0.1)) then colerrs[ri] = sqrt(dmag606[gri[0]]*dmag606[gri[0]] + dmag814[gri[0]]*dmag814[gri[0]]*(1+rsfitm[i]*rsfitm[i]))/(rsnstd[i]*rsSTD[i]) &$
      endfor &$
   rsfitt = -1*(rsfitb[i]-rsfitm[i]*ibtemp-(rbtemp-ibtemp))/(rsnstd[i]*rsSTD[i]) &$
   ;gic = where((sz[iinds] ge zlb[i]) and (sz[iinds] le zhb[i])) &$
   ;gic = where((sz[ors] ge zlb[i]) and (sz[ors] le zhb[i])) &$
                                ;gic2 = where((sz[nors] ge zlb[i]) and (sz[nors] le zhb[i])) &$
                                ;print,rbtemp[ors[gic]],rbtemp[nors[gic2]],ibtemp[ors[gic]],ibtemp[nors[gic2]],rsfitt[ors[gic]],rsfitt[nors[gic2]]
   if i eq 0 then pairsIDs = ['11300','9152']
   if i eq 1 then pairsIDs = ['LFC_SC1_00483','LFC_SC1_0086','LFC_SC2_09481','LFC_SC1_01029','LFC_SC1_03416']
   pair2 = 'COS_SC1_02403'
   if i eq 2 then pairsIDs = ['F00731']
   if i eq 3 then pairsIDs = ['4933']
   pairsI = DBLARR(n_elements(pairsIDs))
   for pi=0,n_elements(pairsIDs)-1 do begin &$
      grpi = where(sLFCID eq pairsIDs[pi]) &$
      pairsI[pi] = spi[grpi[0]] &$
      endfor &$
   Iflux = 10^(pairsI/(-2.5)) &$
   if i eq 1 then gpair2 = where(sLFCID eq pair2) &$
   rsfit = [rsfit,rsfitt] &$
   if i lt 1.5 then rsfity = [rsfity,rsfitt] &$
   if i gt 1.5 then rsfito = [rsfito,rsfitt] &$
   flum = slum+hlum &$
   slum += 0.0000000001 &$
   hlum += 0.0000000001 &$
   slum = alog10(slum)+42 &$
   hlum = alog10(hlum)+42 &$
   gs = sort(sz) &$
   ;print,sz[gs]
   if i eq 0 then gks = [2,5] &$
   if i eq 1 then gks = [0,1,2,5,9] &$
   if i eq 2 then gks = [0] &$
   if i eq 3 then gks = [1] &$
   ;print,sz[gs[gks]]
   if i lt 3.4 then kslum = [kslum,slum[gs[gks]]] &$
   if i lt 3.4 then khlum = [khlum,hlum[gs[gks]]] &$
   if i lt 3.4 then rsfitk = [rsfitk,rsfitt[gs[gks]]] &$
   if i lt 3.4 then print,ibtemp[gs[gks]]/pairsI
   if i lt 3.4 then print,10^(ibtemp[gs[gks]]/(-2.5))/Iflux
   if i eq 1 then print,ibtemp[gs[2]]/spi[gpair2[0]]
   if i eq 1 then print,10^(ibtemp[gs[2]]/(-2.5))/10^(spi[gpair2[0]]/(-2.5))
   totalslum = [totalslum,slum] &$
   totalhlum = [totalhlum,hlum] &$
   ;for jjj=0,n_elements(sz)-1 do print,sz[jjj],rsfitt[jjj] &$
   ;nrsslum = [nrsslum,slum[nors[gic2]]] &$
   ;nrshlum = [nrshlum,hlum[nors[gic2]]] &$
   ;rsslum = [rsslum,slum[ors[gic]]] &$
   ;rshlum = [rshlum,hlum[ors[gic]]] &$
   if i lt 1.5 then yslum = [yslum,slum] &$
   if i lt 1.5 then yhlum = [yhlum,hlum] &$
   if i gt 1.5 then oslum = [oslum,slum] &$
   if i gt 1.5 then ohlum = [ohlum,hlum] &$
   if i lt 1.5 then sigy = [sigy,sigtemp] &$
   if i gt 1.5 then sigo = [sigo,sigtemp] &$
   if i lt 1.5 then colerrsy = [colerrsy,colerrs] &$
   if i gt 1.5 then colerrso = [colerrso,colerrs] &$
   ;Histoplot,slum,TITLE=ids[i]+" - Soft Band" &$
   ;Histoplot,hlum,TITLE=ids[i]+" - Hard Band" &$
   ;Histoplot,flum,TITLE=ids[i]+" - Full Band" &$
   ;print,n_elements(yslum),n_elements(oslum)
   ;print,ors,gic,nors,gic2
endfor

totalflum = alog10(10^(totalslum-42)+10^(totalhlum-42))+42
yflum=alog10(10^(yslum-42)+10^(yhlum-42))+42
oflum=alog10(10^(oslum-42)+10^(ohlum-42))+42
kflum=alog10(10^(kslum-42)+10^(khlum-42))+42
;rsflum=alog10(10^(rsslum-42)+10^(rshlum-42))+42
;nrsflum=alog10(10^(nrsslum-42)+10^(nrshlum-42))+42
;plot,totalslum
;Histoplot,totalslum,TITLE="Total Soft Band"
;Histoplot,totalhlum,TITLE="Total Hard Band"
;Histoplot,totalflum,TITLE="Total Full Band"


;!p.position = square()
;plot,[0,1],[0,1],/nodata,XTITLE='Log Luminosity',YTITLE='Num. of AGN',XRANGE=[41.5,44.5],YRANGE=[0,5.2],XSTYLE=1,YSTYLE=1,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
;Histoplot,yslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",THICK=4
;Histoplot,oslum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Soft Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,yhlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",THICK=4
;Histoplot,ohlum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Hard Band",/LINE_FILL,POLYCOLOR='Royal Blue',ORIENTATION=45,/oplot
;legend,['Cl1604,Cl0023','Cl1324,NEP5281,NEP200'],color=['255','70']
;Histoplot,nrsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",/LINE_FILL,datacolorname='Navy Blue',POLYCOLOR='Navy Blue',ORIENTATION=45,spacing=0.25,THICK=2,/oplot
;Histoplot,rsflum,BINSIZE=0.25,MININPUT=41,MAXINPUT=45,TITLE="Comparison - Full Band",THICK=10,datacolorname='Red',/oplot
;7legend,['On RS','Not on RS'],color=['255','50'],PSYM=[6,8],SYMSIZE=[1.5,1.5],CHARTHICK=4,CHARSIZE=1,THICK=[10,2],/right
plot,[0-1],[0-1],/nodata,XTITLE=['RS Offset (RS Widths)'],YTITLE=['Log Rest-frame 0.5-8.0 keV Luminosity'],XRANGE=[-7.5,2],YRANGE=[41.75,44.5],/xsty,/ysty,XTHICK=4,YTHICK=4,CHARSIZE=1.3,CHARTHICK=4
xyouts,[-5.4,-2.7,-2.7,0.5,0.5,-5.4],[43.7,43.7,41.85,41.85,43.7,41.85],['1','2','3','4','6','5'],CHARSIZE=2,CHARTHICK=7
yt = [44.18,30,30,43.3,43.3,30,30,50,50,44.32]
xt = [-3,-3,10,10,-200,-200,-1,-1,-3,-3]
oplot,xt,yt,linestyle=1,THICK=2
;oplot,rsfitk,kflum,PSYM=7,SYMSIZE=2,THICK=4
;oploterror,rsfity,yflum,colerrsy,DBLARR(n_elements(rsfity)),PSYM=4,color='Purple',THICK=4,SYMSIZE=2.5
;oploterror,rsfito,oflum,colerrso,DBLARR(n_elements(rsfity)),PSYM=6,color='Forest Green',THICK=4,SYMSIZE=2.5
oplot,rsfity,yflum,PSYM=4,color=20,THICK=4,SYMSIZE=2.5
oplot,rsfito,oflum,PSYM=6,color='18',THICK=4,SYMSIZE=2.5
legend,['Cl1324,RXJ1821,RXJ1757','Cl1604,Cl0023'],color=['18','20'],PSYM=[6,4],SYMSIZE=[1.5,1.5],CHARTHICK=4,CHARSIZE=1.3,THICK=[4,4],box=0,/top,/left
gtemp = where((yflum gt 43.2) and (rsfity gt -6) and (rsfity lt -3))
;print,"Lum > 43.2, -6>C>-3, young: ",n_elements(gtemp)
gtemp = where((oflum gt 43.2) and (rsfito gt -6) and (rsfito lt -3))
;print,"Lum > 43.2, -6>C>-3, old: ",n_elements(gtemp)
gtemp = where((yflum gt 43.2) and (rsfity gt -3) and (rsfity lt -1))
;print,"Lum > 43.2, -3>C>-1, young: ",n_elements(gtemp)
gtemp = where((oflum gt 43.2) and (rsfito gt -3) and (rsfito lt -1))
;print,"Lum > 43.2, -3>C>-1, old: ",n_elements(gtemp)
gtemp = where((yflum gt 43.2) and (rsfity gt -1) and (rsfity lt 2))
;print,"Lum > 43.2, -1>C>+2, young: ",n_elements(gtemp)
gtemp = where((oflum gt 43.2) and (rsfito gt -1) and (rsfito lt 2))
;print,"Lum > 43.2, -1>C>+2, old: ",n_elements(gtemp)
gtemp = where((yflum lt 43.2) and (rsfity gt -6) and (rsfity lt -3))
;print,"Lum > 43.2, -6>C>-3, young: ",n_elements(gtemp)
gtemp = where((oflum lt 43.2) and (rsfito gt -6) and (rsfito lt -3))
;print,"Lum > 43.2, -6>C>-3, old: ",n_elements(gtemp)
gtemp = where((yflum lt 43.2) and (rsfity gt -3) and (rsfity lt -1))
;print,"Lum > 43.2, -3>C>-1, young: ",n_elements(gtemp)
gtemp = where((oflum lt 43.2) and (rsfito gt -3) and (rsfito lt -1))
;print,"Lum > 43.2, -3>C>-1, old: ",n_elements(gtemp)
gtemp = where((yflum lt 43.2) and (rsfity gt -1) and (rsfity lt 2))
;print,"Lum > 43.2, -1>C>+2, young: ",n_elements(gtemp)
gtemp = where((oflum lt 43.2) and (rsfito gt -1) and (rsfito lt 2))
;print,"Lum > 43.2, -1>C>+2, old: ",n_elements(gtemp)
;for qi=0,n_elements(yflum)-1 do print,10^(yflum[qi]-42),rsfity[qi]
;for ri=0,n_elements(oflum)-1 do print,10^(oflum[ri]-42)XC,rsfito[ri]
;g = where(totalflum lt 43)
;print,rsfit(g)
;Histoplot,rsfit[g],BINSIZE=1,MININPUT=-9,MAXINPUT=4,THICK=2,datacolorname='Navy Blue',/LINE_FILL,POLYCOLOR='Navy Blue',ORIENTATION=45,spacing=0.25
;g = where(totalflum gt 43)
;Histoplot,rsfit[g],BINSIZE=1,MININPUT=-9,MAXINPUT=4,THICK=10,datacolorname='Red',/oplot
;legend,['Log(Lum)>43','Log(Lum)<43'],color=['255','50'],PSYM=[6,8],SYMSIZE=[1.5,1.5],CHARTHICK=4,CHARSIZE=1,THICK=[10,2],/right
;print,rsfit(g)
end
