import cv2
import matplotlib.pyplot as plt

'''
    300,400,3
    이미지 보여주는 방식은
    open CV
    cv2.imshow() 이미지 출력 bgr라이브러리
    matplotlib.pypolt
    plt.show()이미지 출력 rgb라이브러리
'''
img=cv2.imread('main.jpg',cv2.IMREAD_COLOR)
cv2.imshow('main',img)
cv2.waitKey(0)

img_resize = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC);
cv2.imshow('main',img_resize)
cv2.waitKey(0)

img_resize = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA);
cv2.imshow('main',img_resize)
cv2.waitKey(0)

print(img.shape)
# 좌표, 각도 , 배율
for i in range(513, 760, 3):
    M = cv2.getRotationMatrix2D((img.shape[0] / 2, img.shape[1] / 2), i, 0.5)

    '''
    고객이 이미지를 많이 안줄 때  
    '''
    # warpAffine 이미지를 변형하는 함수
    mimg = cv2.warpAffine(img, M, (img.shape[0], img.shape[1]))
    filename = './aimg/a' + str(i) + '.jpg'
    #cv2.imwrite('./aimg/a'+str(i)+'jpg',ming)

    cv2.imwrite(filename, mimg)
    #cv2.imshow('mimg',ming)
    #cv2.waitKey(0)