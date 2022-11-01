from importlib.metadata import files
import cv2
import os
from PIL import Image
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
from sklearn.model_selection import train_test_split
import random
import requests
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
import zipfile

os.environ['TF_CPP_MIN_LEVEL'] = '2'


main_path = r"C:/Users/amad_/makeaiwork2/projects/apple_disease_classification/data/Train"

r = []
for dictname in os.listdir(main_path):
    train_path = f"C:/Users/amad_/makeaiwork2/projects/apple_disease_classification/data/Train/{dictname}"
    # print(train_path)
    images = []

    for filename in os.listdir(train_path):
        img = cv2.imread(os.path.join(train_path,filename))
        if img is not None:
            images.append(img)
            r.append(images)



            
    # print(len(images))




#-----------------------------------------------------------------------------------------------------------------

# get file names
riverDirectory = 'C:/Users/amad_/makeaiwork2/opdrachten/practica/week10/Train/Blotch_Apple'
edgeFiles = list()
 
for filename in os.listdir(riverDirectory):
    imgFile = os.path.join(riverDirectory, filename)
    edgeFiles.append(imgFile)
    
    
# txtFiles = list()

# for txtFile in dataFile.namelist():
#     txtFiles.append(txtFile)
#     # print(txtFile)

edgeFiles = [img for img in edgeFiles if ".jpg" in img]

# print(edgeFiles)

# imageObjects = np.zeros([len(edgeFiles), 64, 64, 3])


# i = 0

# for pic in edgeFiles:
#     imageObjects[i] = np.asarray(Image.open(pic)).astype('uint8')/255
#     i += 1
    
# print(imageObjects)    





imageLabels = np.empty(len(r), dtype = 'S20')

i = 0

for label in r:
    edgeFiles[i] = label.replace("\\","/").split('/')[2]
    i += 1

    

labelNames, labelNumbers = np.unique(r, return_inverse=True)
# print(labelNames)
labelDict = dict(zip(np.unique(labelNumbers), labelNames))
# print(labelNames)

#print("labelNumbers", labelNumbers)
#print("LabelNumbers Length", len(labelNumbers))


# print("imageObjects", len(imageObjects))

np.array(np.unique(labelNumbers, return_counts=True)).T


trainSet, testSet, trainLabels, testLabels = train_test_split(r, labelNumbers, stratify = labelNumbers, train_size = 0.5, random_state=42)
print(trainSet.shape)
nrOfImages = len(trainSet)

print (len(trainSet), len(testSet),len(trainLabels), len(testLabels))