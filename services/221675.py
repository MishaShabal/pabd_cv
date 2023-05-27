import os
import pathlib

from flask import Flask, request
import tensorflow as tf
from utils import data_to_img, predict_imagenet, predict_bimary

app = Flask('Image classifier')
resnet = tf.keras.applications.ResNet101()
with open('data/imgnet_cats_ru.txt', encoding='utf-8') as f:
    categories = f.readlines()

categories_ru = [s.rstrip() for s in categories]


@app.route('/')
def home():
    """ Function docstring """
    return 'Home page'


@app.route('/classify/imagenet', methods=['POST', 'GET'])
def classify_imagenet():
    data = request.data
    img = data_to_img(data)
    out = ', '.join([categories_ru[int(i)] for i in predict_imagenet(img, resnet)])
    return out


@app.route('/classify/binary', methods=['POST'])
def classify_binary():
    data = request.data
    img = data_to_img(data)
    return predict_bimary(img, 'models/my_model')


if __name__ == '__main__':
    app.run(port=1675)
    input()
