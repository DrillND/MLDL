import cv02

image=cv02.imread('main.jpg', cv02.IMREAD_COLOR)
print(image.shape)

cv02.imshow('title', image)
askey = cv02.waitKey(0)
print('askey',askey)


cv02.imwrite('main_copy.jpg', image)

image_gray=cv02.cvtColor(image, cv02.COLOR_BGR2GRAY)
cv02.imshow('image_grey', image_gray)
cv02.waitKey(0)
cv02.imwrite('main_gray.jpg', image_gray)
'''
b g r 
b = 0 파란색 제외
b = 225 파란색 젤 강하게
'''
image[:,:,0] = 255
#image[ : , : , 1] = 0
#image[:,:,2] = 0
cv02.imshow('image', image)
cv02.waitKey(0)
cv02.putText(image, 'Korea', (50, 100), cv02.FONT_ITALIC, 2, 2)
cv02.imwrite('main_blue.jpg', image)

cv02.destroyAllWindows()

