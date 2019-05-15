from __future__ import print_function, division
import cv2
import numpy as np

def load_file(file):
    img = cv2.imread(file)
    return img

def save_file(name, file):
    cv2.imwrite('./res/{}.bmp'.format(name), file)

def sobel(img):
    return cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)

def canny(img):
    return cv2.Canny(img, 50, 150)

def edge_detect(name):
    img = load_file(name)
    img_s = sobel(img)
    img_c = canny(img)
    save_file('{}_s'.format(name), img_s)
    save_file('{}_c'.format(name), img_c)
    return img_c

def hough(name, edges, rho_precision=1, theta_precision=np.pi/180, threshold=200):
    img = load_file(name)
    lines = cv2.HoughLines(edges, rho_precision, theta_precision, threshold)
    print(lines.shape)
    for i in range(len(lines)):
        for rho,theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(0,0,255),1)
    save_file('{}_{}_{}_{}'.format(name, rho_precision, theta_precision, threshold), img)
    

if __name__ == '__main__':
    # test1_c = edge_detect('test1.tif')
    # hough('test1.tif', test1_c)
    # hough('test1.tif', test1_c, threshold=120)
    # hough('test1.tif', test1_c, rho_precision=2)
    # hough('test1.tif', test1_c, theta_precision=np.pi/90)

    # test2_c = edge_detect('test2.png')
    # hough('test2.png', test2_c)
    # hough('test2.png', test2_c, threshold=120)
    # hough('test2.png', test2_c, rho_precision=2)
    # hough('test2.png', test2_c, theta_precision=np.pi/90)

    # test3_c = edge_detect('test3.jpg')
    # hough('test3.jpg', test3_c)
    # hough('test3.jpg', test3_c, threshold=120)
    # hough('test3.jpg', test3_c, rho_precision=2)
    # hough('test3.jpg', test3_c, theta_precision=np.pi/90)

    # test4_c = edge_detect('test4.bmp')
    # hough('test4.bmp', test4_c)
    # hough('test4.bmp', test4_c, threshold=120)
    # hough('test4.bmp', test4_c, rho_precision=2)
    # hough('test4.bmp', test4_c, theta_precision=np.pi/90)
    
    test5_c = edge_detect('test5.png')
    hough('test5.png', test5_c)
    hough('test5.png', test5_c, threshold=220)
    hough('test5.png', test5_c, rho_precision=2)
    hough('test5.png', test5_c, theta_precision=np.pi/360)
    
    # test6_c = edge_detect('test6.jpg')
    # hough('test6.jpg', test6_c)
    # hough('test6.jpg', test6_c, threshold=200)
    # hough('test6.jpg', test6_c, rho_precision=10)
    # hough('test6.jpg', test6_c, theta_precision=np.pi/5)


    

 
    