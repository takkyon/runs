SELECT r.TILENAME,f.RAC1,f.RAC2,f.RAC3,f.RAC4,f.DECC1,f.DECC2,f.DECC3,f.DECC4 
FROM FELIPE.COADDTILE_GEOM_NEW f, RUMBAUGH.Y1A1_TILENAMES_LIST r
WHERE r.TILENAME=f.TILENAME; >Y1A1_TILE_CORNERS.tab
