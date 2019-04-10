import cv2
import numpy
fn='timg.jpeg'
image=cv2.imread(fn)
def fuc_blur(): #均值滤波
    fn_blur=cv2.blur(image,(3,3))
    fn_blur2=cv2.blur(image,(13,13))
    fn_blur3=cv2.blur(image,(23,23))
    cv2.imshow('normal',image)
    cv2.imshow('blur3*3',fn_blur)
    cv2.imshow('blur13*13',fn_blur2)
    cv2.imshow('blur23*23',fn_blur3)
    cv2.waitKey()


def fuc_gussblur_sigma(m):
    fn_blur = cv2.GaussianBlur(image,(3,3),m)
    fn_blur2 = cv2.GaussianBlur(image, (3, 3),m+10)
    fn_blur3 = cv2.GaussianBlur(image, (3, 3),m+20)
    cv2.imshow('normal', image)
    cv2.imshow('GaussianBlur3*3_1', fn_blur)
    cv2.imshow('GaussianBlur3*3_11', fn_blur2)
    cv2.imshow('GaussianBlur3*3_21', fn_blur3)
    cv2.waitKey()

def fuc_gussblur_ksize():
    fn_blur = cv2.GaussianBlur(image,(3,3),1)
    fn_blur2 = cv2.GaussianBlur(image, (5, 5),1)
    fn_blur3 = cv2.GaussianBlur(image, (7, 7),1)
    cv2.imshow('normal', image)
    cv2.imshow('GaussianBlur3*3', fn_blur)
    cv2.imshow('GaussianBlur13*13', fn_blur2)
    cv2.imshow('GaussianBlur23*23', fn_blur3)
    cv2.waitKey()

def fuc_gussblur_sigma_ksize():
    fn_blur = cv2.GaussianBlur(image,(3,3),1)
    fn_blur2 = cv2.GaussianBlur(image, (13, 13),11)
    fn_blur3 = cv2.GaussianBlur(image, (23, 23),21)
    cv2.imshow('normal', image)
    cv2.imshow('GaussianBlur3*3_1', fn_blur)
    cv2.imshow('GaussianBlur13*13_11', fn_blur2)
    cv2.imshow('GaussianBlur23*23_21', fn_blur3)
    cv2.waitKey()

def fuc_medianblur():
    fn_blur = cv2.medianBlur(image,5)
    fn_blur2 = cv2.medianBlur(image,9)
    fn_blur3 = cv2.medianBlur(image,13)
    cv2.imshow('normal', image)
    cv2.imshow('medianBlur5', fn_blur)
    cv2.imshow('medianBlur9', fn_blur2)
    cv2.imshow('medianBlur13', fn_blur3)
    cv2.waitKey()

def fuc_duibi():
    fn_blur = cv2.blur(image, (9, 9))
    fn_blur2 = cv2.GaussianBlur(image, (9, 9),1)
    fn_blur3 = cv2.medianBlur(image,9)
    cv2.imshow('normal', image)
    cv2.imshow('Blur5', fn_blur)
    cv2.imshow('GaussianBlur5*5', fn_blur2)
    cv2.imshow('medianBlur5', fn_blur3)
    cv2.waitKey()

def zaosheng_duibi():
    fn1='lvbo.png'
    image1=cv2.imread(fn1)
    fn_blur = cv2.blur(image1, (7, 7))
    fn_blur2 = cv2.GaussianBlur(image1, (3, 3), 4)
    fn_blur3 = cv2.medianBlur(image1, 7)
    cv2.imshow('normal', image1)
    cv2.imshow('Blur5', fn_blur)
    cv2.imshow('GaussianBlur5*5', fn_blur2)
    cv2.imshow('medianBlur5', fn_blur3)
    cv2.waitKey()

a=input('请输入以下数字：\n 1.均值滤波 \n 2.高斯滤波(σ取值依次增大) \n 3.高斯滤波（滤波器半径依次增大） \n 4.高斯滤波（σ与滤波器同时增大） \n 5.中值滤波（取值数依次增大) \n 6.lena三者比较 \n 7.椒盐噪声三者比较')
if a=='1':
    fuc_blur()
elif a=='2':
    fuc_gussblur_sigma(1)
elif a=='3':
    fuc_gussblur_ksize()
elif a=='4':
    fuc_gussblur_sigma_ksize()
elif a=='5':
    fuc_medianblur()
elif a=='6':
    fuc_duibi()
elif a=='7':
    zaosheng_duibi()
else:
    print('请输入1-5的其中一个数字！')

