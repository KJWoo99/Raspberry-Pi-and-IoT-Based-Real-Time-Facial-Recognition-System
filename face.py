from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
import face_recognition
import pickle
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import dropbox
import os

#To Professor, if you run this file, you will get an error called token expiration.
#The dropbox_token key value is only valid for 4 hours
#After that, it need to reissue it
#If you want only face recognition (marked with green and red boxes) excluding cloud transmission,
#You can use the test.py file (however, pre-installation of open cv is required)

dropbox_token = 'Your dropbox_token!!!'
dbx = dropbox.Dropbox(dropbox_token)

face_cascade_name = './haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

encoding_file = 'encodings.pickle'

data = pickle.loads(open(encoding_file, "rb").read())

cred = credentials.Certificate('test11-5c9b1-fc45969de320.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test11-5c9b1-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

unknown_name = 'Unknown'
recognized_name = None
frame_count = 0
frame_interval = 8

frame_width = 640
frame_height = 480
frame_resolution = [frame_width, frame_height]
frame_rate = 16

camera = PiCamera()
camera.resolution = frame_resolution
camera.framerate = frame_rate
rawCapture = PiRGBArray(camera, size=(frame_resolution))
time.sleep(0.1)

catured_image = './image/captured_image.jpg'



for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    start_time = time.time()
    image = frame.array
    camera.capture(catured_image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray)

    rois = [(y, x + w, y + h, x) for (x, y, w, h) in faces]

    encodings = face_recognition.face_encodings(rgb, rois)

    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"],
            encoding)
        name = unknown_name

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)
        
        names.append(name)


    for ((top, right, bottom, left), name) in zip(rois, names):
        y = top - 15 if top - 15 > 15 else top + 15
        color = (0, 255, 0)
        line = 2
        if(name == unknown_name):
            color = (0, 0, 255)
            line = 1
            
        if(name != recognized_name):
            recognized_name = name
            print("Send Notice")
            current = str(time.ctime())
            path = '/' + current + name + '.jpg'
            print(path)
            
            ref = db.reference('Recognition')
            box_ref = ref.child(name)
            box_ref.update({
                'name': name,
                'time': time.ctime(),
                'path': path
            })
            dbx.files_upload(open(catured_image, "rb").read(), path)
            print(dbx.files_get_metadata(path))

        cv2.rectangle(image, (left, top), (right, bottom), color, line)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
            0.75, color, line)
                
    end_time = time.time()
    process_time = end_time - start_time
    print(" A frame took {:.3f} seconds".format(process_time))
    cv2.imshow("Recognition", image)

    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key == ord("q"):
        break
