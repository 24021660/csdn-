import cv2

#创建第一个视觉程序“hello world！”，显示lena图片
fn='timg.jpeg'
image=cv2.imread(fn)
cv2.imshow('Hello World!',image)
cv2.waitKey(0)



