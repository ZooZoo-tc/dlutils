import os.path
from os import path
from google.colab import drive
from google.colab import files
import tensorflow as tf

def is_file_exists(file_path):
      return path.exists(file_path)

def mkdirs(filepath):
      if not os.path.exists(filepath):
              os.makedirs(filepath)
def mount():
    drive.mount('/content/drive')

def downloadModelPlot(file_name= 'model_plot.png'):
      tf.keras.utils.plot_model(model, to_file=file_name, show_shapes=True, show_layer_names=True)
      files.download(file_name)