import numpy as np
import matplotlib.pyplot as plt

fruits = np.load('fruits_300.npy')
print(fruits.shape)

print(fruits[0,0,:])
#plt.imshow(fruits[0],cmap='gray')
#plt.show()


fig,axis = plt.subplots(1,2)
axis[0].imshow(fruits[100],cmap='gray_r')
axis[1].imshow(fruits[200],cmap='gray_r')

plt.savefig('fru.jpg')
plt.close()


#이미지 픽셀 분석하기 월요일