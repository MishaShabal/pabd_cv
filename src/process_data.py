"""Preprocess data to use it as tf dataset.
Take images from source dir and put in out dir subfolders: Cat and Dog"""
import os
import shutil
from PIL import Image

import click


@click.command()
# @click.option('-i', '--in_dir',
#               default='/home/misha/PycharmProjects/pabd_cv/data/raw/kaggle')
@click.option('-i', '--in_dir',
              default='pabd_cv/data/raw/kaggle')
# @click.option('-o', '--out_dir',
#               default='/home/misha/PycharmProjects/pabd_cv/data/processed/PetImages')
@click.option('-o', '--out_dir',
              default='pabd_cv/data/processed/PetImages')
@click.option('-n', '--n_img', default=20)
@click.option('-s', '--img_size', default=180)
def preprocess_data(in_dir, out_dir, n_img, img_size):
    make_out_dirs(out_dir)
    process_images(in_dir, out_dir, n_img, img_size)


def make_out_dirs(out_dir):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.mkdir(out_dir)
    os.mkdir(os.path.join(out_dir, 'Cat'))
    os.mkdir(os.path.join(out_dir, 'Dog'))


def process_images(in_dir, out_dir, n_img, img_size):
    all_files = os.listdir(in_dir)
    cat_imgs = [img for img in all_files if img.startswith('cat')]
    dog_imgs = [img for img in all_files if img.startswith('dog')]

    def resize_and_save(img_list, category_name):
        for im_name in img_list[:n_img]:
            im_img_path = os.path.join(in_dir, im_name)
            img = Image.open(im_img_path)
            img_r = img.resize((img_size, img_size))
            out_img_path = os.path.join(out_dir, category_name, im_name)
            img_r.save(out_img_path)

    resize_and_save(cat_imgs, "Cat")
    resize_and_save(dog_imgs, "Dog")


if __name__ == '__main__':
    preprocess_data()
