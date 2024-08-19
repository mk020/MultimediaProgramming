import cv2 as cv
import sys

#cap = cv.VideoCapture(0, cv.CAP_DSHOW)  # 동영상을 가져오는 클래스
cap = cv.VideoCapture('face2.mp4')

if not cap.isOpened():
    sys.exit('카메라 연결 실패')

color_model = 'y' # 기본적으로 YCbCr 컬러 모델을 선택

while True:  # 무한루프로
    ret, frame = cap.read()  # 비디오를 구성하는 프레임 획득(frame)

    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    if color_model == 'y':
        # YCbCr 컬러 모델 선택
        ycbcr_img = cv.cvtColor(frame, cv.COLOR_BGR2YCrCb)
        skin_mask = cv.inRange(ycbcr_img, (0,133,77), (255,173,127))  # Cb : 77 ~ 127, Cr : 133 ~ 173
    elif color_model == 'h':
        # HSV 컬러 모델 선택
        hsv_img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        skin_mask = cv.inRange(hsv_img, (0, 70, 50), (50, 150, 255))  # H : 0 ~ 50, S : 70 ~ 150, V : 50~255

    skin_result = cv.bitwise_and(frame, frame, mask=skin_mask)

    cv.imshow('skin color detection', skin_result)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('y'):
        color_model = 'y'  # YCbCr 컬러 모델 선택
    elif key == ord('h'):
        color_model = 'h'  # HSV 컬러 모델 선택

cap.release()
cv.destroyAllWindows()
