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
    maxg=0
    thr=0
    for i in range(0,255):
        font=image<i
        back=image>i
        font_count=numpy.sum(font)
        back_count=numpy.sum(back)
        w0=float(font_count/image.size)
        w1=float(back_count/image.size)
        u0=float(numpy.sum(image*font)/font_count)
        u1=float(numpy.sum(image*back)/back_count)
        g=w0*w1*(u0-u1)*(u0-u1)
        if g>maxg:
            maxg=g
            thr=i



    image1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,imotsu=cv2.threshold(image1,thr,255,0)
    cv2.imshow('123',imotsu)
    cv2.waitKey()


fuc_ostu(fn3)