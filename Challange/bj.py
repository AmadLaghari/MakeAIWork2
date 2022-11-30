import numpy as np
import tkinter as tk
from tkinter import simpledialog
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras import layers
from keras.models import Sequential
import pathlib

model = keras.models.load_model('C:/Users/amad_/makeaiwork2/mijn_model1')


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