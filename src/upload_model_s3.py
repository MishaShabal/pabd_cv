import boto3
import dotenv

config = dotenv.dotenv_values('/home/misha/PycharmProjects/pabd_cv/.env')
# config = dotenv.dotenv_values('.env')
ACCESS_KEY = config['ACCESS_KEY']
SECRET_KEY = config['SECRET_KEY']

# model_path = '/home/misha/PycharmProjects/pabd_cv/models/model.zip'
model_path = 'models/my_model.zip'

client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

client.upload_file(model_path, 'pabdcv', '221675/model.zip')

