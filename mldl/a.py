import numpy as np

on = np.array([1,2,3,4])
np.save('a.npy',on)

filetonp = np.load('a.npy')
print(filetonp)
