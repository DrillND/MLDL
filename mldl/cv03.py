import time

import cv2

image = cv2.imread('main.jpg', cv2.IMREAD_COLOR)
roi = image[10:300,250:500]
print(roi.shape)

image[0:290,0:250] = roi

'''b g r 순서 '''
image[300:,300:,0] = 0
cv2.imshow('image',image)
cv2.waitKey(0)

