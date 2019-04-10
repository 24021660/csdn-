import cv2

fn='timg.jpeg'
image=cv2.imread(fn)
image1=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
def fuc_sobel():
    fn_sobel=cv2.Sobel(image1,dx=1,dy=0,ddepth=-1)
    fn_sobel2 = cv2.Sobel(image1, dx=0, dy=1, ddepth=-1)
    fn_sobel3 = cv2.Sobel(image1, dx=1, dy=1, ddepth=-1)
    fn_sobel4=cv2.addWeighted(fn_sobel,0.5,fn_sobel2,0.5,0)
    cv2.imshow('sobel',fn_sobel)
    cv2.imshow('sobel2', fn_sobel2)
    cv2.imshow('sobel3', fn_sobel3)
    cv2.imshow('sobel4', fn_sobel4)
    cv2.waitKey()

def fuc_canny_yuzhi():
    gaussian_image=cv2.GaussianBlur(image1,(3,3),1)
    fn_canny=cv2.Canny(gaussian_image,30,50)
    fn_canny2 = cv2.Canny(gaussian_image, 50, 70)
    fn_canny3 = cv2.Canny(gaussian_image, 100, 120)
    cv2.imshow('sobel', fn_canny)
    cv2.imshow('sobel2', fn_canny2)
    cv2.imshow('sobel3', fn_canny3)
    cv2.waitKey()

def fuc_canny_jianju():
    gaussian_image=cv2.GaussianBlur(image1,(3,3),1)
    fn_canny=cv2.Canny(gaussian_image,30,50)
    fn_canny2 = cv2.Canny(gaussian_image, 30, 70)
    fn_canny3 = cv2.Canny(gaussian_image, 30, 100)
    cv2.imshow('sobel', fn_canny)
    cv2.imshow('sobel2', fn_canny2)
    cv2.imshow('sobel3', fn_canny3)
    cv2.waitKey()

def func_canny_sobel():
    gaussian_image = cv2.GaussianBlur(image1, (3, 3), 1)
    fn_sobel = cv2.Sobel(image1, dx=1, dy=0, ddepth=-1)
    fn_sobel2 = cv2.Sobel(image1, dx=0, dy=1, ddepth=-1)
    fn_sobel3 = cv2.addWeighted(fn_sobel, 0.5, fn_sobel2, 0.5, 0)
    fn_canny = cv2.Canny(gaussian_image, 140, 150)
    cv2.imshow('sobel', fn_sobel3)
    cv2.imshow('canny', fn_canny)
    cv2.waitKey()

a=input('请输入以下数字：\n 1.sobel算子 \n 2.canny算子等距 \n 3.canny算子不等距 \n 4.canny与sobel比较' )
if a=='1':
    fuc_sobel()
elif a=='2':
    fuc_canny_yuzhi(1)
elif a=='3':
    fuc_canny_jianju()
elif a=='4':
    func_canny_sobel()
else:
    print('请输入1-5的其中一个数字！')
