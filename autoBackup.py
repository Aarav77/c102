import cv2
import time
import random

import os
import dropbox
from dropbox.files import WriteMode
#
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token
#
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

            # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    # construct the full local path
                local_path = os.path.join(root, filename)

                    # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    # upload the file
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def upload_file(imageName):
    access_token = "RRmnQD7JTaIAAAAAAAAAAe392FipwJ1fOawE7J-3Oy2K87I9drMqNYqEyLfjG3QS"
    file = img_counter
    file_from = file
    file_to = "/Security/"+(imageName)
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from,'rb')
    transferData = TransferData(access_token)
    transferData.upload_file(file_from,file_to)
    print("Files Uploaded")

def main():
    while(True):
        if((time.time()-startTime) >= 300):
            name = takeSnapshot()
            upload_file(name)

main()