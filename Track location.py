#track Student & teacher location
import requests
import cv2

token = "yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1wczI0NyIsImZpcnN0bmFtZSI6Ik1heWFuayIsImVtYWlsIjoibXBzMjQuN0BnbWFpbC5jb20ifQ.MtHdT6zth_W_ioOQPkrtkQyx4RqfZWBIvmfcsulkUj0"
secret = "6053083da8b4c7ac1017073fa051084"
imageName = "C:/Users/mayank singh/Desktop/face1/chris.jpg"


img = open(imageName,'rb')

g_url = 'http://api.giscle.ml'
auth = {
    'secretKey':secret,
    'apiKey':token,
    'folderKey':"default"
    }

r = requests.post("{}/{}".format(g_url,'face_search'),data=auth, files={'img1':img})

if r.ok:
    result = r.json()
    print(result)
    if result['label'] == 1:
        image = cv2.imread(imageName)
        for person in result['result']:
                t,r,b,l = person['face']
                cv2.rectangle(image,(l,t),(r,b),(255,255,255))          
                cv2.putText(image,person['person'],(l,t-13),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255))
                
        cv2.imshow('Image',image)

else:
    print(r.status_code)
cv2.waitKey(0)
cv2.destroyAllWindows()    