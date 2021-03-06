import numpy as np
import pyfits as py
execfile('/home/rumbaugh/git/data_redux_code/spec_simple.py')
obs_dict = {}
#blue_ID_list = np.array([192,189,190,191,195,196,197,198,199,200,201,366,367,368,369,375,376,377,378])
#red_ID_list = np.array([141,132,133,140,151,158,159,174,175,182,342,343,350,351,369,370,377,378])
blue_ID_list = np.array([195,196,197,198,199,200,201,366,367,368,369,375,376,377,378])
red_ID_list = np.array([151,158,159,174,175,182,342,343,350,351,369,370,377,378])

def plot_spec(ID,side):
    figure(1)
    clf()
    smooth_boxcar('/home/rumbaugh/KAST/Science/spec_skysub.%s%i.dat'%(side,ID),5)
    savefig('/home/rumbaugh/KAST/plots/spec_skysub.%s%i.smooth_5.png'%(side,ID))

for ID in blue_ID_list: plot_spec(ID,'b')
for ID in red_ID_list: plot_spec(ID,'r')
