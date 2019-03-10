#ADD dataset

import os
import requests

dirpath = 'C:/Users/mayank singh/Desktop/face1/'
dataset = os.listdir(dirpath)

token = "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1wczI0NyIsImZpcnN0bmFtZSI6Ik1heWFuayIsImVtYWlsIjoibXBzMjQuN0BnbWFpbC5jb20ifQ.MtHdT6zth_W_ioOQPkrtkQyx4RqfZWBIvmfcsulkUj0"
secret = "6053083da8b4c7ac1017073fa051084"
for data in dataset:
    img = open(os.path.join(dirpath,data),'rb')
    label = data.split('.')[0]

    payload = {
        'secretKey':secret,
        'apiKey':token,
        'label':label,
    'folderKey':"default"
    }

    r = requests.post('http://api.giscle.ml/face_search/train',data=payload,files={'image':img})

    if r.ok:
        print(r.json())