import numpy as np
import os
os.chdir('/mnt/data2/rumbaugh/LRIS/Marusa/lrispipeline_marusa')
from LRIS.resample import resample
import pyfits,numpy
from LRIS.LRIStools import *
from LRIS.XSolve import *
execfile('/mnt/data2/rumbaugh/LRIS/Marusa/lrispipeline_marusa/lris_reduce_multislit.py')
execfile('/home/rumbaugh/LRIS_files_dict_master.py')

indir_dict = {'miki22.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki03_A': {'night': {'1': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", '2': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2"}}, 'miki04.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki04_A': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night1", 'miki21.f': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki03_B': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki04_B': "/mnt/data2/rumbaugh/LRIS/Marusa/LRIS2_092010/data_night2", 'miki16B.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'miki21C.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'miki21D.': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'bc3.file': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data', 'bc3B.fil': '/mnt/data2/rumbaugh/LRIS/Marusa/LRIS13_082011/data'}
outdir_dict = {'miki22.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki03_A': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04_A': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki21.f': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki03_B': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki04_B': "/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS2_092010/", 'miki16B.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'miki21C.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'miki21D.': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'bc3.file': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/', 'bc3B.fil': '/mnt/data2/rumbaugh/LRIS/Marusa/reduced/LRIS13_082011/'}

for mask in [mask]:
	if mask == 'miki03_A':
		try:
			nights
		except NameError:
			nights = ['1','2']
		for night in nights:
			lris_reduce_multislit(indir_dict[mask]['night'][night],outdir_dict[mask],files_dict[mask]['night'][night]['prefix'],files_dict[mask]['night'][night],mask,colors=color,sides=[side])
	else:
		lris_reduce_multislit(indir_dict[mask],outdir_dict[mask],files_dict[mask]['prefix'],files_dict[mask],mask,colors=color,sides=[side])
