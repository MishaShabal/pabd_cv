import tensorflow as tf


def data_to_img(data, size):
    img = tf.io.decode_jpeg(data)
    img_t = tf.expand_dims(img, axis=0)
    return tf.image.resize(img_t, (size, size))


def predict_imagenet(img, model):
    out = model(img)
    return tf.argsort(out, direction='DESCENDING')[0][:3].numpy()


def predict_imagenet(img, model):
    out = model(img)
    return tf.argsort(out, direction='DESCENDING')[0][:3].numpy()

def predict_bimary(img, path):
    model = tf.keras.models.load_model('models/my_model')
    out = model(img)
    dog_probability = out.numpy()[0, 0]
    idx = dog_probability > 0.5
    return ('Cat', 'Dog')[idx]

