import cv2
import dropbox
import time
import random

startTime=time.time()
def takeSnapshot():
    num=random.randint(0,1000)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        imageName="img"+str(num)+".png"
        cv2.imwrite(imageName, frame)
        startTime=time.time()
        result=False
    return imageName
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    acessToken='cKhvlm-3tHUAAAAAAAAAAcTlQq1NyInHsmaxdnielmL7efBncGGoSzvJHKO8PAVK'
    source=imageName
    fileTo="/security/"+imageName
    dbx=dropbox.Dropbox(acessToken)
    f=open(source, 'rb')
    dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
    print("filesUploaded")

def main():
    while(True):
        if((time.time()-startTime)>=300):
            name=takeSnapshot()
            uploadFile(name)

main()