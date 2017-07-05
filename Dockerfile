FROM gcr.io/tensorflow/tensorflow
RUN pip install keras
RUN pip install h5py
RUN pip install flask
RUN pip install flask-restful

ADD src/ /

WORKDIR /

EXPOSE 5000

CMD python server.py