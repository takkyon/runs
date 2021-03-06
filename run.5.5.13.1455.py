import numpy as np
import os
os.chdir('/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
execfile("/local/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py")

files_dict = {'miki22_z': {'prefix': '110630_', \
'red': {'arc': 13, 'arc_array': np.array([13,55]), 'flat': 19, 'flat_array': np.array([17,18,19,58,59,60]), 'images': np.array([32,33,34,35,36,37,38,39,40,41,42,43])}, \
'blue': {'arc': 20, 'arc_array': np.array([20,80]), 'flat': 25, 'flat_array': np.array([23,24,25,83,84,85]), 'images': np.array([44,45,46,48,49,50,53,54,55,57,58,59])}}, \
'miki10.f': {'prefix': '110630_', \
'red': {'arc': 15, 'arc_array': np.array([15,57,64]), 'flat': 25, 'flat_array': np.array([23,24,25,65]), 'images': np.array([29,30,31])}, \
'blue': {'arc': 22, 'arc_array': np.array([22,82,89]), 'flat': 32, 'flat_array': np.array([30,31,32,90]), 'images': np.array([38,39,40])}}, \
'miki21_B': {'prefix': '110630_', \
'red': {'arc': 14, 'arc_array': np.array([14,56]), 'flat': 22, 'flat_array': np.array([20,21,22,61,62,63]), 'images': np.array([44,45,46,47,48])}, \
'blue': {'arc': 21, 'arc_array': np.array([21,81,]), 'flat': 29, 'flat_array': np.array([27,28,29,86,87,88]), 'images': np.array([68,69,70,72,73])}} \
}

indir = '/local/rumbaugh/LRIS/Marusa/LRIS5_062011/data'
outdir = '/local/rumbaugh/LRIS/Marusa/test/'
lris_reduce_multislit(indir,outdir,files_dict[mask]['prefix'],files_dict[mask],mask,colors=color,sides=[side])
