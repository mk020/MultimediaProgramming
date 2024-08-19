import cv2 as cv
import numpy as np
import time

img1=cv.imread('mot_color70.jpg')[190:350,440:560]  # 버스를 크롭하여 모델 영상으로 사용
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img2=cv.imread('mot_color83.jpg')			     # 장면 영상
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create()
kp1,des1=sift.detectAndCompute(gray1,None)
kp2,des2=sift.detectAndCompute(gray2,None)
print('특징점 개수:',len(kp1),len(kp2)) 

start=time.time()
# flann 방법
# flann_matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
# knn_match=flann_matcher.knnMatch(des1,des2,2)  # k=2
bf_matcher=cv.BFMatcher()  # 전수조사 방법
knn_match=bf_matcher.knnMatch(des1,des2,2)
print(len(knn_match))

T=0.7
good_match=[]
for nearest1,nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance)<T:
        good_match.append(nearest1)
print(len(good_match))
print(good_match[0].queryIdx, ' -- ', good_match[0].trainIdx, ' : ', good_match[0].distance)
# 왼쪽 이미지의 특징 기술자 인덱스, 오른쪽 이미지의 특징 기술자 인덱스
print('매칭에 걸린 시간:',time.time()-start)

img_match=np.empty((max(img1.shape[0],img2.shape[0]),img1.shape[1]+img2.shape[1],3),dtype=np.uint8)
# cv.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv.DrawMatchesFlags_DEFAULT)  # 모든 특징 표시

cv.imshow('Good Matches', img_match)

k=cv.waitKey()
cv.destroyAllWindows()