from PIL import Image
import numpy as np
import cv2
from math import sqrt


def getVecLen(vec):
    return sqrt(vec[0]**2+vec[1]**2+vec[2]**2)

def rgbTheSame(r,g,b,color):
    return r**2+g**2+b**2 - getVecLen(color) < 25000


def getWallCords2(imagePath):
    try :
        image = Image.open(imagePath)
        pixels = image.load()
        width, height = image.size
        stonePixel = [255, 255, 255]

        for i in image.getdata():

            if i[0] < stonePixel[0] and i[1] < stonePixel[1] and i[2] < stonePixel[2] or getVecLen(i) < getVecLen(
                stonePixel):
                stonePixel = i

        # print(stonePixel)

        Temp = []
        rgb_im = image.convert('RGB')
        for x in range(1,width-1):
            for y in range(1,height-1):
                r, g, b = rgb_im.getpixel((x, y))
                r1,g1,b1 = rgb_im.getpixel((x -1, y -1))
                r2,g2,b2 = rgb_im.getpixel((x -1, y ))
                r3,g3,b3 = rgb_im.getpixel((x -1, y +1))
                r4,g4,b4 = rgb_im.getpixel((x ,y-1 ))
                r5,g5,b5 = rgb_im.getpixel((x , y +1))
                r6,g6,b6 = rgb_im.getpixel((x +1, y))
                r7,g7,b7 = rgb_im.getpixel((x+1 , y -1))
                r8,g8,b8 = rgb_im.getpixel((x+1 , y +1))


                if rgbTheSame(r, g, b, stonePixel):
                    counter = 0
                    if (rgbTheSame(r5,g5,b5,stonePixel) and not rgbTheSame(r4,g4,b4,stonePixel) or not rgbTheSame(r5,g5,b5,stonePixel) and rgbTheSame(r4,g4,b4,stonePixel)):
                        if (rgbTheSame(r6, g6, b6, stonePixel) and not rgbTheSame(r2,g2,b2,stonePixel) or not rgbTheSame(r6,g6,b6,stonePixel) and rgbTheSame(r2,g2,b2,stonePixel)):
                            if not rgbTheSame(r1, g1, b1, stonePixel):
                                counter += 1
                            if not rgbTheSame(r3, g3, b3, stonePixel):
                                counter += 1
                            if not rgbTheSame(r7, g7, b7, stonePixel):
                                counter += 1
                            if not rgbTheSame(r8, g8, b8, stonePixel):
                                counter += 1

                    if counter == 3:
                        Temp += [[x, y]]

        imageDraw = np.zeros((height, width, 3), np.uint8)
        for element in Temp:
            x = element[1]
            y = element[0]
            imageDraw[x, y] = [105, 210, 15]

    # Save
        cv2.imwrite("result2.png", imageDraw)
        return Temp
    except FileExistsError:
        print("Wrong adress")
        return []



def getVecLen(vec):
    return vec[0]**2+vec[1]**2+vec[2]**2

def getWallCords(imagePath):
    try :
        image = Image.open(imagePath)
        pixels = image.load()
        width, height = image.size
        stonePixel = [255, 255, 255]

        for i in image.getdata():

            if i[0] < stonePixel[0] and i[1] < stonePixel[1] and i[2] < stonePixel[2] or getVecLen(i) < getVecLen(
                stonePixel):
                stonePixel = i

        # print(stonePixel)

        Temp = []
        rgb_im = image.convert('RGB')
        for x in range(1,width-1):
            for y in range(1,height-1):
                r, g, b = rgb_im.getpixel((x, y))
                r1,g1,b1 = rgb_im.getpixel((x -1, y -1))
                r2,g2,b2 = rgb_im.getpixel((x -1, y ))
                r3,g3,b3 = rgb_im.getpixel((x -1, y +1))
                r4,g4,b4 = rgb_im.getpixel((x ,y-1 ))
                r5,g5,b5 = rgb_im.getpixel((x , y +1))
                r6,g6,b6 = rgb_im.getpixel((x +1, y))
                r7,g7,b7 = rgb_im.getpixel((x+1 , y -1))
                r8,g8,b8 = rgb_im.getpixel((x+1 , y +1))


                if rgbTheSame(r, g, b, stonePixel):
                    counter = 0
                    if not rgbTheSame(r1,g1,b1, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r2,g2,b2, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r3,g3,b3, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r4,g4,b4, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r5,g5,b5, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r6,g6,b6, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r7,g7,b7, stonePixel):
                        counter+= 1
                    if not rgbTheSame(r8,g8,b8, stonePixel):
                        counter+= 1

                    if counter <  4:
                        Temp += [[x, y]]

        imageDraw = np.zeros((height, width, 3), np.uint8)
        for element in Temp:
            x = element[1]
            y = element[0]
            imageDraw[x, y] = [105, 210, 15]

    # Save
        cv2.imwrite("result2.png", imageDraw)
        return Temp, width
    except FileExistsError:
        print("Wrong adress")
        return []


# getWallCords2("flat3.jpg")

# image = cv2.imread('result2.png')
# image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
# bg=cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
# out_gray=cv2.divide(image, bg, scale=255)
# out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1]
#
# cv2.imshow('binary', out_binary)
# cv2.imwrite('binary.png',out_binary)
#
# cv2.imshow('gray', out_gray)
# cv2.imwrite('gray.png',out_gray)