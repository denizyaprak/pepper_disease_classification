import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

dir = "C:/Code/pepper-bell-disease/training/Pepper_Bell_Images"

IMAGE_SIZE = 256
BATCH_SIZE = 32
CHANNELS = 3


dataset = tf.keras.preprocessing.image_dataset_from_directory(
    directory = dir,
    shuffle = True,
    image_size = (IMAGE_SIZE, IMAGE_SIZE),
    batch_size = BATCH_SIZE
)

print("the size of the dataset(the number of batches): ", len(dataset))



import os
file_counter = 0
for i in os.listdir(dir + "/Pepper__bell___Bacterial_spot"):
    file_counter += 1
print(file_counter) #997


file_counter_2 = 0
for i in os.listdir(dir + "/Pepper__bell___healthy"):
    file_counter_2 += 1
print(file_counter_2) # 1478 

# in total = 2475 images


