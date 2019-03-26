import cv2
import numpy



#rgb分量
fn='timg.jpeg'
image1=cv2.imread(fn)
image=numpy.mat
bgrs=numpy.mat
hsv=numpy.mat
hsvs=numpy.mat
image=cv2.pyrDown(image1)
bgrs=cv2.split(image)
cv2.imshow('source image',image)
cv2.imshow('b',bgrs[0])
cv2.imshow('g',bgrs[1])
cv2.imshow('r',bgrs[2])
cv2.waitKey()

#hsv分量
hsv=cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)
hsvs=cv2.split(hsv)
cv2.imshow('Hue',hsvs[0])
cv2.imshow('Saturation',hsvs[1])
cv2.imshow('Value',hsvs[2])
cv2.waitKey()



