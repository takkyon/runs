import numpy as np

data = np.array([-2.6,1.75,1.8,3.2,0.1,-2.75,-3.25,-1.7,-4.25,-0.8,-1,1.1,3,2.5,-1.75,-3.25,4,-3.2,-1.6,-0.75,2.25,0.7,-2.1,-3.35,1.3,2.8,0,1.8,2.3,3.2,0.4,4.5,2,-4.75,-1.3,1.4,-4.5,-6.5,-0.5,4.5,1.5,-3.8,-3.75,-4.9,-2.25,2.1,0.8,-0.1,1.4,0.3,-1.8,2.6,1.3,3.1,3.85,4.2,5.6,-0.25])
print np.std(data)
print np.sqrt(np.mean(data**2))
