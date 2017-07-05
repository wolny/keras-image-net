from flask import Flask, request
from flask_restful import Resource, Api
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import tensorflow as tf
import numpy as np
import hashlib
import urllib

app = Flask(__name__)
api = Api(app)

model = ResNet50(weights='imagenet')
graph = tf.get_default_graph()


class ObjectDetection(Resource):
    def img_path(self, img_url):
        m = hashlib.md5()
        m.update(img_url)
        return '/tmp/' + m.hexdigest() + '.jpg'

    def to_detection(self, d):
        x, label, score = d
        # convert score from 'numpy.float32' to normal 'float'
        return {'label': label, 'score': score.item()}

    def get(self):
        with graph.as_default():
            img_url = request.args.get('imageUrl')
            path = self.img_path(img_url)

            urllib.urlretrieve(img_url, path)
            img = image.load_img(path, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            preds = model.predict(x)
            # decode the results into a list of tuples (class, description, probability)
            # (one such list for each sample in the batch)
            print('Predicted:', decode_predictions(preds, top=5)[0])

            result = {'imageUrl': img_url, 'results': [self.to_detection(d) for d in decode_predictions(preds, top=5)[0]]}
            return result

api.add_resource(ObjectDetection, '/detect')

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
