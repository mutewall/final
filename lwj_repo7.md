# 第七次作业

廖沩健

自动化65

2160504124

提交日期:  2019年5月10日

摘要:

这次作业聚焦于图像的边缘提取和直线检测。相关的算法都是直接使用python的cv库接口，所以结果的应该都是绝对正确的。这样，我就可以将更多的精力放在分析结果上。边缘提取部分，我选用了Sobel算子与Canny算法进行对比，总体上来说，Canny算法效果要好很多，具体结果分析见下方；直线检测部分在Canny算法提取了边缘的基础上使用Hough变换，通过改变原点的距离，与X轴的夹角，阈值三个参数进行了充分的对比，总体上来说，简单图像上，三组参数的值分别为1，1（度），100时，产生的效果是不错的；而对于复杂的图片，则需要针对性的调参，其中调节角度这个参数得到的效果是最好的，这是比较好调整的参数。


## 边缘提取
##＃ Sobel算子
#### test1
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_s.png)

#### test2
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_s.bmp)

#### test3
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_s.bmp)

#### test4
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_s.bmp)

#### test5
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test5.png_s.bmp)

#### test6
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_s.bmp)

## Canny算法
#### test1
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_c.bmp)

#### test2
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_c.bmp)

#### test3
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_c.bmp)

#### test4
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_c.bmp)

#### test5
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test5.png_c.bmp)

#### test6
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_c.bmp)

从上面的结果，可以看出，Canny算法提取的效果更好，表现为边界更加清晰，更加完整，但有点缺陷就是在图像较为复杂时，提取的边界会比较不准确，这可能和参数设置不当有关，而Sobel算子提取的边界非常暗淡，有时候还是不完整的，中间会断掉，但对于比较复杂的图来说，反而更能有重点的提取，而不是整个画面都充满了边界。

## 直线检测
以下的直线检测都是基于Canny算法提取的边界结果，P表示参数ρ（到原点距离）的精度，R表示参数θ（与x轴夹角）的精度（单位为度），T表示一组参数成为直线参数的阈值。
### test1
#### P = 1, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_1_0.0174532925199_100.bmp)
#### P = 2, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_2_0.0174532925199_100.bmp)
#### P = 1, R = 2, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_1_0.0349065850399_100.bmp)
#### P = 1, R = 1, T = 120
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test1.tif_1_0.0174532925199_120.bmp)

### test2
#### P = 1, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_1_0.0174532925199_100.bmp)
#### P = 2, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_2_0.0174532925199_100.bmp)
#### P = 1, R = 2, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_1_0.0349065850399_100.bmp)
#### P = 1, R = 1, T = 120
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test2.png_1_0.0174532925199_120.bmp)

### test3
#### P = 1, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_1_0.0174532925199_100.bmp)
#### P = 2, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_2_0.0174532925199_100.bmp)
#### P = 1, R = 2, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_1_0.0349065850399_100.bmp)
#### P = 1, R = 1, T = 120
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test3.jpg_1_0.0174532925199_120.bmp)

### test4
#### P = 1, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_1_0.0174532925199_100.bmp)
#### P = 2, R = 1, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_2_0.0174532925199_100.bmp)
#### P = 1, R = 2, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_1_0.0349065850399_100.bmp)
#### P = 1, R = 1, T = 120
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test4.bmp_1_0.0174532925199_120.bmp)

### test5
#### P = 1, R = 1, T = 200
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test5.png_1_0.0174532925199_200.bmp)
#### P = 1, R = 0.5, T = 200
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test5.png_1_0.00872664625997_200.bmp)
#### P = 1, R = 1, T = 220
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test5.png_1_0.0174532925199_220.bmp)


### test6
#### P = 5, R = 9, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_5_0.157079632679_100.bmp)
#### P = 10, R = 9, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_10_0.157079632679_100.bmp)
#### P = 5, R = 36, T = 100
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_5_0.628318530718_100.bmps)
#### P = 5, R = 9, T = 200
![](https://raw.githubusercontent.com/mutewall/homework_img/master/test6.jpg_5_0.157079632679_200.bmp)

对每个测试图片我都采用了4组不同的参数,每组改变其中一个参数，剩下3个不变。可以发现，对于不同的图片，不同的参数改变会带来不同的效果。但总体趋势是一致的，当P增大时，图片上会增加很多线，但其实大部分是冗余的，很多线都是没有价值的；当R增大时，图上的线会减少，尤以比较倾斜的线为主，在较复杂的图中，这是一个值得调整的参数，它可以减少更多不必要的直线；增大记录阈值，直线也会减少，但比较依赖图片的内容，也就是说随着图片内容的复杂程度的不同，它的效果也是参差不齐的，难以调整。