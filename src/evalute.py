import tensorflow as tf
import click


@click.command()
@click.option('-d', '--data_dir',
              default='/home/misha/PycharmProjects/pabd_cv/data/raw/pinterest')
@click.option('-m', '--model_dir',
              default='/home/misha/PycharmProjects/pabd_cv/models/colab_model')
@click.option('-r', '--report_path',
              default='/home/misha/PycharmProjects/pabd_cv/output/report.txt')
# @click.command()
# @click.option('-d', '--data_dir',
#               default='pabd_cv/data/raw/pinterest')
# @click.option('-m', '--model_dir',
#               default='pabd_cv/data/raw/pinterest')
# @click.option('-d', '--data_dir',
#               default='pabd_cv/data/raw/pinterest')
def evaluate(data_dir, model_dir, report_path):
    test_df = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        image_size=(180, 180))
    model = tf.keras.models.load_model(model_dir)
    metrics = [
        tf.metrics.BinaryAccuracy(),
        tf.metrics.Precision(),
        tf.metrics.Recall()
    ]
    model.compile(metrics=metrics)

    result = model.evaluate(test_df)
    loss, acc, precision, recall = result
    output = [
        f'test data len: {len(test_df)}\n'
        f'Accuracy: {acc:.3f}, Precision {precision:.3f}, Recall {recall:.3f}, loss: {loss:.3f}'
    ]
    with open(report_path, 'w+', encoding='utf-8') as f:
        f.writelines(output)


if __name__ == '__main__':
    evaluate()
