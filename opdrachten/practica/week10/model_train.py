from ast import Pass
from curses.ascii import FF
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from keras.models import Sequential
import tkinter as tk
from tkinter import simpledialog
from easygui import *
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping


#UI
# choices = ["Model","+ Data Augmentation", "+ Early Stopping"]
# optie = buttonbox('Kies een optie', "Opties", choices = choices)

data_dir = 'C:/Users/amad_/makeaiwork2/projects/apple_disease_classification/data/Train'

img_height = 250
img_width = 250
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

train_label = train_ds.class_names

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

val_label = val_ds.class_names


class_names = train_ds.class_names
plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
        for i in range(9):
            ax = plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            plt.title(class_names[labels[i]])
            plt.axis("off")

#sets
print(train_label)
print(val_label)

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

num_classes = len(class_names)

import numpy as np
import tkinter as tk
from tkinter import simpledialog
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from keras.models import Sequential
import pathlib

model = keras.models.load_model('C:/Users/amad_/makeaiwork2/projects/apple_disease_classification/models/new_model')


link = simpledialog.askstring(title="Test",
                                  prompt="link:")
image_url = f"{link}"
ind_link = link.rfind('/') +1


url_str = image_url[ind_link:(len(image_url))]


image_path = tf.keras.utils.get_file(url_str, origin=link)

img = tf.keras.utils.load_img(
    image_path, target_size=(img_height, img_width)
)
img_array = tf.keras.utils.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format(class_names[np.argmax(score)], 100 * np.max(score))
)

