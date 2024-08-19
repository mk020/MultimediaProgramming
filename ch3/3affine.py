import cv2 as cv
import numpy as np

img=cv.imread('rose.png')

rows,cols = img.shape[:2] #shpae은 영상의 크기(세로, 가로)

#Horizontal 좌우대칭
src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[cols-1,0], [0,0], [cols-1,rows-1]])

#Vertical 상하대칭
src_points = np.float32([[0,0], [cols-1,0], [0,rows-1]])
dst_points = np.float32([[0,rows-1], [cols-1,rows-1], [0,0]])

#Origin 원점대칭
src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
dst_points = np.float32([[cols-1,rows-1], [cols-1,0], [0,rows-1]])

#90 반시계방향 rotate
src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
dst_points = np.float32([[0,cols-1], [rows-1,cols-1], [0,0]])

#90 시계방향 rotate
src_points = np.float32([[0,0], [0,rows-1], [cols-1,0]])
dst_points = np.float32([[rows-1,0], [0,0], [rows-1,cols-1]])

affine_matrix = cv.getAffineTransform(src_points, dst_points) # 행렬만 만들어줌
#img_symmetry = cv.warpAffine(img, affine_matrix, (cols,rows)) # 영상 변수, 행렬 변수, 출력 영상 크기(가로,세로)
img_symmetry = cv.warpAffine(img, affine_matrix, (rows,cols))

cv.imshow('Original',img)
cv.imshow('Symmetry',img_symmetry)

cv.waitKey()
cv.destroyAllWindows()