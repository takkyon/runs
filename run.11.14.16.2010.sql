SELECT y.COADD_OBJECTS_ID,ms.MQ_ROWNUM,y.RA,y.DEC,y.mag_auto_g,o.magerr_auto_g,y.mag_auto_r,o.magerr_auto_r,y.mag_auto_i,o.magerr_auto_i,y.mag_auto_z,o.magerr_auto_z,y.mag_auto_Y,o.magerr_auto_Y,y.mag_model_g,o.magerr_model_g,y.mag_model_r,o.magerr_model_r,y.mag_model_i,o.magerr_model_i,y.mag_model_z,o.magerr_model_z,y.mag_model_Y,o.magerr_model_Y,y.mag_psf_g,o.magerr_psf_g,y.mag_psf_r,o.magerr_psf_r,y.mag_psf_i,o.magerr_psf_i,y.mag_psf_z,o.magerr_psf_z,y.mag_psf_Y,o.magerr_psf_Y,y.mag_hybrid_g,o.magerr_hybrid_g,y.mag_hybrid_r,o.magerr_hybrid_r,y.mag_hybrid_i,o.magerr_hybrid_i,y.mag_hybrid_z,o.magerr_hybrid_z,y.mag_hybrid_Y,o.magerr_hybrid_Y FROM des_admin.Y1A1_COADD_OBJECTS y,milliquas_y1a1_match ms where ms.coadd_objects_id=y.coadd_objects_id; > milliquas_lightcurve_entries_y1a1_coadd.tab
