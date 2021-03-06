SELECT y.COADD_OBJECTS_ID,ms.SP_ROWNUM,y.RA as ra_y1a1,y.DEC as dec_y1a1,sp.sdr7id,sp.mjd_r_sdss,sp.ra, sp.dec,sp.G_POSS,sp.R_POSS,sp.I_POSS,sp.g_err as G_POSS_err,sp.r_err as R_POSS_err,sp.i_err as I_POSS_err,sp.G_SDSS,sp.R_SDSS,sp.I_SDSS,sp.g_sdss_err as G_SDSS_err,sp.r_sdss_err as R_SDSS_err,sp.i_sdss_err as I_SDSS_err
FROM des_admin.Y1A1_COADD_OBJECTS y,SDSSPOSS_Y1A1_MATCH ms,SDSSPOSS_RELEASE sp 
where ms.coadd_objects_id=y.coadd_objects_id 
and ms.SP_ROWNUM=sp.sp_rownum; > milliquas_lightcurve_entries_SDSSPOSS_Y1A1.tab
