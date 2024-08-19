import cv2 as cv
import numpy as np
import math

img = np.zeros((600,900,3), np.uint8)  # 세로*가로 * 3바이트 * unsigned int(1바이트)
img[:] = (255,255,255)  # 행렬을 흰색(바탕색)으로 초기화

BrushSiz=5  # 붓의 크기
Blue,Green,Red,Black,Pink=(255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,0,255)

def painting(event,x,y,flags,param):
    global ix, iy  # 전역변수 설정

    if event==cv.EVENT_LBUTTONDOWN or event==cv.EVENT_RBUTTONDOWN:	# 마우스 왼쪽 또는 오른쪽 버튼 클릭했을 때 초기 위치 저장
        ix,iy=x,y
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_SHIFTKEY:
        cv.line(img,(ix,iy),(x,y),Blue,5) # Shift + 마우스 왼쪽 버튼 다운/업 직선
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_ALTKEY:
        cv.rectangle(img,(ix,iy),(x,y),Green,5) # Alt + 마우스 왼쪽 버튼 다운/업 직사각형
    elif event==cv.EVENT_RBUTTONUP and flags==cv.EVENT_FLAG_ALTKEY:
        cv.rectangle(img,(ix,iy),(x,y),Red,cv.FILLED) # Alt + 마우스 오른쪽 버튼 다운/업 내부가 칠해진 직사각형
    elif event==cv.EVENT_LBUTTONUP and flags==cv.EVENT_FLAG_CTRLKEY:
        cv.circle(img,((ix+x)//2,(iy+y)//2),int(math.sqrt((x-ix)**2+(y-iy)**2)/2),Black,5) # Ctrl + 왼쪽 버튼 다운/업 원
        # r = np.sqrt((x - ix) * (x - ix) + (y - iy) * (y - iy))
        # cv.circle(img, (ix, iy), r.astype('i'), (255, 0, 255), 2) # r을 정수로 변환
    elif event==cv.EVENT_RBUTTONUP and flags==cv.EVENT_FLAG_CTRLKEY:
        cv.circle(img,((ix+x)//2,(iy+y)//2),int(math.sqrt((x-ix)**2+(y-iy)**2)/2),Pink,cv.FILLED) # Ctrl + 오른쪽 버튼 다운/업 내부가 칠해진 원
        # r = np.sqrt((x - ix) * (x - ix) + (y - iy) * (y - iy))
        # cv.circle(img, (ix, iy), r.astype('i'), (255, 0, 255), -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,Blue,-1) # 왼쪽 버튼 클릭하고 이동하면 파란색
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,Red,-1) # 오른쪽 버튼 클릭하고 이동하면 빨간색

    cv.imshow('Painting',img)		# 수정된 영상을 다시 그림

cv.namedWindow('Painting')
cv.imshow('Painting',img)

cv.setMouseCallback('Painting',painting) # Painting 윈도우에 painting 콜백 함수 지정

while(True):
    key = cv.waitKey(1)
    if key==ord('q'):
        cv.destroyAllWindows()      
        break