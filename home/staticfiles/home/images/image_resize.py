import cv2
name = 'instagram_6.jpg'
width, height = 720, 720
img = cv2.imread(name)

t = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
# cv2.imshow('exampleshq', t)
cv2.imwrite(name, t)
cv2.waitKey(0)
