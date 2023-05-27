import io
import unittest
import PIL.Image
import requests
# import services.server_221675
from requests import request


class MyTestCase(unittest.TestCase):
    # def setUp(self):
        # app.run()

    def test_home(self):
        response = requests.request('GET', 'http://localhost:1675/')
        sample = response.content.decode()
        self.assertEqual(sample, 'Home page')  # add assertion here

    def test_classify_imagenet(self):
        img = PIL.Image.open('../data/dog.jpg')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')

        with buffer as buf:
            buffer.seek(0)
            response = request('POST', 'http://localhost:1675/classify/imagenet', data=buf)

        out = response.content.decode('utf-8')
        print(out)
        expected = 'Пембрук'

        self.assertIn(expected, out)


    def test_classify_binary(self):
        img = PIL.Image.open('../data/cat.jpg')
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')

        with buffer as buf:
            buffer.seek(0)
            response = request('POST', 'http://localhost:1675/classify/binary', data=buf)

        out = response.content.decode('utf-8')
        print(out)
        expected = 'Cat'

        self.assertEqual(expected, out)



if __name__ == '__main__':
    unittest.main()
