from importlib.metadata import files
import cv2
import os

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



            
    print(len(images))

print(r)