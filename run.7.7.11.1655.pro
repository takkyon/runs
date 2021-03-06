set_dirs
set_plot,'PS'
loadct,13
device,file='/home/rumbaugh/paperstuff/RS.hist.1757.7.7.11.ps',/color
path = '/home/rumbaugh/paperstuff'
zlb = [0.65,0.80,0.82,0.84,0.68]
zub = [0.79,0.84,0.87,0.96,0.71]
names = ['Cl1324','NEP5281','Cl0023','Cl1604','RXJ1757']
names2 = ['Cl1324','RXJ1821','Cl0023','Cl1604','RXJ1757']
ymax = [20,14,20,20,20]
thicks=[4,6,5,4,6]
bsize = [0.001,0.001,0.001,0.001,0.002]
i = 4
rfile = path + '/input.fullRShist.' + names[i] + '.dat' 
readcol,rfile,ra,dec,z,format='D,D,D',/silent 
g = where((z gt zlb[i]) and (zub[i] gt z))
mu = mean(z[g])
var = variance(z[g])
gaussx = (DINDGEN(10000)-5000)/10000.0 + mu
gaussy = 10*exp(-0.5*(mu-gaussx)^2/var)
readcol,'/home/rumbaugh/1757.cdf.plot.dat',zs,cdf,format='D,D',/silent
readcol,'/home/rumbaugh/1757.cdf2.plot.dat',cdf2x,cdf2y,format='D,D',/silent
plot,[0-1],[0-1],/nodata,title=names2[i],xtitle='Redshift',ytitle='Num. of Galaxies',xrange=[zlb[i],zub[i]],yrange=[0,ymax[i]],xstyle=1,ystyle=1,CHARSIZE=1.3,CHARTHICK=3,XTHICK=8,YTHICK=8 
Histoplot,z,maxinput=zub[i],mininput=zlb[i],BINSIZE=bsize[i],thick=thicks[i],datacolorname='Black',/oplot
;oplot,zs,10*cdf,linestyle=1
oplot,cdf2x,10*cdf2y,linestyle=1
oplot,gaussx,gaussy
end

