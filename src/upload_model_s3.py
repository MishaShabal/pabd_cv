import boto3

ACCESS_KEY = ''
SECRET_KEY = ''

model_path = 'models/my_model.zip'

client = boto3.clent(
    's3',
    endpoint_url = 'https://storage.yandex.cloud.net',
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY
)


# Получить список объектов в строке

client.upload_file(model_path, 'pabdcv', '221675/model.zip')

for key in client.list(Busket='pabdcv', Key= '')