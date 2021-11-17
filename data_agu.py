import argparse
import json
import logging
import os
import shutil
import cv2 as cv
import numpy as np
# import pandas as pd
import time

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO) 

def image_augmenter(arr):
        for i in arr:
                if i.endswith(".jpg"):
                        name = str(i) 
                        print(name)
                        imagen=cv.imread("female/"+i)
                        cont_err = 0
                        try:
                                #-----Converting image to LAB Color model----------------------------------- 
                                lab = cv.cvtColor(imagen, cv.COLOR_BGR2LAB)
                                #cv.imshow("lab",lab)
                                #-----Splitting the LAB image to different channels-------------------------
                                l, a, b = cv.split(lab)
                                #cv.imshow('l_channel', l)
                                #cv.imshow('a_channel', a)
                                #cv.imshow('b_channel', b)
                                #-----Applying CLAHE to L-channel-------------------------------------------
                                clahe = cv.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
                                cl = clahe.apply(l)
                                #cv2.imshow('CLAHE output', cl)
                                #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
                                limg = cv.merge((cl,a,b))
                                #cv2.imshow('limg', limg)
                                #-----Converting image from LAB Color model to RGB model--------------------
                                final = cv.cvtColor(limg, cv.COLOR_LAB2BGR)
                                #cv.imshow('final', final)

                                final = cv.flip(final, 1)
                                #direccionName="Contrasted/"+"Contrasted"+fileName[:len(fileName)-4]+".jpg"
                                cv.imwrite(f'female/augmented_{name}', final)
                                #cv.imwrite(direccionName,final)
                        except:
                                cont_err += 1 
                                pass
        print('No se aumentaron ' +str(cont_err)+ ' imagenes')


arr = os.listdir("female/")
inicio=time.time()
image_augmenter(arr)
fin=time.time()
print("Tiempo en segundos:" + str(fin-inicio))