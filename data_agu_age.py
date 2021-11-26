import cv2 as cv
import numpy as np
import os
import argparse
import time
import math
from skimage import img_as_ubyte, img_as_float
import random

def HtoBGR(hh, ss, ii):
    h = hh.copy()  # np.multiply(hh,(180.0/math.pi))#to
    s = ss.copy()
    v = ii.copy()
    red, green, blue = np.zeros(h.shape), np.zeros(h.shape), np.zeros(h.shape)
    flag = 0  # nose
    greToRad = math.pi/180
    for k in range(rows):
        for j in range(cols):
            flag = 0
            if h[k][j] <= 1.2e-16 or (np.isnan(h[k][j]) == 1):
                if s[k][j] <= 1.2e-16 or (np.isnan(s[k][j]) == 1):
                    flag = 1
                    blue[k][j] = i[k][j]
                    green[k][j] = i[k][j]
                    blue[k][j] = i[k][j]
            if flag == 0:
                if h[k][j] < (120*greToRad):
                    blue[k][j] = i[k][j]*(1-s[k][j])
                    red[k][j] = i[k][j] * \
                        (1 + ((s[k][j] * math.cos(h[k][j])) /
                         math.cos((math.pi/3) - h[k][j])))
                    green[k][j] = (i[k][j]*3) - (red[k][j] + blue[k][j])

                elif h[k][j] >= (120*greToRad) and h[k][j] < (240*greToRad):
                    h[k][j] = h[k][j]-(math.pi*2/3.0)

                    red[k][j] = i[k][j]*(1-s[k][j])
                    green[k][j] = i[k][j] * \
                        (1 + ((s[k][j] * math.cos(h[k][j])) /
                         math.cos((math.pi/3) - h[k][j])))
                    blue[k][j] = (i[k][j]*3) - (red[k][j] + green[k][j])
                elif h[k][j] >= (240*greToRad) and h[k][j] < (360*greToRad):
                    h[k][j] = h[k][j]-(math.pi*4/3.0)

                    green[k][j] = i[k][j]*(1-s[k][j])
                    blue[k][j] = i[k][j] * \
                        (1 + ((s[k][j] * math.cos(h[k][j])) /
                         math.cos((math.pi/3) - h[k][j])))
                    red[k][j] = (i[k][j]*3) - (green[k][j] + blue[k][j])
            if red[k][j] > 255:
                red[k][j] = 255
            if red[k][j] < 0:
                red[k][j] = 0
            if green[k][j] > 255:
                green[k][j] = 255
            if green[k][j] < 0:
                green[k][j] = 0
            if blue[k][j] > 255:
                blue[k][j] = 255
            if blue[k][j] < 0:
                blue[k][j] = 0

    return red, green, blue

def a1(imgg):
    HSV = cv.cvtColor(imgg,cv.COLOR_BGR2HSV)
    RR1,RR2,RR3,RR4,RR5,RR6,RR7,RR8,RR9 = HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy()
# [:,:,1] = saturation, [:,:,2]=valor mas o menos lumination
    RR1[:,:,1] = RR1[:,:,1]*0.25#value
    RR2[:,:,1] = RR2[:,:,1]*0.75#value
    RR3[:,:,1] = RR3[:,:,1]*.5#value
    RR4[:,:,2] = RR4[:,:,2]*0.25#value
    RR5[:,:,2] = RR5[:,:,2]*0.75#value
    RR6[:,:,2] = RR6[:,:,2]*.5#value
    RR7[:,:,1] = RR7[:,:,1]*0.25#value
    RR7[:,:,2] = RR7[:,:,2]*.75#value
    RR8[:,:,1] = RR8[:,:,1]*0.8#value
    RR8[:,:,2] = RR8[:,:,2]*.75#value
    RR9[:,:,1] = RR9[:,:,1]*0.5#value
    RR9[:,:,2] = RR9[:,:,2]*.75#value


    RR1 = cv.cvtColor(RR1,cv.COLOR_HSV2BGR)
    RR1 = cv.flip(RR1, 1)
    RR2 = cv.cvtColor(RR2,cv.COLOR_HSV2BGR)
    RR2 = cv.flip(RR2, 1)
    RR3 = cv.cvtColor(RR3,cv.COLOR_HSV2BGR)
    RR4 = cv.cvtColor(RR4,cv.COLOR_HSV2BGR)
    RR5 = cv.cvtColor(RR5,cv.COLOR_HSV2BGR)
    RR6 = cv.cvtColor(RR6,cv.COLOR_HSV2BGR)
    RR7 = cv.cvtColor(RR7,cv.COLOR_HSV2BGR)
    RR8 = cv.cvtColor(RR8,cv.COLOR_HSV2BGR)
    RR8 = cv.flip(RR8, 1)
    RR9 = cv.cvtColor(RR9,cv.COLOR_HSV2BGR)
    RR9 = cv.flip(RR9, 1)
    return RR1,RR2,RR3,RR4,RR5,RR6,RR7,RR8,RR9

#New a1: it takes account the number of images to be produced.
""" def a1(imgg):
    HSV = cv.cvtColor(imgg,cv.COLOR_BGR2HSV)
    RR1,RR2,RR3,RR4,RR5,RR6,RR7,RR8,RR9 = HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy(),HSV.copy()
# [:,:,1] = saturation, [:,:,2]=valor mas o menos lumination
    RR1[:,:,1] = RR1[:,:,1]*0.25#value
    RR2[:,:,1] = RR2[:,:,1]*0.75#value
    RR3[:,:,1] = RR3[:,:,1]*.5#value
    RR4[:,:,2] = RR4[:,:,2]*0.25#value
    RR5[:,:,2] = RR5[:,:,2]*0.75#value
    RR6[:,:,2] = RR6[:,:,2]*.5#value
    RR7[:,:,1] = RR7[:,:,1]*0.25#value
    RR7[:,:,2] = RR7[:,:,2]*.75#value
    RR8[:,:,1] = RR8[:,:,1]*0.8#value
    RR8[:,:,2] = RR8[:,:,2]*.75#value
    RR9[:,:,1] = RR9[:,:,1]*0.5#value
    RR9[:,:,2] = RR9[:,:,2]*.75#value


    RR1 = cv.cvtColor(RR1,cv.COLOR_HSV2BGR)
    RR1 = cv.flip(RR1, 1)
    RR2 = cv.cvtColor(RR2,cv.COLOR_HSV2BGR)
    RR2 = cv.flip(RR2, 1)
    RR3 = cv.cvtColor(RR3,cv.COLOR_HSV2BGR)
    RR4 = cv.cvtColor(RR4,cv.COLOR_HSV2BGR)
    RR5 = cv.cvtColor(RR5,cv.COLOR_HSV2BGR)
    RR6 = cv.cvtColor(RR6,cv.COLOR_HSV2BGR)
    RR7 = cv.cvtColor(RR7,cv.COLOR_HSV2BGR)
    RR8 = cv.cvtColor(RR8,cv.COLOR_HSV2BGR)
    RR8 = cv.flip(RR8, 1)
    RR9 = cv.cvtColor(RR9,cv.COLOR_HSV2BGR)
    RR9 = cv.flip(RR9, 1)
    return RR1,RR2,RR3,RR4,RR5,RR6,RR7,RR8,RR9 """

def pathStand(raw_path):
    raw_path = os.path.expanduser(raw_path)
    if raw_path[-1] == "/":
        path = raw_path
    else:
        path = raw_path+"/"
    print(path)
    return path

parser = argparse.ArgumentParser()
parser.add_argument("--folder", "-f", required=True,help="name of the folder containing the images")
parser.add_argument("--number_images", "-n", default=9 ,help="number of images produced for each image")
args = parser.parse_args()




folder = args.folder
number_images=int(args.number_images)

name_folder =folder.split('/')[-1]

#folder = "1_10"
rootPath= pathStand(folder)
print(f" Problem Path:  {name_folder}")
newPath= pathStand( os.path.normpath(rootPath + os.sep + os.pardir)+"/Augmented_Images/"+name_folder)
try:
    os.makedirs(newPath)
except:
    pass

#testPath = pathStand(folder.split('/')[:-1]+'/Nuevas')
images=os.listdir(rootPath)
print(images)
print(len(images))

#Acces to the new path and verify it is 0
nuevas=os.listdir(newPath)
print(f"There are {len(nuevas)} in the new folder {newPath}")


no_image=[]
#arr = os.listdir("originales/")
restantes=len(images)
for image in images:
        #fileName=image[:len(image)-3]+""+"jpg"
        fileName=str(image)
        #print(image)
        imagen=cv.imread(rootPath+image)
        if imagen is None:
          no_image.append(image)
          continue
        rows, cols = imagen.shape[0], imagen.shape[1]
        resultado=a1(imagen)
        resultado=list(resultado)
        #make a suffle
        random.shuffle(resultado)
        resultado=resultado[:number_images]
        cv.imwrite(newPath+fileName,imagen)
        for j in range (1,number_images):
            direccionName=newPath+fileName[:len(fileName)-4]+"_Ilumination_"+str(j)+".jpg"
            cv.imwrite(direccionName,resultado[j-1])
        restantes-=1
        print(f"Done {len(resultado)} images of {fileName}, faltan {restantes}")
        
print("End")
nuevas=os.listdir(newPath)
print(f"There are {len(nuevas)} in the new folder {folder}")