import time

import cv2

image = cv2.imread('main.jpg', cv2.IMREAD_COLOR)
bgr = image[100, 100]

print('3개 = ', bgr)
print('파란값 = ', bgr[0])
print('녹색값 = ', bgr[1])
print('빨간색값 = ', bgr[2])

starttime = time.time()
for x in range(0,100):
    for y in range(0,100):
        image[x,y] = [0,225,225]

print('걸린시간 = ', time.time()-starttime)

starttime = time.time()
image[200:300,300:] = [225,0,0]
print('걸린시간 = ', time.time()-starttime)

cv2.imshow('image',image)
cv2.waitKey(0)

