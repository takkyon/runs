print,' '
print,'Make sure you set strname equal to the string form of the chandra ID'
print,' '


;;;; Read in Photometry catalogs
 photcat1 = 'stats.radec_netcntscor_netcnts_cnts_sig_flux.soft.dat'
 readcol, photcat1, id_soft,ra_soft,dec_soft,netcnts_corr_soft,netcnts_soft,counts_soft,sig_soft,offaxis_soft,flux_soft,wmask_soft,wsigf_soft,wsigs_soft,wsigh_soft, format='I,D,D,D,D,D,D,D,D,D,D,D,D'
 photcat2 = 'stats.radec_netcntscor_netcnts_cnts_sig_flux.hard.dat'
 readcol, photcat2, id_hard,ra_hard,dec_hard,netcnts_corr_hard,netcnts_hard,counts_hard,sig_hard,offaxis_hard,flux_hard,wmask_hard,wsigf_hard,wsigs_hard,wsigh_hard, format='I,D,D,D,D,D,D,D,D,D,D,D,D'

;;;; Set minimum counts to zero
 netcnts_corr_softz = netcnts_corr_soft  &  netcnts_corr_hardz = netcnts_corr_hard
 netcnts_corr_softz[where(netcnts_corr_softz lt 0.0)] = 0.0
 netcnts_corr_hardz[where(netcnts_corr_hardz lt 0.0)] = 0.0

 netcnts_softz = netcnts_soft  &  netcnts_hardz = netcnts_hard
 netcnts_softz[where(netcnts_softz lt 0.0)] = 0.0
 netcnts_hardz[where(netcnts_hardz lt 0.0)] = 0.0

;;;; Get Full band counts & flux
 flux_softz = flux_soft  &  flux_hardz = flux_hard
 flux_softz[where(flux_softz lt 0.0)] = 0.0
 flux_hardz[where(flux_hardz lt 0.0)] = 0.0

 netcnts_corr_fullz = netcnts_corr_softz + netcnts_corr_hardz 
 flux_fullz = flux_softz + flux_hardz

;;;; Get full and composite signifigances
 sig_full = (netcnts_softz+netcnts_hardz) / (1.0 + SQRT(0.75 + ((counts_soft-netcnts_soft)+(counts_hard-netcnts_hard)))) 
 sig_max = make_array(n_elements(sig_soft))
 sig_max = sig_soft
 for i=0, n_elements(sig_max)-1 do begin &$
   if sig_hard[i] gt sig_max[i] then sig_max[i] = sig_hard[i] &$
   if sig_full[i] gt sig_max[i] then sig_max[i] = sig_full[i] &$
 endfor

 sig_soft[where(sig_soft le 0)] = 0
 sig_hard[where(sig_hard le 0)] = 0


;;;; Make flag which determines which band the position was measured (this is in the combined source list)
 readcol, '../sources.' + strname + '.full+soft+hard.srclist.dat', ra_temp_temp, dec_temp, mask_temp, sigf_temp, sigs_temp, sigh_temp, ncnts_f, ncnts_s, ncnts_h,wflag, format='D,D,A,D,D,D,I'


;;;; output final catalog
 ra = ra_soft  &  dec = dec_soft   ; all ra,dec are the same by the time photometry gets carried out
 wsig_full = wsigf_hard
 wsig_soft = wsigs_hard
 wsig_hard = wsigh_hard
 wmask = wmask_soft

 openw, 1, strname + '.xray_phot.soft_hard_full.dat'
 for i=0, n_elements(ra)-1 do printf,1, ra[i], dec[i], flux_softz[i], flux_hardz[i], flux_fullz[i],  netcnts_corr_softz[i], netcnts_corr_hardz[i], netcnts_corr_fullz[i], sig_soft[i], sig_hard[i], sig_full[i], wsig_soft[i], wsig_hard[i], wsig_full[i], wmask[i], wflag[i],format='(1(G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",G," ",I," ",I," "))'
 close, 1

end
