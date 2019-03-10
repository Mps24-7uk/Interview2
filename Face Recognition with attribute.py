#Image attribute detection
#Student Emotion detection

import requests
import cv2
import base64

token = "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1wczI0NyIsImZpcnN0bmFtZSI6Ik1heWFuayIsImVtYWlsIjoibXBzMjQuN0BnbWFpbC5jb20ifQ.MtHdT6zth_W_ioOQPkrtkQyx4RqfZWBIvmfcsulkUj0"

toStore = str(0)
g_url = 'http://api.giscle.ml'

imageName = "C:/Users/mayank singh/Desktop/PCD/class.jpg"
img = open(imageName,'rb')
img = img.read()
image = base64.b64encode(img)
payload = {'image':image}

r = requests.post(g_url + ':80/image', files=payload, headers={'token':token,'store':toStore})

if r.ok:
    result = r.json()

    image = cv2.imread(imageName)
    for key in result['Data'][2].keys():
            x,y,h,w = result['Data'][2][str(key)]['rect_coordinate']
            cv2.rectangle(image, (x,y),(x+h,y+w), (255,255,255))
            
            cv2.putText(image,str(result['Data'][2][str(key)]['Emotion']), (x+w,y ) , cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0), 1)
          
    cv2.imshow('Image',image)
    
else:
    print(r.status_code)
    
cv2.waitKey(0)
cv2.destroyAllWindows()    