from PIL import  Image
import random


def main():
    image1 = Image.open('example1.jfif')
    image2 = Image.open('example2.jfif')
    #image1.show()
    #print(image1.size)
    #print(image1.format)
    #print(image1.mode)
        #图片信息


    #rect = (200, 200, 800, 800)
        #左，上，右，下
    #image1_cut=image1.crop(rect)
    #image1_cut.show()
    #print(image1_cut.size)
    #print(image1_cut.format)
    #print(image1_cut.mode)

    #size = (80, 128)
    #image1.thumbnail(size)
        #改变内存中图片自身
        #按照原比例缩小，size中保护占原图比小的一侧
    #image1.show()
    #print(image1.size)

    #image1_change=image1.resize((110,154))
    #image1_change.show()
        #拉伸变换

    # rect = (200, 200, 800, 800)
    # 左，上，右，下
    # image1_cut=image1.crop(rect)
    # image1_cut.show()
    # print(image1_cut.size)
    # print(image1_cut.format)
    # print(image1_cut.mode)

    #rect = (750, 100, 1200, 600)
    #image2_cut = image2.crop(rect)
    #image1.paste(image2_cut,(250,200))
        #设置粘贴位置，改变自身
    #image1.show()


    #image1_rotate=image1.rotate(75)
    #image1_rotate.show()
        #旋转 保留原来的图片格式

    #image1_transpose=image1.transpose(Image.FLIP_LEFT_RIGHT)
    #image1_transpose.show()
        #镜像

    #for x in range(250, 700):
        #for y in range(200, 700):
            #color1=  random.randint(0,80)
            #color2 = random.randint(80, 160)
            #color3 = random.randint(160, 240)
            #image1.putpixel((x, y), (color1, color2, color3))
                #前面是像素位置，后面是rgb
    #image1.show()

    from PIL import ImageFilter

    #image1_filter1=image1.filter(ImageFilter.CONTOUR)
    #image1_filter1.show()
        #捕捉边缘
    #image1_filter2 = image1.filter(ImageFilter.BLUR)
    #image1_filter2.show()
        #模糊化
    #image1_filter3 = image1.filter(ImageFilter.DETAIL)
    #image1_filter3.show()
        #锐化
        #要用再查
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
