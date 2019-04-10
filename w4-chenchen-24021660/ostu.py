import cv2
import numpy
from matplotlib import pyplot
import matlab
fn1 = 'juxian1.png'
fn2 = 'juxian2.png'
fn3 = 'mili.png'
def fuc_calchist(m):
    image1 = cv2.imread(m)
    hist_cv = cv2.calcHist([image1], [0], None, [256], [0, 256])
    pyplot.plot(hist_cv)
    pyplot.show()
    cv2.imshow('pic',image1)
    cv2.waitKey()

def fuc_ostu(m):
    image = cv2.imread(m)
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    maxg=0
    thr=0
    for i in range(0,255):
        font=image1>i
        back=image1<=i
        font_count=numpy.sum(font)
        back_count=numpy.sum(back)
        if 0 == font_count:
            break
        if 0 == back_count:
            continue

        w0=float(font_count/image1.size)
        w1=float(back_count/image1.size)
        u0=float(numpy.sum(image1*font)/font_count)
        u1=float(numpy.sum(image1*back)/back_count)
        g=w0*w1*(u0-u1)*(u0-u1)
        if g>maxg:
            maxg=g
            thr=i

    ret,imotsu=cv2.threshold(image1,thr,255,0)
    cv2.imshow('otsu', imotsu)
    cv2.imshow('normal',image1)
    cv2.imshow('otsu',imotsu)
    cv2.waitKey()

def fuc_adaptive(m):
    image = cv2.imread(m)
    image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imotsu=cv2.adaptiveThreshold(image1,255,1,0,101,C=0)
    contours,hierarchy =cv2.findContours(imotsu,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  #这里返回两个参数，填的参数需要看一下
    count=0
    sumh=0
    sumarea=0
    c_h=0
    c_area=0
    for n in range(0,len(contours)):
        area=cv2.contourArea(contours[n])
        if area<10:
            continue
        count+=1
        rect=cv2.boundingRect(contours[n])
        #rect = cv2.minAreaRect(contours[n])
        h=rect[2]
        if rect[3]>rect[2]:
            h=rect[3]
        sumh+=h
        sumarea+=area
        print('第'+str(count)+'粒米粒长度为：'+str(h)+'，面积为：'+str(area))
        cv2.rectangle(image,rect,(0,0,255),1)
        cv2.putText(image,str(count),(rect[0],rect[1]),fontScale=0.5,fontFace=cv2.FONT_HERSHEY_PLAIN,color=(0,255,0))
    p_h=sumh/count
    p_area=sumarea/count
    for n in range(0,len(contours)):
        area=cv2.contourArea(contours[n])
        if area<10:
            continue
        rect = cv2.boundingRect(contours[n])
        h = rect[2]
        if rect[3] > rect[2]:
            h = rect[3]
        c_h+=(h-p_h)*(h-p_h)
        c_area+=(area-p_area)*(area-p_area)
    fc_h=c_h/count
    fc_area=c_area/count
    print('长度均值为：'+str(p_h)+'，长度方差为：'+str(fc_h)+'，面积均值为：'+str(p_area)+'，面积方差为：'+str(fc_area))
    cv2.drawContours(image,contours[n],-1,(0,0,255),1)
    #cv2.imshow('normal',imotsu)
    cv2.imshow('otsu', image)  #最后需要回到彩色图像上才能有红色的轮廓
    cv2.waitKey()


fuc_adaptive(fn3)