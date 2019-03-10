#get dataset

import os
import requests

token = "JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1wczI0NyIsImZpcnN0bmFtZSI6Ik1heWFuayIsImVtYWlsIjoibXBzMjQuN0BnbWFpbC5jb20ifQ.MtHdT6zth_W_ioOQPkrtkQyx4RqfZWBIvmfcsulkUj0"
secret = "053083da8b4c7ac1017073fa051084"

payload = {
    'secretKey':secret,
    'apiKey':token,
}
r = requests.post('http://api.giscle.ml/face_search/dataset',data=payload)

if r.ok:
    result = r.json()
    print(result)

else:
    r.status_code