import cv2 as cv
import sys

img=cv.imread('soccer.jpg')	# 영상 읽기

print(type(img)) # class 'numpy.ndarray'
print(img.shape) # img 배열의 크기 (img.shape[0], img.shape[1], img.shape[2])
                            # = (세로, 가로, 한 픽셀을 표현하는 데 필요한 바이트 수(3: RGB를 가지고 있는 color 이미지))
print(img[850][50][0], img[850][50][1], img[850][50][2]) # 850,50 위치의 BGR 픽셀값(0~255)

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    
cv.imshow('Image Display',img)	# 윈도우에 영상 표시, '창의 타이틀'

cv.waitKey() # 기다림
cv.destroyAllWindows() # 창 닫기