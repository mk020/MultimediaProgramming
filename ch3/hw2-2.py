import cv2 as cv
import sys
import cvlib as cvl

#cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 동영상을 가져오는 클래스
cap = cv.VideoCapture('face2.mp4')

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

ksize = 31              # 블러 처리에 사용할 커널 크기

while True:  # 무한루프로
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득(frame)

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    faces, confidences = cvl.detect_face(frame)
    for (x, y, x2, y2), conf in zip(faces, confidences): # (좌측상단좌표,우측하단좌표)
        cv.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
        roi = frame[y:y2, x:x2]  # 얼굴 영역 지정
        roi = cv.GaussianBlur(roi, (ksize, ksize), 0.0)  # 블러링 : 모자이크
        frame[y:y2, x:x2] = roi  # 원본 동영상에 적용

    cv.imshow('face detection', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
