import cv2
import numpy as np
import face_recognition
import pickle
import time

# 카메라 입력을 Raspberry Pi Camera 대신 일반 웹캠으로 변경
camera = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다.

# OpenCV에서 사용할 얼굴 인식 XML 파일 경로
face_cascade_name = './haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

# 인코딩 데이터 로드
encoding_file = 'test_encodings.pickle'
with open(encoding_file, "rb") as f:
    data = pickle.load(f)

unknown_name = 'Unknown'
recognized_name = None
frame_count = 0
frame_interval = 8

catured_image = './image/captured_image.jpg'

while True:
    start_time = time.time()

    # 카메라에서 프레임 읽기
    ret, image = camera.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 이미지 저장 (디버깅 용도)
    cv2.imwrite(catured_image, image)
    
    # 얼굴 인식 처리
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray)

    rois = [(y, x + w, y + h, x) for (x, y, w, h) in faces]
    encodings = face_recognition.face_encodings(rgb, rois)

    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
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

        cv2.rectangle(image, (left, top), (right, bottom), color, line)
        y = top - 15 if top - 15 > 15 else top + 15
        cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, line)

    end_time = time.time()
    process_time = end_time - start_time
    print("=== A frame took {:.3f} seconds".format(process_time))
    cv2.imshow("Recognition", image)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
