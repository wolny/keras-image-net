# keras-image-net
Simple REST app for image classification using [Keras pre-trained deep learning models](https://keras.io/applications/).
By default the app uses [pre-trained ResNet-50 model](https://github.com/KaimingHe/deep-residual-networks) described in the paper "Deep Residual Learning for Image Recognition"
```
@article{He2015,
	author = {Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
	title = {Deep Residual Learning for Image Recognition},
	journal = {arXiv preprint arXiv:1512.03385},
	year = {2015}
}
```

## Run (Docker)
```
docker build -t keras-image-net .
docker run -p 5000:5000 keras-image-net
# wait for models to be loaded
# test with: curl -v http://localhost:5000/detect?imageUrl=<imageUrl>, e.g.
curl -v http://localhost:5000/detect?imageUrl=http://expressioncoffins.com.au/wp-content/uploads/2012/06/RED-TRACTOR1.jpg
```
You should get the following response:
```
{
"imageUrl": "http://expressioncoffins.com.au/wp-content/uploads/2012/06/RED-TRACTOR1.jpg",
"results": [
  {
    "score": 0.6732403039932251,
    "label": "tractor"
  },
  {
    "score": 0.3161275088787079,
    "label": "plow"
  },
  {
    "score": 0.010076208040118217,
    "label": "harvester"
  },
  {
    "score": 0.00041331720422022045,
    "label": "thresher"
  },
  {
    "score": 0.00006622869841521606,
    "label": "hay"
  }]
}
```

## Run (command line)
Make sure you have Keras installed, then just
```
python src/res-net-50.py
```
You should see:
```
('Predicted:', [(u'n02106662', u'German_shepherd', 0.99324906), (u'n02096051', u'Airedale', 0.0033434019), (u'n02105162', u'malinois', 0.0015451796), (u'n03803284', u'muzzle', 0.0005292811), (u'n02091635', u'otterhound', 0.00021379442)])
```

## Run (GCP)

```
docker build -t eu.gcr.io/$PROJECT_NAME/keras-res-net .
gcloud docker -- push eu.gcr.io/$PROJECT_NAME/keras-res-net
kubectl run keras-res-net --image=eu.gcr.io/$PROJECT_NAME/keras-res-net --port=5000 --replicas=2
kubectl expose deployment keras-res-net --type=LoadBalancer --name=keras-res-net
```
