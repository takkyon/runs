SELECT e.mjd_obs,o.expnum,y.COADD_OBJECT_ID,o.RA,o.DEC,o.mag_pointsource,o.band FROM des_admin.Y3A1_COADD_OBJECT_SUMMARY y, des_admin.y3a1_finalcut_object o,des_admin.y3a1_exposure e,des_admin.y3a1_wavg_oclink l where o.expnum=e.expnum and y.coadd_object_id=l.coadd_object_id and o.filename=l.se_object_filename and o.object_number=l.se_object_number and rownum<10;
