"""Preprocess data to use it as tf dataset.
Take images from source dir and put in out dir subfolders: Cat and Dog"""
import os
import shutil

import click

# in_dir = 'data/raw/kaggle'
# out_dir = './data/processed/PetImages'


@click.command()
@click.option('-i', '--in_dir', default='/home/misha/PycharmProjects/pabd_cv/data/raw/kaggle')
@click.option('-o', '--out_dir', default='/home/misha/PycharmProjects/pabd_cv/data/processed/PetImages')
@click.option('-n', '--n_img', default=20)
def preprocess_data(in_dir, out_dir, n_img):
    # make_out_dirs(out_dir)
    copy_files(in_dir, out_dir, n_img)


def make_out_dirs(out_dir):
    if os.path.exists(out_dir):
        os.remove(out_dir)
        os.mkdir(out_dir)
        os.mkdir(os.path.join(out_dir, 'Cat'))
        os.mkdir(os.path.join(out_dir, 'Dog'))


def copy_files(in_dir, out_dir, n_img):
    all_files = os.listdir(in_dir)
    cat_imgs = [img for img in all_files if img.startswith('cat')]
    dog_imgs = [img for img in all_files if img.startswith('dog')]

    for cat_img in cat_imgs[:n_img]:
        shutil.copy2(
            os.path.join(in_dir, cat_img),
            os.path.join(out_dir, 'Cat')
        )

    for dog_img in dog_imgs[:n_img]:
        shutil.copy2(
                os.path.join(in_dir, dog_img),
                os.path.join(out_dir, 'Dog')
        )


if __name__ == '__main__':
    preprocess_data()
