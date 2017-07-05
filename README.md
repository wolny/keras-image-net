# keras-image-net
Simple REST app for image classification using Keras pre-trained deep learning models

## Run
```
docker build -t keras-image-net .
docker run -p 5000:5000 keras-image-net
# wait for models to be loaded
# test with: curl -v http://localhost:5000/detect?imageUrl=<imageUrl>, e.g.
curl -v http://localhost:5000/detect?imageUrl=http://expressioncoffins.com.au/wp-content/uploads/2012/06/RED-TRACTOR1.jpg

```
