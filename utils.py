import os.path
from os import path
from google.colab import drive

def is_file_exists(file_path):
      return path.exists(file_path)

def mkdirs(filepath):
      if not os.path.exists(filepath):
              os.makedirs(filepath)
def mount():
    drive.mount('/content/drive')
