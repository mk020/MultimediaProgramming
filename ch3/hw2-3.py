import cv2 as cv
import numpy as np

img=cv.imread('rose.png')

def rotate_image(event, x, y, flags, param):
    global img
    global rows, cols
    rows, cols = img.shape[:2]  # shape은 영상의 크기(세로, 가로)

    if event == cv.EVENT_LBUTTONDOWN:
        # 왼쪽 마우스 버튼 클릭 시 시계 반대 방향으로 90도 회전
        src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
        dst_points = np.float32([[0,cols-1], [rows-1,cols-1], [0,0]])

        affine_matrix = cv.getAffineTransform(src_points, dst_points) # 행렬만 만들어줌
        img = cv.warpAffine(img, affine_matrix, (rows, cols)) # 영상 변수, 행렬 변수, 출력 영상 크기(가로,세로)

        cv.imshow('Rotated Image', img)

        rows,cols=cols,rows  # 세로 가로 바꿔줌

    elif event == cv.EVENT_RBUTTONDOWN:
        # 오른쪽 마우스 버튼 클릭 시 시계 방향으로 90도 회전
        src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
        dst_points = np.float32([[rows-1,0], [0,0], [rows-1,cols-1]])

        affine_matrix = cv.getAffineTransform(src_points, dst_points)
        img = cv.warpAffine(img, affine_matrix, (rows, cols))

        cv.imshow('Rotated Image', img)

        rows,cols=cols,rows  # 세로 가로 바꿔줌

cv.imshow('Rotated Image',img)
cv.setMouseCallback('Rotated Image',rotate_image) # 윈도우에 rotate_image 콜백 함수 지정

while(True):
    key = cv.waitKey(1)
    if key==ord('q'):
        cv.destroyAllWindows()
        break